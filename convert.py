#!/usr/bin/env python3
"""Convert c_notes LaTeX to Markdown and split by chapter."""

import re
import os
import unicodedata

DOCS_DIR = '/Users/lasaro/code/lasaro/c_notes/docs'
# The source file contains the full multi-chapter LaTeX content
SOURCE_FILE = f'{DOCS_DIR}/intro/index.md'
MKDOCS_FILE = '/Users/lasaro/code/lasaro/c_notes/mkdocs.yml'


def convert_inline_cell(text):
    """Lightweight inline conversion for table cell content (verb, lstinline, emph, textbf, texttt)."""
    text = re.sub(r'\\verb\*?(.)(.*?)\1', lambda m: f'`{m.group(2)}`', text)
    text = re.sub(r'\\lstinline\{([^}]*)\}', lambda m: f'`{m.group(1)}`', text)
    text = re.sub(r'\\lstinline(.)(.*?)\1', lambda m: f'`{m.group(2)}`', text)
    for _ in range(3):
        text = re.sub(r'\\emph\{([^{}]*)\}', r'*\1*', text)
        text = re.sub(r'\\textbf\{([^{}]*)\}', r'**\1**', text)
        text = re.sub(r'\\texttt\{([^{}]*)\}', r'`\1`', text)
        text = re.sub(r'\\textit\{([^{}]*)\}', r'*\1*', text)
    text = re.sub(r'\\footnote\{([^{}]*)\}', r' (\1)', text)
    text = re.sub(r'~?\\ref\{[^}]*\}', '', text)
    text = re.sub(r'\\ldots\b', '...', text)
    text = re.sub(r'\\rightarrow\b', '→', text)
    text = re.sub(r'\\times\b', '×', text)
    text = re.sub(r'\\%', '%', text)
    text = re.sub(r'\\\$', '$', text)
    text = re.sub(r"\`\`(.*?)''", r'"\1"', text)
    return text.strip()


def convert_tabular(content, spec):
    """Convert LaTeX tabular to Markdown table."""
    lines = content.strip().split('\n')
    rows = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Skip pure \hline rows
        cleaned = re.sub(r'\\hline', '', line).strip()
        if not cleaned:
            continue
        # Remove trailing \\
        cleaned = re.sub(r'\\\\\s*$', '', cleaned).strip()
        # Remove \hline occurrences within the line
        cleaned = re.sub(r'\\hline\s*', '', cleaned).strip()
        if not cleaned:
            continue
        # Split on unescaped & only (not \&)
        cells = [cell.strip() for cell in re.split(r'(?<!\\)&', cleaned)]
        # Process each cell: convert \& → &, then run inline conversion,
        # then escape any remaining | that are outside code spans
        processed = []
        for c in cells:
            c = c.replace(r'\&', '&')
            c = convert_inline_cell(c)
            # Escape bare | not inside backtick spans
            c = re.sub(r'\|(?=[^`]*(?:`[^`]*`[^`]*)*$)', r'\\|', c)
            processed.append(c)
        rows.append(processed)

    if not rows:
        return ''

    ncols = max(len(row) for row in rows)

    def pad(row):
        while len(row) < ncols:
            row.append('')
        return row

    result = []
    result.append('| ' + ' | '.join(pad(rows[0])) + ' |')
    result.append('| ' + ' | '.join(['---'] * ncols) + ' |')
    for row in rows[1:]:
        result.append('| ' + ' | '.join(pad(row)) + ' |')

    return '\n'.join(result)


def convert_itemize(content, bullet='-'):
    """Convert itemize/enumerate content to list items."""
    items = re.split(r'\\item\b', content)
    result = []
    for i, item in enumerate(items):
        item = item.strip()
        if not item:
            continue
        # Handle \item[label] in description lists
        m = re.match(r'^\[([^\]]*)\]\s*', item)
        if m:
            label = m.group(1)
            rest = item[m.end():]
            result.append(f'**{label}**: {rest.strip()}')
        else:
            if bullet == 'num':
                result.append(f'{len(result)+1}. {item}')
            else:
                result.append(f'{bullet} {item}')
    return '\n\n'.join(result)


