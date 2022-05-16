# My C Programming Lecture Notes

These are the sources of my introduction to programming in C @ the Federal University of Uberlândia.
I haven´t taught this course in a while and when I did, the notes were in LaTeX, but thought it would be useful to update the notes in case anyone out there is interested.
Given that I am not teaching it, expect the conversion to be slow. Feel free to make PRs if you want to speed the process. 

For the live current version, go to (https://lasarojc.github.io/c_notes/)

To build your own version and deploy, use `mkdocs`

* `python3 -m pip install git+https://github.com/Python-Markdown/markdown.git`
* `python3 -m pip install mkdocs-material`
* `python3 -m pip install mkdocs-drawio-exporter`
* `python3 -m pip install python-markdown-math`
* `python3 -m pip upgrade pymdown-extensions`
* `python3 -m pip install mkdocs-drawio-exporter`
* `python3 -m mkdocs serve` - and then access localhost:8000
* `python3 -m mkdocs gh-deploy` - then go to your project's site, like (https://lasarojc.github.io/c_notes/)