def convert_block_environments(text):
    """Convert LaTeX block environments to Markdown (multiple passes for nesting)."""

    # STEP 1: Convert lstlisting and verbatim to fenced code blocks
    def replace_lstlisting(m):
        opts = m.group(1) or ''
        code = m.group(2)
        cap_m = re.search(r'caption=\{([^}]*)\}', opts) or re.search(r'caption=([^,\]]*)', opts)
        caption = cap_m.group(1).strip() if cap_m else ''
        header = '```c'
        if caption:
            header = f'```c\n// {caption}'
        return header + '\n' + code.strip('\n') + '\n```'

    text = re.sub(
        r'\\begin\{lstlisting\}(?:\[([^\]]*)\])?\n?(.*?)\\end\{lstlisting\}',
        replace_lstlisting, text, flags=re.DOTALL
    )
    text = re.sub(
        r'\\begin\{verbatim\}(.*?)\\end\{verbatim\}',
        lambda m: '```\n' + m.group(1).strip('\n') + '\n```',
        text, flags=re.DOTALL
    )

    # STEP 2: Protect fenced code blocks so subsequent transforms don't touch them
    text, code_placeholders = protect_fenced(text)

    # STEP 3: All remaining block environment conversions

    # quote → blockquote
    def replace_quote(m):
        lines = m.group(1).strip().split('\n')
        return '\n'.join('> ' + line for line in lines)

    text = re.sub(
        r'\\begin\{quote\}(.*?)\\end\{quote\}',
        replace_quote, text, flags=re.DOTALL
    )

    # Do itemize/enumerate multiple passes to handle nesting
    for _ in range(4):
        text = re.sub(
            r'\\begin\{itemize\}(.*?)\\end\{itemize\}',
            lambda m: convert_itemize(m.group(1), '-'),
            text, flags=re.DOTALL
        )
        text = re.sub(
            r'\\begin\{enumerate\}(.*?)\\end\{enumerate\}',
            lambda m: convert_itemize(m.group(1), 'num'),
            text, flags=re.DOTALL
        )
        text = re.sub(
            r'\\begin\{description\}(.*?)\\end\{description\}',
            lambda m: convert_itemize(m.group(1), '-'),
            text, flags=re.DOTALL
        )

    # exercicio → admonition
    def replace_exercicio(m):
        content = m.group(1).strip()
        indented = '\n'.join('    ' + line for line in content.split('\n'))
        return '!!! question "Exercício"\n' + indented

    text = re.sub(
        r'\\begin\{exercicio\}(.*?)\\end\{exercicio\}',
        replace_exercicio, text, flags=re.DOTALL
    )

    # lab → admonition
    def replace_lab(m):
        content = m.group(1).strip()
        indented = '\n'.join('    ' + line for line in content.split('\n'))
        return '!!! example "Laboratório"\n' + indented

    text = re.sub(
        r'\\begin\{lab\}(.*?)\\end\{lab\}',
        replace_lab, text, flags=re.DOTALL
    )

    # tabular → markdown table (multiple passes for nesting)
    for _ in range(2):
        text = re.sub(
            r'\\begin\{tabular\}\{([^}]*)\}(.*?)\\end\{tabular\}',
            lambda m: convert_tabular(m.group(2), m.group(1)),
            text, flags=re.DOTALL
        )

    # Remove environment wrappers that just wrap content
    for env in ['center', 'figure', 'table', 'subfigure']:
        text = re.sub(rf'\\begin\{{{env}\}}(?:\[[^\]]*\])?', '', text)
        text = re.sub(rf'\\begin \{{{env}\}}(?:\[[^\]]*\])?', '', text)
        text = re.sub(rf'\\end\{{{env}\}}', '', text)

    # Remove \subfigure{ (not \begin{subfigure}) - just drop the command
    text = re.sub(r'\\subfigure\{', '', text)

    # Remove bare { } lines (used as scoping braces around tabulars etc.)
    text = re.sub(r'^\{\s*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\}\s*$', '', text, flags=re.MULTILINE)

    # STEP 4: Restore fenced code blocks
    text = restore_fenced(text, code_placeholders)

    return text


def convert_headings(text):
    """Convert LaTeX headings to Markdown."""
    text = re.sub(r'\\chapter\*?\{([^}]*)\}', r'# \1', text)
    text = re.sub(r'\\part\*?\{([^}]*)\}', r'# Part: \1', text)
    text = re.sub(r'\\subsubsection\*?\{([^}]*)\}', r'#### \1', text)
    # Remove braces (and optional *) from already-converted ## {Title} or ## *{Title} headings
    text = re.sub(r'^(#{1,6})\s*\*?\{(.*?)\}\s*$', r'\1 \2', text, flags=re.MULTILINE)
    return text


def convert_inline(text):
    """Convert inline LaTeX commands to Markdown."""

    # \\ (LaTeX forced line break) → space (handle both end-of-line and mid-line)
    text = re.sub(r'\\\\\s*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'\\\\', ' ', text)

    # \verb<delim>...<delim>
    def replace_verb(m):
        content = m.group(2)
        if '`' in content:
            return f'`` {content} ``'
        return f'`{content}`'
    text = re.sub(r'\\verb\*?(.)(.*?)\1', replace_verb, text)

    # \lstinline{...}, \lstinline<delim>...<delim>
    text = re.sub(r'\\lstinline\{([^}]*)\}', lambda m: f'`{m.group(1)}`', text)
    text = re.sub(r'\\lstinline(.)(.*?)\1', lambda m: f'`{m.group(2)}`', text)

    # Repeated passes to handle nested braces in formatting commands
    for _ in range(4):
        text = re.sub(r'\\emph\{([^{}]*)\}', r'*\1*', text)
        text = re.sub(r'\\textbf\{([^{}]*)\}', r'**\1**', text)
        text = re.sub(r'\\texttt\{([^{}]*)\}', r'`\1`', text)
        text = re.sub(r'\\textit\{([^{}]*)\}', r'*\1*', text)
        text = re.sub(r'\\text\{([^{}]*)\}', r'\1', text)

    # \href{url}{text}
    text = re.sub(r'\\href\{([^}]*)\}\{([^}]*)\}', r'[\2](\1)', text)

    # \url{...}
    text = re.sub(r'\\url\{([^}]*)\}', r'<\1>', text)

    # \footnote{...} → inline parenthetical (single-line)
    # Multiple passes for nesting
    for _ in range(3):
        text = re.sub(r'\\footnote\{([^{}]*)\}', r' (\1)', text)

    # References and labels
    text = re.sub(r'[~\s]*\\ref\{[^}]*\}', '', text)
    text = re.sub(r'\\label\{[^}]*\}', '', text)
    text = re.sub(r'\\pageref\{[^}]*\}', '', text)

    # \todo{...}
    text = re.sub(r'\\todo\{([^}]*)\}', r'<!-- TODO: \1 -->', text)
    text = re.sub(r'\\todo\b', '<!-- TODO -->', text)

    # \includegraphics[...]{path}
    text = re.sub(r'\\includegraphics\[[^\]]*\]\{([^}]*)\}', r'![](\1)', text)
    text = re.sub(r'\\includegraphics\{([^}]*)\}', r'![](\1)', text)

    # \caption{...}
    text = re.sub(r'\\caption\{([^}]*)\}', r'*\1*\n', text)

    # Symbols
    text = re.sub(r'\\ldots\b', '...', text)
    text = re.sub(r'\\dots\b', '...', text)
    text = re.sub(r'\\rightarrow\b', '→', text)
    text = re.sub(r'\\leftarrow\b', '←', text)
    text = re.sub(r'\\Rightarrow\b', '⇒', text)
    text = re.sub(r'\\Leftarrow\b', '⇐', text)
    text = re.sub(r'\\times\b', '×', text)
    text = re.sub(r'\\infty\b', '∞', text)
    text = re.sub(r'\\pm\b', '±', text)
    text = re.sub(r'\\sqrt\b', '√', text)

    # LaTeX special characters
    text = re.sub(r'\\%', '%', text)
    text = re.sub(r'\\&', '&', text)
    text = re.sub(r'\\_', '_', text)
    text = re.sub(r'\\#', '#', text)
    text = re.sub(r'\\\$', '$', text)
    text = re.sub(r'\\{', '{', text)
    text = re.sub(r'\\}', '}', text)

    # LaTeX quotes → Unicode
    text = re.sub(r"``(.*?)''", r'"\1"', text)
    text = re.sub(r"`(.*?)'", r"'\1'", text)

    # ~ → space (non-breaking space)
    text = text.replace('~', ' ')

    # Remove stray commands
    text = re.sub(r'\\newpage\b', '', text)
    text = re.sub(r'\\centering\b', '', text)
    text = re.sub(r'\\small\b', '', text)
    text = re.sub(r'\\large\b', '', text)
    text = re.sub(r'\\Large\b', '', text)
    text = re.sub(r'\\hline\b', '', text)
    text = re.sub(r'\\textwidth\b', '', text)
    text = re.sub(r'\\tnome\{[^}]*\}', '', text)
    text = re.sub(r'\\tnome\b', '', text)
    text = re.sub(r'\\n\b', '\\n', text)

    # \Delta, \pi, etc. in non-math context — leave as-is (MathJax handles in $...$)

    return text


def protect_fenced(text):
    """Replace fenced code blocks with placeholders."""
    placeholders = {}
    counter = [0]

    def replace(m):
        key = f'\x00BLOCK{counter[0]}\x00'
        counter[0] += 1
        placeholders[key] = m.group(0)
        return key

    text = re.sub(r'```.*?```', replace, text, flags=re.DOTALL)
    return text, placeholders


def restore_fenced(text, placeholders):
    for key, value in placeholders.items():
        # Check if placeholder appears with leading indentation (inside an admonition)
        indented_pattern = re.compile(r'^( {2,})' + re.escape(key) + r'\s*$', re.MULTILINE)
        def make_replacer(val):
            def replacer(m):
                indent = m.group(1)
                lines = val.split('\n')
                return '\n'.join(indent + line if line.strip() else '' for line in lines)
            return replacer
        text = indented_pattern.sub(make_replacer(value), text)
        # Replace any remaining unindented occurrences
        text = text.replace(key, value)
    return text


def convert(text):
    """Full LaTeX → Markdown conversion."""
    text = convert_block_environments(text)
    text = convert_headings(text)

    # Protect fenced code blocks before inline conversion (simple restore — no re-indenting)
    text, placeholders = protect_fenced(text)
    text = convert_inline(text)
    # Simple restore: just substitute, indentation was already handled in block env conversion
    for key, value in placeholders.items():
        text = text.replace(key, value)

    # Clean up
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = text.strip() + '\n'
    return text


def slugify(title):
    """Convert title to ASCII slug."""
    title = unicodedata.normalize('NFKD', title)
    title = title.encode('ascii', 'ignore').decode('ascii')
    title = title.lower()
    title = re.sub(r'[^a-z0-9\s-]', '', title)
    title = re.sub(r'\s+', '-', title.strip())
    title = re.sub(r'-+', '-', title)
    return title[:40].strip('-')


def split_and_convert(text):
    """Split text by \\chapter{} and convert each part. Returns list of (title, slug, content)."""
    # Split on \chapter{...} boundaries
    # First part has no \chapter{} prefix (it's chapter 1 with existing # heading)
    pattern = r'(?=\\chapter\{)'
    parts = re.split(pattern, text)

    results = []
    for i, part in enumerate(parts):
        part = part.strip()
        if not part:
            continue

        if i == 0:
            # Extract title from existing # heading
            m = re.match(r'^#\s+(.+)', part)
            title = m.group(1).strip() if m else 'Introdução'
        else:
            # Extract title from \chapter{...}
            m = re.match(r'\\chapter\{([^}]*)\}', part)
            title = m.group(1).strip() if m else f'Capítulo {i}'

        converted = convert(part)
        results.append((title, converted))

    return results


def build_nav_yaml(chapters):
    """Build mkdocs nav entries for chapters."""
    lines = ['nav:']
    lines.append('        - Apresentação: preface.md')
    lines.append('        - Capítulos:')
    for title, filename in chapters:
        lines.append(f'            - "{title}": {filename}')
    return '\n'.join(lines)


def main():
    print(f'Reading {SOURCE_FILE}...')
    with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
        text = f.read()

    # Pre-process the full text before splitting
    # Strip \iffalse ... \fi blocks that may span chapter boundaries
    text = re.sub(r'\\iffalse.*?\\fi\b', '', text, flags=re.DOTALL)
    # Un-comment any commented-out \chapter{} lines so they still split correctly
    # Handles: %\chapter{...}, % \chapter{...}, %TODO: \chapter{...}, etc.
    text = re.sub(r'^%[^\n]*(\\chapter\{)', r'\1', text, flags=re.MULTILINE)
    # Strip remaining LaTeX comments
    text = re.sub(r'^%.*$', '', text, flags=re.MULTILINE)

    print('Splitting and converting...')
    chapters = split_and_convert(text)

    chapter_nav = []
    for i, (title, content) in enumerate(chapters):
        num = str(i + 1).zfill(2)
        filename = f'cap{num}.md'

        filepath = os.path.join(DOCS_DIR, filename)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        chapter_nav.append((title, filename))
        print(f'  Written: {filename} — {title}')

    # Update mkdocs.yml nav section
    print('\nUpdating mkdocs.yml nav...')
    with open(MKDOCS_FILE, 'r', encoding='utf-8') as f:
        yml = f.read()

    nav_block = build_nav_yaml(chapter_nav)
    # Replace existing nav: block
    yml = re.sub(r'nav:.*$', nav_block, yml, flags=re.DOTALL)

    with open(MKDOCS_FILE, 'w', encoding='utf-8') as f:
        f.write(yml)

    print('Done.')
    print(f'\n{len(chapters)} chapters written.')


if __name__ == '__main__':
    main()
