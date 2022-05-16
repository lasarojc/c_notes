# O computador é uma máquina burra

Computadores são máquinas "burras" que não fazem nada além de seguir instruções. 
Sendo assim, eles precisam de instruções precisas e detalhadas sobre o que fazer. 
Agora que está ciente deste fato, você está pronto para entender que quando o programa não fizer o que você quer, é por que você lhe deu instruções erradas. 

Para que não cometamos erros (ou pelo menos para minimizá-los), ao montar a sequência de instruções que resolvem determinado problema precisamos, antes de qualquer outra coisa, entender o problema e sermos capazes de resolvê-lo ``na mão''. 
Uma vez que tenhamos uma solução teremos o que chamamos de um \emph{algoritmo}\footnote{\url{http://www.merriam-webster.com/dictionary/algorithm}}.

## Algoritmo 
Um algoritmo nada mais é que um conjunto de instruções para se resolver um problema. Por exemplo, para se destrancar uma porta temos o seguinte algoritmo:

\begin{itemize}
\item Coloque a chave na fechadura
\item Gire a chave
\end{itemize}

É claro que este algoritmo está em um nível de abstração muito alto e que poderia ser muito mais detalhado. Por exemplo, não há por quê destrancar a porta se ela já estiver destrancada e não há como destrancá-la se não estiver de posse da chave. Quanto mais detalhada sua sequência de passos, mais próximo de algo inteligível ao computador ela será. Para que isto ocorra, isto é, para que o computador entenda suas intruções, além de detalhadas, eles precisam ser escritas em uma linguagem de programação.

## {Linguagem de Programação}
De acordo com fontes altamente confiáveis\footnote{\url{http://en.wikipedia.org/wiki/Programming\_language}}
\begin{quote}
%\emph{A programming language is an artificial language designed to communicate instructions to a machine, particularly a computer. Programming languages can be used to create programs that control the behavior of a machine and/or to express algorithms precisely.}
Uma linguagem de programação é uma linguagem artificial projetada para comunicar instruções a uma máquina, particularmente computadores. Linguagens de programação podem ser usadas para criar programas que controlam o comportamento da máquina e expressar algoritmos de forma precisa (não ambígua).
\end{quote}
De forma simplificada, uma liguagem de programação é um conjunto de palavras e regras sobre como usá-las na descrição de algoritmos interpretáveis por um computador. 

Existem diversas
\footnote{Uma listagem não completa mas ainda assim impressionante pode ser encontrada em \url{http://en.wikipedia.org/wiki/Categorical_list_of_programming_languages}} linguagens de programação, tendo cada uma seus pontos fortes e fracos; neste curso, usaremos as linguagens C e C++.

## {A linguagem C(++)}
A primeira encarnação da linguagem de programação  \href{http://en.wikipedia.org/wiki/C_(programming_language)}{C} foi desenvolvida no fim da década de 60, tendo sido extendida, melhorada e padronizada várias vezes depois. A linguagem C++, que extende a linguagem C com diversas funcionalidades como orientação a objetos, começou a ser desenvolvida na década de 70 e, como a linguagem C, também passou por várias reformas. 
Como resultado, hoje temos uma linguagem C++ padronizada que pode ser usada, mesmo que com certa dificuldade, para se programar em vários sistemas operacionais de forma portável. 
Além disso, a linguagem C++ é um super conjunto da linguagem C. Ou seja, todo e qualquer programa em C também é um programa em C++, mesmo que o oposto não seja verdade.

Como já mencionado, neste curso usaremos primariamente a linguagem C. Contudo, uma vez que o objetivo deste curso é introduzir o uso do raciocício computacional e não aprofundar no uso de determinada linguagem, estudaremos somente os aspectos mais básicos da linguagem C. Além disso, usaremos partes da linguagem C++ para simplificar o desenvolvimento dos nossos programas. Assim, nos referiremos à linguagem usada como C(++), pois nem é toda a C, e nem é somente C, mas não chega a ser C++. Mas chega de ladainha; vamos ao nosso primeiro programa em linguagem C(++)!

### {Meu Primeiro Programa}
O algoritmo em linguagem C(++)
\footnote{Usaremos também os termos ``programa'' e ``código'' para nos referirmos a tais algoritmos.}, 
abaixo, descreve para o computador os passos necessários para se escrever a mensagem ``Olá Mundo!'' na tela do computador. Não se preocupe com os detalhes de como isso é feito agora, mas foque-se nos seguintes aspectos:
\begin{itemize}
\item existem várias formas de se dizer ``Olá Mundo!'', por exemplo se pode saltar antes de fazê-lo, agaixar, ou fechar os olhos. Todas estas formas são corretas, embora algumas possam lhe causar certo constrangimento quando em público.

\item um código de computador deve ser entendido, além de pelos computadores, também por humanos. Sendo assim, é imprescindível que você mantenha o código organizado.

\item usar acentos em um programa é fonte de dores de cabeça; melhor simplesmente ignorá-los em nosso curso.
\end{itemize}

\begin{lstlisting}[caption=Ola Mundo!, label=cod:ola]
#include <iostream>

using namespace std;

int main()
{
    cout << "Ola Mundo!" << endl;
    return 0;
}

\end{lstlisting}

Analisando o Código~\ref{cod:ola}, podemos facilmente identificar a linha que contém a frase ``Ola Mundo!''. Esta linha é a que efetivamente \emph{escreve} na tela do computador. Altere esta linha para que contenha, por exemplo, seu nome em vez da palavra \emph{Mundo}. Digamos que seu nome seja \emph{Feissibukson}. Este programa agora escreve na tela do computador os dizeres ``Ola Feissibukson!''. 

Para entendermos o que as demais linhas fazem, precisamos passar para o nosso próximo problema/programa.


### {Área de um Retângulo}
A área de um retângulo pode ser facilmente calculada caso você saiba o comprimento de sua base e de sua altura. Matematicamente, seja $b$ o comprimento da base e $a$ a altura. A função $f$ equivalente à área do retângulo pode ser definda como: $f(a,b) = a*b$. Isto é, a função $f$ tem dois parâmetros (a altura $a$ e base $b$ do retângulo) e calcula a área como sendo a multiplicação de $a$ e $b$. 

Em linguagem C(++) a função $f$ pode-se escrever esta função como mostrado no Código~\ref{cod:area}, que analisaremos em seguida.

\begin{lstlisting}[caption=Área de um retângulo, label=cod:area]
int f(int a, int b)
{
    return a * b;
}
\end{lstlisting}

A linha 1 do código define a função \verb|f| como uma função que aceita dois parâmetros \lstinline!a! e \lstinline!b!. Além disso, esta função também define que cada um destes parâmetros é um número inteiro ao preceder cada parâmetro pela palavra \lstinline!int!. Finalmente, esta linha também define que o resultado da função será um número inteiro ao preceder o nome da função (\lstinline!f!) pela palavra \lstinline!int!. Isto quer dizer que você não pode usar esta função para calcular a área de retângulos cujos lados não sejam inteiros. Mas não se preocupe, corrigiremos esta deficiência daqui a pouco.

As linhas 2 e 4 definem o \emph{corpo da função}, isto é, quais outras linhas são partes da função \lstinline!f!. Toda função na linguagem C precisa ter definido seu começo e fim usando \lstinline!{! e \lstinline!}!, respectivamente.

A linha 3 do código é onde o cálculo da área é efetivamente executado: \lstinline!a*b!. Além disso, esta linha define também qual é o resultado da função ao preceder o resultado da multiplicação por \lstinline!return!. Como a multiplicação de dois números inteiros só pode resultar em um número inteiro, o resultado da função também é inteiro, está justificado o tipo da função ser \lstinline|int|.

### {Tipos Primitivos da Linguagem C}
O Código~\ref{cod:area}, como mencionado, tem a limitação de só calcular a área de retângulos cujos lados tenham tamanhos inteiros. Para corrigir esta deficiência, vamos alterá-lo para que aceite números reais. Em computação, números reais são também chamados de números com \emph{pontos flutuantes} e, em linguagem C, simplesmente de \lstinline!float!. Sendo assim, podemos corrigir o programa simplesmente substituindo as ocorrências da palavra \lstinline!int! por \lstinline!float!, resultando no Código~\ref{cod:area1}

\begin{lstlisting}[caption=Área de retângulo com dimensões reais., label=cod:area1]
float f(float a, float b)
{
    return a * b;
}
\end{lstlisting}

Pronto, a função agora \emph{recebe} dois parâmetros do tipo \verb|float| e \emph{retorna} um resultado também deste tipo. Juntamente com outros tipos que serão vistos adiante no curso, \verb|int| e \verb|float| são chamados de tipos de dados primitivos da linguagem. Isto sugere, obviamente, que há também tipos não primitivos, e nada poderia ser mais verdade. Estes tipos, contudo, só serão vistos bem mais adiante no curso, no Capítulo~?\todo{Adicionar referência}.

### {Organização do Código}
É possível facilmente perceber um padrão nos exemplos de código apresentados até agora:
\begin{itemize}
\item A linha definindo a função é seguida por uma linha contendo apenas um \verb|{| que é alinhado com o início da linha acima.
\item A última linha da função contém apenas um \verb|}|, alinhado com o \verb|{| do início da função.
\item Todas as linhas entre o \verb|{| inicial e o \verb|}| final estão alinhas e mais avançadas em relação às chaves.
\end{itemize}
Esta organização do código serve para facilitar a leitura do código, uma vez que torna extremamente óbvio onde a função começa e termina. Esta técnica é chamada \emph{indentação}.

Algo que faltou nestes exemplos e que também serve ao propósito de facilitar o entendimento do código são os chamados comentários. O exemplo no Código~\ref{cod:comment} mostra como a função \verb|f| poderia ser comentada.

\begin{lstlisting}[caption={Área do retângulo, com comentários.}, label=cod:comment]
/*
 * A funcao a seguir calcula a area de um retangulo de base
 * b e altura a. Os parametros e resultado da funcao sao do
 * tipo float.
 */
float f(float a, float b)
{
	//Calcula e retorna a area do retangulo.
    return a * b;
}
\end{lstlisting}

Observe que há dois tipos de comentários no código. O primeiro começa com \verb|\*| e termina com \verb|*\| e o segundo começa com \verb|\\| e termina no final da linha. Todos os comentários servem somente ao programador e são completamente ignorados pelo computador. Os comentários podem ser poderosos aliados na hora de procurar por erros no seu código, uma vez que permitem desabilitar trechos do mesmo.

Finalmente, é muito importante nomear suas funções e parâmetros com nomes intuitivos. Seguindo esta orientação, escreveremos a última versão de nossa função.

\begin{lstlisting}[caption={Área do retângulo, com comentários e nomes intuitivos.}, label=cod:intui]
/*
 * A funcao a seguir calcula a area de um retangulo de base
 * base e altura altura. Os parametros e resultado da funcao 
 * sao do tipo float.
 */
float area_retangulo(float altura, float base)
{
    //Calcula e retorna a area do retangulo.
    return altura * base;
}
\end{lstlisting}



## {Saída de Dados}
Em computação, diz-se que um programa está executando a saída de dados quando envia para ``fora'' do programa tais dados. Exemplos comuns de saída de dados são a escrita em arquivo, o envio de mensagens na rede ou, o mais comum, a exibição de dados na tela. 

Em nossos programas, a saída de dados efetuada mais comumente será para a tela do computador. Este tipo de saída, por ser tão comum, é chamada de a saída padrão do C(++), ou simplesmente \emph{C out}. Para enviar dados para a saída do C(++), usamos a expressão \lstinline|cout <<|, seguido do dado a ser impresso na tela. Por exemplo, para imprimir a mensagem ``Olá João'', simplesmente adicionamos \lstinline|cout << "Ola Joao"| ao código. Observe que o simbolos \lstinline|<<| funciona como uma seta dizendo para onde os dados devem, neste caso, \lstinline|cout|.

É possível enviar vários tipos de dados para a saída, como veremos no decorrer do curso. No caso da tela, os dados são convertidos para sua forma textual, para que possam ser lidos pelo usuário. 
O computador realiza a conversão de acordo com o tipo original do dado: se o dado já for um texto, ele é simplesmente copiado para a tela; se for um número, ele é convertido para um conjunto de dígitos que o represente.
Por exemplo, o trecho de programa 
\begin{lstlisting}
cout << "numero ";
cout << 10;
\end{lstlisting}
gera a saída \verb|numero 10| na tela.

Observe que a palavra \lstinline|numero| no programa aparece entre aspas duplas e que o numero 10. Isto ocorre por quê \lstinline|numero| é um texto, e \lstinline|10| é um número; todos os textos devem ser colocados entre aspas duplas, para que o computador o identifique como tal, mas o mesmo não é necessário para números. Veja bem, o número \lstinline|10| é bem difernte de \lstinline|"10"| pois, por exemplo, \lstinline|10| pode ser somado a outro número (\lstinline|10 + 32|), mas \lstinline|"10"| não.

Para simplificar a saída de dados, em C(++) é possível encadear várias saídas em uma só, assim
\begin{lstlisting}
cout << "numero " << 10;
\end{lstlisting}
com o mesmo efeito do código anterior. Se houver necessidade de se iniciar nova linha na ``impressão'' na tela, basta enviar \lstinline|endl| (contração de \emph{end line}) para a saída. Assim, o código 
\begin{lstlisting}
cout << "numero " << 10 << endl << "texto " << endl;
\end{lstlisting}
imprime na tela o texto
\begin{verbatim}
numero 10
texto

\end{verbatim}

Finalmente, quando uma ``chamada'' a uma função é enviada para o \lstinline|cout|, o que é impresso é o resultado da função. Assim, 
\begin{lstlisting}
cout << "sen(1)" << endl << sen(1);
\end{lstlisting}
imprime na tela o texto
\begin{verbatim}
sen(1)
0
\end{verbatim}
Você verá vários exemplos de usos do \lstinline|cout| na próxima seção.



## {A Função \texttt{main}}
Que o computador é uma máquina burra e executa somente o que você manda você já deve ter entendido, mas como mandá-lo executar algo? Em linguagem C(++), o computador \emph{sempre} começa a execução de um código pela função \verb|main|, a função principal. Sendo assim, se você quer dizer ao computador que calcule a área de um retângulo, então esta ordem dever partir, de alguma forma, da função \verb|main|. 

Para um exemplo,veja o seguinte código.

\begin{lstlisting}
#include <iostream>

using namespace std;

/*
 * A funcao a seguir calcula a area de um retangulo de base
 * base e altura altura. Os parametros e resultado da funcao 
 * sao do tipo float.
 */
float area_retangulo(float altura, float base)
{
    //Calcula e retorna a area do retangulo.
    return altura * base;
}

int main()
{
    //Calculemos a area de alguns retangulos.
    cout << area_retangulo(3.3, 2.0) << endl;
    cout << area_retangulo(2.0, 2.0) << endl;	
	
    //Lembre-se, todo numero inteiro tambem e um numero real.
    cout << area_retangulo(4, 2) << endl;		

    return 0;
}
\end{lstlisting}

Algumas observações importantes sobre a função \verb|main|:
\begin{enumerate}
\item A função \verb|main| tem sempre um resultado do tipo inteiro e seu resultado é sempre 0 (\verb|return 0;|)\footnote{Na verdade, nem nem sempre é 0, mas por enquanto definiremos sempre assim.}

\item Função \verb|main| é como um \emph{highlander}: só pode haver uma! Isto é, cada programa só pode conter a definição de uma função com este nome. Aliás, a regra vale para toda e qualquer função; se não fosse assim, o computador não saberia a qual função você está se referindo em seu código.

\item Finalmente, a função \verb|area_retangulo| aparece antes da fução \verb|main| no programa. Isto deve ser verdade para todas as funções do seu programa. Isto ocorre por quê, antes de executar a função \verb|main|, o computador precisa aprender sobre a existência das outras funções.
\end{enumerate}

O código como está, includindo as duas linhas iniciais que ainda não sabem para que servem, ``pronto'' para ser executado no seu computador. No próximo capítulo veremos exatamente como fazer isso. Até lá, executemos o código ``na mão'':
\begin{itemize}
\item O programa começa a executar pela função \lstinline|main|; somente o que está no corpo desta função é executado.
\item Na linha 18 não há o que executar, pois é só um comentário. 
\item Na linha 19, como vimos no Código~\ref{cod:ola}, está se dizendo para o computador escrever algo na tela. Este algo é o resultado da aplicação da função \lstinline|area_retangulo| aos parâmetros 3.3 e 2.0.\footnote{Observe o uso de ``.'' como separador de casas decimais.}. Para que se conheça este resultado, o programa executa a função \lstinline|area_retangulo|.
\item A linha 13 calcula a área do retângulo, que é então retornado para a linha 19.
\item Na linha 19, a \emph{chamada} da função é ``substituída'' pelo resultado, e o número 6.6 é escrito na tela do computador. Na sequência, é escrito também \lstinline|endl|, que faz com que o computador salte para a próxima linha da tela do computador.
\item Na linha 20 o procedimento todo é repetido, agora escrevendo o valor 4.0 na tela.
\item Na linha 23 também se repete o procedimento, mas agora passando como parâmetro para a função os valores inteiros 4 e 2. Como todo número inteiro também é um número real, a função é novamente executada e o valor 8.0 é impresso na tela.
\end{itemize}

## {Conclusão}
Os códigos apresentados neste capítulo, apesar de simples, ilustraram vários pontos importantes da programação de computadores em geral e da linguagem C em específico. Estes pontos podem ser sumarizados assim:
\begin{itemize}
\item Em C(++) pode-se definir funções que executem computações bem definidas e específicas. 
\item C(++) tem vários \emph{tipos} de dados, como \verb|int| (números inteiros) e \verb|float| (números reais).
\item É importante manter o código organizado, comentado e indentado. Isso facilita seu entendimento e manutenção.
\end{itemize}

## {Exercícios}
\begin{exercicio}
Escreva um função que calcule a área de um círculo. Observe que a linguagem C é baseada na língua inglesa, na qual se separa casas decimais por \verb|.| e não por \verb|,|. Logo, $\Pi$ é igual 3.14 e não 3,14.
\end{exercicio}


\begin{exercicio}
Escreva uma função que calcule a área de um triângulo.
\end{exercicio}
















\chapter{Compilação e Execução}
Para colocarmos nossos algoritmos em execução, o primeiro passo é escrevê-los, usando um editor de textos qualquer que salve arquivos em texto puro, como o notepad, vim, gedit, etc. A este arquivo com o \emph{código} chamaremos \emph{código fonte} ou simplesmente \emph{fonte}. Uma vez de posse do fonte, é preciso submetê-lo a um processos com vários passos que gera, ao final, um arquivo executável ou o que chamamos, comumente, de \emph{programa}. O processo como um todo, descrito na seção seguinte, é conhecido como \emph{compilação}, apesar de compilação ser apenas um dos passos do processo.

## {O processo de compilação}
A sequência de passos que compõem a compilação é a seguinte:

Código Fonte $\rightarrow$ Pré-processador $\rightarrow$ Fonte Expandido $\rightarrow$ Compilador $\rightarrow$ Arquivo Objeto $\rightarrow$ Ligador $\rightarrow$ Executável

De forma simplificada, a pré-compilação é um passo que modifica o código fonte substituindo certas ``palavras chave'' encontradas ao longo do texto por suas definições. Por exemplo, pode-se definir que, no programa, toda vez que o pré-processador encontrar a palavra PI, ele a substituirá por 3.141649. A utilidade da pré-compilação ficará mais clara mais adiante no curso.

Uma vez terminada a pré-compilação, acontece a compilação do seu programa. A compilação traduz o código que você escreveu para uma linguagem inteligível ao computador, salvando-o em um arquivo chamado arquivo objeto. Por exemplo, a compilação transformaria o código ``Olá Mundo!'' escrito acima em algo como %http://farid.hajji.name/blog/2009/12/26/hello-world-in-freebsd-assembler/
\begin{verbatim}
...
CALL  write(0x1,0x400623,0xe)
GIO   fd 1 "Olá Mundo!"
RET
 ...
\end{verbatim}

Após a compilação vem a \emph{linkedição}, o passo que junta o seu arquivo objeto a outros arquivos objetos interessantes, como por exemplo um que contenha código de funções matemáticas, manipulação de arquivos, ou interação gráfica com o usuário.\footnote{Embora a explicação dada aqui não seja estritamente correta, ela é próxima o suficiente da realidade para o escopo deste curso.}

## {A IDE Code::Blocks}
Embora a edição de um programa possa ser feita em praticamente qualquer editor de textos, há certos editores que são mais adequados a esta tarefa. Tais editores fazem, dentre outras, a colorização das palavras de seu código de forma a ajudá-lo a detectar erros e tentam alinhar automaticamente as linhas do seu código. A intenção destes editores é aumenentar sua produtividade como programador. Outros editores vão ainda mais longe e lhe permitem fazer todo o processo de compilação com um simples \emph{click} do mouse ou apertar de uma tecla. Estes editores mais completos são conhecidos como \emph{Integrated Development Environment}, ou simplesmente IDE.

No decorrer deste curso consideraremos que o aluno estará usando a IDE \href{http://www.Code::Blocks.org}{Code::Blocks}, que é gratuita e com versões para Windows, Linux e OSX. Entretanto, qualquer outra IDE ou mesmo a compilação manual podem ser usados em substituição ao Code::Blocks.

### {Criando um Projeto}
Para começar a programar no Code::Blocks, precisamos criar um \emph{projeto}. Este projeto conterá seu código fonte e, no caso de uma programação mais avançada, arquivos de imagens, definições de personalização do processo de compilação, etc. Para criar um projeto no Code::Blocks, clique em \textbf{File} e, em seguida, \textbf{New}, \textbf{Project}.

Na tela que se apresenta, você deve escolher o tipo de projeto a ser criado. Não se perca nos tipos; escolha \textbf{Console Application} e então clique em \textbf{Go}.

\begin{center}
\includegraphics[width=.7\textwidth]{imagens/2-1.PNG}
\end{center}

Na tela seguinte você deverá escolher a linguagem de programação usada; escolha C++ e clique em \textbf{Next} para passar para a tela onde deverá nomear o seu projeto. Em \textbf{project title} escreva algo como teste1; em \textbf{folder to create the project in}, clique no botao com \ldots e escolha uma pasta para salvar o projeto; esta pode ser, por exemplo, a pasta \textbf{Meus Documentos} ou uma pasta qualquer em um \emph{pen drive}.\footnote{O importante aqui é salvar o arquivo em um lugar em que você possa voltar mais tarde para reler.}. Clique então \textbf{Next} e, na tela seguinte, clique em \textbf{Finish}.

\begin{center}
\includegraphics[width=.7\textwidth]{imagens/2-2.PNG}
\end{center}

Pronto, seu projeto foi criado. Agora abra o arquivo \textbf{main.cpp}, que está na pasta \textbf{sources}, dando um clique duplo no nome do arquivo. Observe que o Code::Blocks criou automaticamente um programa básico.

\begin{center}
\includegraphics[width=.7\textwidth]{imagens/2-3.PNG}
\end{center}

Finalmente, clique  em \textbf{build} e então em \textbf{build and run}. Parabéns, você acaba de executar seu primeiro programa.

### {Depuração}
Todo programa de tamanho considerável, e mesmo aqueles de tamanho diminuto, possuirão, ao menos em suas versões iniciais, erros. Por razões históricas, nos referimos a estes erros por \emph{bugs}\todo{Referência para o uso de bug}. Uma das formas de achar os bugs do seu programa é fazer com que o computador execute seu programa passo a passo, isto é, linha a linha, e acompanhar esta execução verificando se o programa faz o que você espera.

Para experimentarmos a depuração, processo pelo qual removemos bugs, modifique a mensagem "Hello world!" do seu programa para "Olá <seu nome>!" e execute novamente o programa (\textbf{build and run}). Se o programa executou normalmente, você está no caminho certo. Agora, copie toda a linha contendo a mensagem e cole-a várias vezes, substituindo o nome em cada linha. Seu programa deve ficar como no Código~\ref{cod:olas}

\begin{lstlisting}[label=cod:olas, caption={Programa com vários Hello's.}]
#include <iostream>

using namespace std;

int main()
{
    cout << "Hello Joao!" << endl;
    cout << "Hello Jose!" << endl;
    cout << "Hello Joaquim!" << endl;
    cout << "Hello Joselino!" << endl;
    cout << "Hello Asdrubal!" << endl;
    return 0;
}
\end{lstlisting}

Mais uma vez, compile e execute seu programa. Se a execução foi bem sucedida, você está pronto para a depuração. Para depurar, clique ao lado direito do número 7 (sétima linha do programa), até que uma bolinha vermelha apareça, como na figura a seguir. A bolinha vermelha é, na verdade, um sinal de pare, e diz ao computador que deve, ao executar seu programa, parar ali.

\begin{center}
\includegraphics[width=.7\textwidth]{imagens/2-4.PNG}
\end{center}

Se você for adiante e executar o programa como fizemos até agora, verá que o pare não funcionou. Isto é por que o sinal é ignorado a não ser que você inicie a execução em modo de depuração. Para fazer isso, clique no menu \textbf{Debug} e então em \textbf{Start} ou, alternativamente, pressione a tecla F8. Observe que a execução parou onde você esperava. Agora, clique em \textbf{Debug} e \textbf{Next Line} ou aperte F7, no teclado, sucessivamente para ver o que acontece. Observe que cada linha é executada e então a execução pára novamente.


## {O Arquivo Executável}
Agora que você já escreveu programas super interessantes, os compilou e executou, imagine como faria para enviar tais programas a um amigo que não tenha qualquer interesse ou aptidão em programação. A solução é simples: mandaremos a este amigo o arquivo executável do programa. Para fazê-lo, abra a pasta na qual salvou seu projeto Code::Blocks. Nesta pasta você encontrará um arquivo com extensão \verb|.exe|; este é o arquivo executável que deveria enviar para seu amigo. Quando seu amigo executar este programa, verá exatamente a mesma coisa que você viu quando o fez. Além de ser muito útil, este procedimento é também uma ótima forma de se compartilhar vírus de computador.

## {Exercícios}
\begin{exercicio}
Escreva o programa completo que calcula a área de vários retângulos do capítulo anterior e execute-o.
\end{exercicio}

\begin{exercicio}
Altere seu programa para usar, além da função de cálculo de área de um quadrado, as funções definidas nos exercícios do capítulo anterior.
\end{exercicio}























\chapter{Variáveis, Entrada / Saída e Operadores}

A todo momento precisamos representar informação do mundo a nossa volta em nossos programas. Essas informações, tais como nome, número de matrícula, nota final, temperatura, idade e outras tantas são armazenadas em entidades chamadas variáveis.

Uma variável nada mais é do que um pedaço de memória, no qual se pode ler ou escrever alguma informação. A estes pedaços de memória podemos dar nomes que nos ajude a lembrar o que exatamente está escrito ali. Por exemplo, se uma variável guarda a idade de alguém, um bom nome seria ``idade'', enquanto que ``rataplam'' ou ``var13'' provavelmente serão péssimas escolhas.

As alterações em uma variável resultam da interação com o usuário, isto é, quando o usuário informa valores para as mesmas em uma operação de leitura, ou da avaliação de expressões lógico-aritméticas (o tipo de cálculo nos quais o computador é especializado).

Neste capítulo veremos como criar nossas primeiras variáveis e como alterar seus valores por meio da leitura direta do teclado e da utilização de operadores.


## {Declaração de Variáveis}
Na linguagem C, toda variável deve ser declarada (isto é, criada) no início do corpo da função que a contem. A declaração de uma variável tem pelo menos duas partes:
\begin{description}
\item[Nome:] usado para referenciar a variável quando se precisa ler ou escrever a mesma;

\item[Tipo:] para que o computador saiba como tratar a informação, ele precisa saber de que tipo ela é, ou seja, se é um número, ou uma palavra, ou uma caractere, etc; e,
\end{description}

Algumas regras simples devem ser seguinda na hora de se nomear uma variável:
\begin{itemize}
\item o nome só pode conter os caracteres [a-z], [A-Z], [0-9] e o ``\_''; e,
\item o nome não pode começar com números.
\end{itemize}

Quanto aos tipos usaremos, por enquanto, os seguintes:
\begin{description}
\item[int] representando um número inteiro, como por exemplo 3, 4 e -78;

\item[float:] representando um número real, com casas decimais separadas por \emph{ponto}, como por exemplo 3.1416 e -1.2; e
\item[char:] representando um caractere (letra, dígito, sinal de pontuação) como por exemplo 5, a, Z, ., e -.
\end{description}

São exemplos de declarações de variáveis válidas:
\begin{lstlisting}
int nota1, nota2;
float media;
char _caractere;
\end{lstlisting}

São exemplos de declarações inválidas:
\begin{lstlisting}
int 1nota, 2nota;
float #media;
char nome completo;
\end{lstlisting}

### {Atribuição e Uso}
Como já dito, uma variável é um pedaço da memória do computador no qual se pode ``escrever'' e ``ler'' dados.
Em vez de ``escrever'', contudo, no mundo da computação usamos a expressão \emph{atribuir um valor a uma variável} para significar a mudança do valor da variável. Esta operação é executada pelo operador de atribuição \verb|=|. Por exemplo, o seguinte código declara três variáveis numéricas, duas inteiras e uma real, e, em seguida, lhes atribui os valores \verb|0|, \verb|10| e \verb|10.0|.
\begin{lstlisting}
int inteiro1, inteiro2;
float real;

inteiro1 = 0;
inteiro2 = 10;
real = 10.0;
\end{lstlisting}

A memória do computador sempre tem algum dado, tenha ele sido colocado por você ou não, seja ele relevante ou não. Logo, para se usar o conteúdo de uma variável, é necessário ter certeza de que a mesma contém um valor que faça sentido. Isto é, algo que tenha sido atribuído pelo seu programa àquela variável, via uma operação de leitura, via uma computação qualquer, ou via uma atribuição como a do exemplo anterior.

Denominamos a primeira atribuição de um valor a uma variável de \emph{iniciação} (ou \emph{inicialização}). E já que qualquer variável só deve ser usada se tiver sido iniciada, o C(++) permite que as variáveis sejam iniciadas já em sua declaração. Por exemplo, o código abaixo faz exatamente o que fazia o exemplo anterior, mas de forma mais compacta.

\begin{lstlisting}
int inteiro1 = 0, 
    inteiro2 = 10;
float real = 10.0;
\end{lstlisting}

Observe que se pode iniciar várias variáveis do mesmo tipo, declaradas na mesma linha, com valores distintos. Neste caso, note  quebra de linha entre as declarações de \verb|inteiro1| e \verb|inteiro2|; ela é somente estética, mas ajuda a separar a declaração e iniciação das várias variáveis.

Agora que você viu como declarar e iniciar uma variável vem a parte fácil: usá-la. Veja como no seguinte exemplo.
\begin{lstlisting}[label={Programa com exemplo de uso de variáveis.}, caption=cod:vars]
#include <iostream>

using namespace std;

float area_circulo(float raio)
{
  float PI = 3.14, 
        area;
  area = PI * raio * raio;
  return area;
}

char proxima_letra(char c1)
{
  char c2;
  c2 = c1 + 1;
  return c2;
}

int main() {
  int r1;
  float r2;
  char _c;
  _c = 'a';
  cout << "O proximo de " << _c << " eh " << proxima_letra(_c) << endl;
  r1 = 2;
  r2 = 9.7;
  cout << "r = " << r1 << ", area = " << area_circulo(r1) << endl;
  cout << "r = " << r2 << ", area = " << area_circulo(r2) << endl;
  r1 = 12;
  r2 = 0.4;
  cout << "r = " << r1 << ", area = " << area_circulo(r1) << endl;
  cout << "r = " << r2 << ", area = " << area_circulo(r2) << endl;
  return 0;
}
\end{lstlisting}
É simples assim: para se usar uma variável, basta colocar seu nome na expressão a ser computada. Na linha 9, por exemplo, atribui-se à variável \lstinline|area|  o valor da multiplicação do conteúdo da variável \lstinline|PI| por \lstinline|raio|, ao quadrado. Na linha 10, o resultado da função é o conteúdo da variável \lstinline|area|.

### {Parâmetros são Variáveis}
Nos exemplos de programas dos capítulos anteriores, você viu como o conteúdo de uma parâmetro é definido e usado. Por exemplo, os  dois parâmetros da função \verb|area_retangulo|, reproduzida abaixo, são declarados dizendo-se de que tipo eles são e quais são seus nomes. Em seguida, no corpo da função, os parâmetros são usados no cálculo da área simplesmente multiplicando-se ``o nome de um pelo nome do outro''; os valores dos parâmetros são aqueles passados na chamada da função. 

\begin{lstlisting}
float area_retangulo(float altura, float base)
{
    //Calcula e retorna a area do retangulo.
    return altura * base;
}

int main()
{
    float area;
    area = area_retangulo(2.0, 2.0);
    cout << area;
    
    return 0;
}
\end{lstlisting}

Esta semelhança com a declaração e uso de variáveis não é coincidental: parâmetros não são mais do que variáveis declaradas e iniciadas de uma forma especial. Isto é, elas declaradas na definição da função e são iniciadas atribuindo-se os valores passados na invocação da função, na mesma órdem em que são passados. Isto é, se a função é invocada como \lstinline|area_retangulo(1,2)|, então 1 é atribuído à variável/parâmetro \lstinline|altura| e 2 à \lstinline|base|. Se a função é invocada como \lstinline|area_retangulo(X,y)|, então o valor da variável X, seja lá qual for é atribuído à variável/parâmetro \lstinline|altura| e de y à \lstinline|base|.



## {Entrada / Saída}
Além da escrita ou impressão de dados na tela, vista no Capítulo\ref{cap:introducao}, uma das tarefas mais comuns em programação é a leitura de valores informados pelo usuário. A seguir veremos o comando que nos permitem executar tal tarefas.

### {Leitura}
De forma semelhante ao \verb|cout|, há um comando para leitura denominado \verb|cin|. Este comando permite ler valores digitados pelo usuário atualizando a(s) variável(is) passada(s) para o \verb|cin| por meio do conector \verb|>>|.

A seguir temos um exemplo de entrada de dados:
\begin{lstlisting}
char letra;
int idade;

cout << "Informe a letra inicial de seu nome e sua idade: ";
// a seguir eh feita a leitura
cin >> letra >> idade;
cout << "A letra eh " << letra;
cout << " e sua idade eh " << idade << endl;
\end{lstlisting}

### {Impressão}
Complementando o que já vimos sobre o \verb|cout|, vejamos como escrever o conteúdo de variáveis na tela:
\begin{itemize}
\item Variáveis e chamadas de funções aparecem diretamente também, e seus valores (e resultado) é que são colocados na saída.
\end{itemize}
A seguir, podemos ver alguns exemplos:
\begin{lstlisting}
char letra = 'a';
int num = 2;
cout << "letra = " << letra << endl << "num = " << num << endl;
\end{lstlisting}
que gera a seguinte saída:
\begin{lstlisting}
letra = a
num = 2
\end{lstlisting}



Agora que você consegue ler do teclado e escrever para a tela, veja como é fácil fazer um programa que calcule a área de retângulo cujos lados são digitados pelo usuário.
\begin{lstlisting}
float area_retangulo(float altura, float base)
{
    //Calcula e retorna a area do retangulo.
    return altura * base;
}

int main()
{
    float area,
          b,
          a;
    cout << "Qual a altura do retangulo?" << endl;
    cin >> a;
    
    cout << "Qual a base do retangulo?" << endl;
    cin >> b;
            
    area = area_retangulo(b, a);
    cout << area;
    
    return 0;
}
\end{lstlisting}

\subsubsection{Formatação de Impressão}

Em algumas ocasiões há necessidade de formatar a saída para, por exemplo, garantir que os dados
fiquem alinhados, imprimir uma tabela, ou simplesmente por estética. A seguir veremos algumas
maneiras de formatar, texto, números inteiros e reais. Para formatação de texto e números deve-se
incluir a biblioteca \lstinline|iomanip|.

A formatação de texto é obtida mediante definição da largura do conteúdo impresso e do alinhamento. O
comando \lstinline{setw(<valor>)}, define a largura do texto impresso para o valor informado como
argumento, enquanto os comandos \lstinline{right} e \lstinline{left} definem o alinhamento para a
direita e esquerda, respectivamente. O efeito do comando \lstinline|setw| não é permamente.
O código a seguir ilustra a utilização destes comandos:
\begin{lstlisting}
#include <iostream>
#include <iomanip>

using namespace std;

float volume_cubo(float aresta)
{
    return aresta*aresta*aresta;
}

int main()
{
    float a, v;
    cout << "Entre valor da aresta do cubo:" << endl;
    cin >> a;
    v = volume_cubo(a);
    cout <<  setw(30) << left << "O volume do cubo eh: " << v << endl;
    cout << setfill('-');
    cout <<  setw(30) << left << "O volume do cubo eh: " << v << endl;
    cout <<  setw(30) << "O volume do cubo eh: " << setw(20) << v << endl;
    cout <<  setw(30) << "O volume do cubo eh: " << setw(20) << right << v << endl;
    cout <<  setw(30) << left << "O volume do cubo eh: " << v << endl;
    return 0;
}
\end{lstlisting}
A execução deste código produz a seguinte saída:
\begin{verbatim}
Entre valor da aresta do cubo:
2.5
O volume do cubo eh:          15.625
O volume do cubo eh: ---------15.625
O volume do cubo eh: ---------15.625--------------
O volume do cubo eh: -----------------------15.625
O volume do cubo eh: ---------15.625
\end{verbatim}
O comando \lstinline|setfill| permite definir o caractere que será usado para preencher os espaços
restantes, de acordo com a largura definida com \lstinline|setw|

Para formatação de números reais (\lstinline{float} e \lstinline{double}), o exemplo a seguir mostra
alguns comandos para formatação:

\begin{lstlisting}
#include <iostream>
#include <iomanip>

using namespace std;

float volume_cubo(float aresta)
{
    return aresta*aresta*aresta;
}

int main()
{
    float a, v;
    cout << "Entre valor da aresta do cubo:" << endl;
    cin >> a;
    v = volume_cubo(a);
    cout <<  "O volume do cubo eh: " << v << endl;
    cout << fixed << setprecision(2);
    cout <<  "O volume do cubo eh: " << v << endl;
    cout << fixed << setprecision(4);
    cout <<  "O volume do cubo eh: " << v << endl;
    return 0;
}
\end{lstlisting}

O comando \lstinline{fixed} determina que o número de casas depois decimais será fixo, enquanto o
comando \lstinline{setprecision} define quantas casas decimais serão impressas. Desta maneira, para
o exemplo anterior, teremos a seguinte saída:

\begin{verbatim}
Entre valor da aresta do cubo:
4
O volume do cubo eh: 64
O volume do cubo eh: 64.00
O volume do cubo eh: 64.0000 
\end{verbatim}


## {Operadores}

Os operadores são os mecanismos por meio dos quais os computadores realizam os cálculos aritméticos e lógicos, atualizando valores das variáveis e executando as tarefas a que se destinam.

Os operadores matemáticos são os mais utilizados na maioria dos programas que serão desenvolvidos. Os principais operadores aritméticos são: $+, -, *, /$ e o \%, indicando, respectivamente, as operações de soma, subtração, multiplicação, divisão e resto da divisão.

Considere o exemplo a seguir:
\begin{lstlisting}
#include<iostream>

using namespace std;

int main()
{
  int n, dobro_de_n;
  cout << "Entre um inteiro: ";
  cin >> n;
  dobro_de_n = 2*n;
  cout << "O dobro de " << n << " eh " << dobro_de_n << endl;
  return 0;
}
\end{lstlisting}

## {Exercícios}

\begin{exercicio}
Escreva uma função em C que, dado uma temperatura em graus Célsius (do tipo float), retorne a temperatura equivalente em Farenheit. 
Escreva também a função \verb|main|  que leia a temperatura em Célsius do teclado, invoque a função de conversão, e imprima o resultado.

Dado: $F = \frac{9C}{5} + 32$
\end{exercicio}





%\todo{Esta seção deve ser movida para mais adiante, para quando formos falar em números binários, e incrementada.}

\chapter{Variáveis (II)}
## {Escopo de Variáveis}
No capítulo anterior estudamos como declarar e utilizar variáveis em nossos programas. Fizemos, por exemplo, um programa como o seguinte, que pede ao usuário que entre com as medidas da base e altura de um retângulo e então imprime na tela do computador a área deste retângulo.

\begin{lstlisting}
float area_retangulo(float altura, float base)
{
    //Calcula e retorna a area do retangulo.
    return altura * base;
}

int main()
{
    float area,
          b,
          a;
    cout << "Qual a altura do retangulo?" << endl;
    cin >> a;
    
    cout << "Qual a base do retangulo?" << endl;
    cin >> b;
            
    area = area_retangulo(b, a);
    cout << "A area do retangulo de base " << b << " e altura " 
          << a << " eh " << area << endl;
    
    return 0;
}
\end{lstlisting}

O que aconteceria se em vez de chamarmos as variáveis na função \verb|main|  de \verb|a|  e \verb|b| as tivéssemos chamado de \verb|base| e \verb|altura|? Veja que estes são exatamente os nomes dos parâmetros da função \verb|area_retangulo|. Melhor ainda, e se a função tivesse alterado os valores dos parâmetros? 

Para descobrir as respostas a estas perguntas, faça o seguinte experimento:
\begin{itemize}
\item digite o programa tal qual acima em seu computador e \emph{execute-o}.

\item modifique somente a função \verb|main| do seu programa para que fique assim
\begin{lstlisting}
int main()
{
    float area,
          base,
          altura;
    cout << "Qual a altura do retangulo?" << endl;
    cin >> altura;
    
    cout << "Qual a base do retangulo?" << endl;
    cin >> base;
            
    area = area_retangulo(base, altura);
    cout << "A area do retangulo de base " << base << " e altura " 
         << altura << " eh " << area << endl;
    
    return 0;
}
\end{lstlisting}
e execute-o.
\item Note quais as diferenças na execução.
\item Finalmente, altere a função \verb|area_retangulo| para que fique assim
\begin{lstlisting}
float area_retangulo(float altura, float base)
{
    //Calcula e retorna a area do retangulo.
    altura *= base;
    return altura;
}

\end{lstlisting}
e execute novamente o programa.
\item Note se houve alguma alteração do valor da variável \verb|altura|.
\end{itemize}

Como se pôde notar, estas mudanças não afetaram a execução do programa. Isto acontece por quê as variáveis tem escopos bem definidos em C. A variável \verb|altura| da função \verb|main| não é a mesma variável/parâmetro \verb|altura| da função \verb|area_retangulo|; cada uma só existe dentro do corpo da função em que foi declarada. Quando a função \verb|area_retangulo| é invocada passando-se como parâmetro a variável \verb|altura| da função \verb|main|, o valor desta variável é \emph{copiado} para o parâmetro \verb|altura| da função invocada. Sendo assim, quaisquer alterações ao valor do parâmetro dentro da função afetam apenas a cópia, não o valor da variável de onde foi copiado.

A variáveis definidas até agora possuem o que chamamos \emph{escopo local}. Isto é, elas são visiveis somente localmente à função em que foram definidas. Outro tipo de escopo presente possível em C é o \emph{escopo global}. Uma variável tem escopo global se for definida fora de qualquer função. Uma variáel com escopo global poderá ser acessada de (quase) qualquer parte do seu código. Para um exemplo de variável de escopo global, veja o código a seguir. 

\begin{lstlisting}
float PI = 3.1416;

float resposta = 0;

float area_retangulo(float altura, float base)
{
    //Calcula e retorna a area do retangulo.
    resposta = base * altura;
    return resposta;
}

float area_circulo(float raio)
{
    //Calcula e retorna a area do circulo.
    resposta = PI * raio * raio; 
    return resposta;
}

int main()
{
    float area,
          base,
          altura,
          raio;
    
    cout << "Qual a altura do retangulo?" << endl;
    cin >> altura;
    
    cout << "Qual a base do retangulo?" << endl;
    cin >> base;
            
    area = area_retangulo(base, altura);
    cout << "A area do retangulo de base " << base << " e altura " 
          << altura << " eh " << area << endl;
    
    cout << "Resposta da chamada de funcao " << resposta << endl; 

    cout << "Qual o raio do circulo?" << endl;
    cin >> raio;

    area = area_circlo(raio);
    cout << "A area do circulo de raio " << raio 
    << " e PI arredondado para " << PI <<" eh " << area << endl;
     
    cout << "Resposta da chamada de funcao " << resposta << endl; 
    return 0;
}
\end{lstlisting}

Observe a variável \verb|PI|. Esta variável foi declarada fora de qualquer função e, sendo assim, é visível em qualquer delas, como demonstrado pelo seu uso na função \verb|main| e \verb|area_circulo|.

Observe também que a mesma variável \verb|area| foi utilizada mais de uma vez. Isto é comum em programação pois, com a quantidade limitada de recursos, pode não fazer sentido criar uma variável para cada novo uso. Observe que a variável \verb|resposta| foi alterada dentro das duas funções de cálculo de área e que estas mudanças foram visíveis à função \verb|main|.

Verifique de forma experimental (copiando e executando) que o programa acima funciona como esperado.

## {Faixas de Valores}
Você já aprendeu que variáveis são espaços (células) da memória do computador para o qual damos nomes. Estes espaços, por serem limitados, podem armazenar uma quantidade limitada de valores. Pense, por exemplo, em quais os números, positivos e negativos, se pode representar com três dígitos: $-99, -98, \ldots, 0, 1, 2, \ldots, 998,999$.

Tentemos descobrir qual a faixa de valores que ``cabem'' em uma variável \verb|int|. Escreva um programa que declare uma variável do tipo \verb|int|, inicie esta variável com um número (digamos, 10000), e imprima este número na tela do computador. Veja que o número é impresso na tela como deveria: \verb|10000|. 

Agora altere seu programa para que imprima 20000 e execute-o. Refaça este passo (adicionando 10000 a cada passo) até que a impressão fuja do que você esperava. Neste ponto, trabalhe com incrementos menores até determinar qual o maior número que é impresso como esperado. Fepita o processo para identificar qual o menor número que cabe em um \verb|int|. Quais são estes valores?

Finalmente, tente identificar a faixa de valores que cabem em um \verb|float|. Dica: os incrementos iniciais deveriam ser na faixa de milhões e não dezenas de milhares.


## {Exercícios}
\todo{Colocar}

## {Laboratório}
\todo{Colocar}


\chapter{Seleção Simples}
Nossos programas até agora foram extremamente simples, contendo apenas algumas pequenas funções além da \verb|main|. Isto acontece em parte por quê nossos programas são apenas sequências diretas de comandos, sem execução condicional. Isto é, até agora não aprendemos a dizer para o computador ``Se for assim, então faça assado! Senão, faça cozido!''. Esta deficiência será corrigida neste capítulo.

Como exemplo de programação mais interessante, implementemos uma função que calcule as raizes de uma equação de segundo grau. Para fazê-lo, relembremos a fórmula de Bhaskara:

$x = \frac{-b \pm \sqrt{\Delta}}{2a}$, sendo $\Delta = b^2 -4ac$.

Comecemos então definindo uma função para o cálculo do $\Delta$.

\begin{lstlisting}
float delta(float a, float b, float c)
{
    return b*b - 4*a*c;
}
\end{lstlisting}

Para testar o cálculo do $\Delta$ precisamos da função \verb|main|, juntamente com o restante do esqueleto de programa aprendido até agora.

\begin{lstlisting}
#include <iostream>

using namespace std;

float delta(float a, float b, float c)
{
    return b*b - 4*a*c;
}

int main()
{
    float a, b, c;

    cout << "Equacao do segundo grau: axx + bx + c = 0" << endl;
    cout << "Digite o valor de a: ";
    cin >> a;
    cout << "Digite o valor de b: ";
    cin >> b;
    cout << "Digite o valor de c: ";
    cin >> c;

    cout << "Delta: " << delta(a,b,c) << endl;
    return 0;
}
\end{lstlisting}

Agora, para cálculo das raízes! Comecemos por alterar o programa para imprimir \emph{o número} de raízes da equação. O cálculo do número de raízes será feito na função \verb|raizes|. A equação tem ou 0 raízes reais (se o $\Delta < 0$), ou duas raízes iguais (se $\Delta = 0$), ou duas raizes distintas (se $\Delta > 0$).

\begin{lstlisting}
#include <iostream>

using namespace std;

float delta(float a, float b, float c)
{
    return b*b - 4*a*c;
}

int raizes(float a, float b, float c)
{
    float d = delta(a,b,c);
    int qtd;

    se d menor que 0
    {
        qtd = 0;
    }
    senao e se d igual a 0
    {
        qtd = 1;
    }
    senao
    {
        qtd = 2;
    }

    return qtd;
}


int main()
{
    float a, b, c;

    cout << "Equacao do segundo grau: axx + bx + c = 0" << endl;
    cout << "Digite o valor de a: ";
    cin >> a;
    cout << "Digite o valor de b: ";
    cin >> b;
    cout << "Digite o valor de c: ";
    cin >> c;

    cout << "Delta: " << delta(a,b,c) << endl;
    cout << "A equacao tem " << raizes(a,b,c) << " raizes.";
    return 0;
}
\end{lstlisting}

Acontece que o computador não entende nem o \verb|se| e nem o \verb|menor que|. Mas então como faremos as verificações necessárias para determinar a quantidade raizes? A resposta tem duas partes.

## {Operadores Relacionais}
As linguagens de programação provêem sempre formas de se comparar dados. Em C(++) os operadores relacionais, usados para comparar, são os seguintes:

\begin{tabular}{c l}
\verb|==| & igual a\\
\verb|!=| &	diferente de\\
\verb|>| &	maior que\\
\verb|<| &	menor que\\
\verb|>=| &	maior ou igual a\\
\verb|<=| &	menor ou igual a\\
\end{tabular}

Observe que o primeiro operador tem \emph{dois} sinais de igual. Isto é para diferenciar este operador do operador de atribuição \verb|=|, visto anteriormente. O segundo operador tem um sinal de exclamação (\verb|!|) que, em linguagem C, significa \emph{negação}. Logo, \verb|!=| significa não igual ou, simplesmente, diferente. Os demais operadores devem ter significados óbvios.

Usando estes operadores, podemos re-escrever a função raizes do nosso programa assim: 

\begin{lstlisting}
int raizes(float a, float b, float c)
{
    float d = delta(a,b,c);
    int qtd;

    se d < 0
    {
        qtd = 0;
    }
    senao e se d == 0
    {
        qtd = 1;
    }
    senao
    {
        qtd = 2;
    }

    return qtd;
}
\end{lstlisting}

Melhorou, mas ainda não pode ser executado pelo computador. Vamos então ao \emph{se}.

## {\texttt{if-else}}
Em C, testes simples (tudo o que você realmente precisa) podem ser feitos com a estrutura \verb|if|, que tem uma das seguintes sintaxes:

\begin{itemize}
\item \verb|if(| expressão lógica \verb|)| bloco de comandos 1

\item \verb|if(| expressão lógica \verb|)| bloco de comandos 1 \verb|else| bloco de comandos 2
\end{itemize}

Uma \emph{expressão lógica} é uma expressão cuja avaliação resulte em \emph{verdadeiro} ou \emph{falso} como, por exemplo, as expressões que usam os operadores relacionais apenas apresentados.

Um \emph{bloco de comandos} é ou uma instrução ou um conjunto de instruções dentro de \verb|{| \verb|}|.

Quando a expressão lógica é avaliada, se seu resultado for \emph{verdadeiro}, então o bloco de comandos 1 será executado. Se o resultado for \emph{falso}, o bloco de comandos 1 não será executado e o bloco 2, se existir, será executado em seu lugar.

Observe que o segundo bloco pode ser, por sua vez, outro \verb|if|. Por exemplo, nosso programa pode ser reescrito assim:

\begin{lstlisting}
#include <iostream>

using namespace std;

float delta(float a, float b, float c)
{
    return b*b - 4*a*c;
}

int raizes(float a, float b, float c)
{
    float d = delta(a,b,c);
    int qtd;

    if(d < 0)
    {
        qtd = 0;
    }
    else if(d == 0)
    {
        qtd = 1;
    }
    else
    {
        qtd = 2;
    }

    return qtd;
}

int main()
{
    float a, b, c;

    cout << "Equacao do segundo grau: axx + bx + c = 0" << endl;
    cout << "Digite o valor de a: ";
    cin >> a;
    cout << "Digite o valor de b: ";
    cin >> b;
    cout << "Digite o valor de c: ";
    cin >> c;


    cout << "Delta: " << delta(a,b,c) << endl;
    cout << "A equacao tem " << raizes(a,b,c) << " raizes.";
    return 0;
}
\end{lstlisting}

O último passo no desenvolvimento do nosso programa é imprimir na tela as raizes da equação, o que faremos em uma nova função: \verb|imprime_raizes|.

\begin{lstlisting}
#include <iostream>
#include <math.h>

using namespace std;

float delta(float a, float b, float c)
{
    return pow(b,2) - 4*a*c;
}

int raizes(float a, float b, float c)
{
    float d = delta(a,b,c);
    int qtd;

    if(d < 0)
    {
        qtd = 0;
    }
    else if(d == 0)
    {
        qtd = 1;
    }
    else
    {
        qtd = 2;
    }

    return qtd;
}

int imprime_raizes(float a, float b, float c)
{
    float d = delta(a,b,c);
    int qtd;

    if(d < 0)
    {
        cout << "A equacao tem zero raizes reais." << endl;
    }
    else if(d == 0)
    {
        cout << "A equacao tem duas raizes iguais a " << -b/(2*a);
    }
    else
    {
        cout << "A equacao tem duas raizes iguais distintas " << endl <<
        "x' = " << (-b + sqrt(d))/(2*a) << endl <<
        "x'' = " << (-b - sqrt(d))/(2*a) << endl;
    }

    return qtd;
}


int main()
{
    float a, b, c;

    cout << "Equacao do segundo grau: axx + bx + c = 0" << endl;
    cout << "Digite o valor de a: ";
    cin >> a;
    cout << "Digite o valor de b: ";
    cin >> b;
    cout << "Digite o valor de c: ";
    cin >> c;


    cout << "Delta: " << delta(a,b,c) << endl;
    cout << "A equacao tem " << raizes(a,b,c) << " raizes." << endl;
    imprime_raizes(a,b,c);
    return 0;
}
\end{lstlisting}

Note que a nova função usa a função \verb|sqrt| para calcular a raíz de $\Delta$. Esta função é uma das muitas disponíveis na linguagem C. Para usar esta função é preciso dizer ao computador sua intenção. No nosso programa, isto é feito na linha 2, isto é,\\
 \verb|#include <math.h>|\\
 em que dizemos ao computador que queremos usar as funções da biblioteca matemática da linguagem. Aproveitando a inclusão desta biblioteca também alteramos a linha 8 para usar a função  \verb|pow| para o cálculo do $b^2$. Várias outras funções estão disponíveis e podem ser consultadas em \url{http://www.cplusplus.com/reference/clibrary/cmath/}.


\todo{A seção seguinte deveria virar um capítulo e a parte if else vistos até agora se juntar ao próximo capítulo}

## {Funções e Procedimentos}
A função \verb|imprime_raizes|, definida na seção anterior, tem por objetivo imprimir na tela as raizes da equação de segundo grau, se existirem. Esta função não tem, pela nossa definição, o objetivo de calcular a quantidade de raízes (que era o objetivo da função \verb|raizes|). Em \verb|imprime_raizes| não faz sentido, então, a função ter um \emph{resultado}. Funções sem resultado são denominadas \emph{procedimentos} e, em C, são declaradas como qualquer outra função, apenas com uma particularidade: o tipo do resultado é \verb|void|. Antes de vermos alguns exemplos, precisamos ver a sintaxe de funções em geral, que estivemos usando nas seções e capítulos anteriores mas não havíamos definido formalmente.

tipo\_resultado \\
identificador\_função(tipo\_parâmetro 1 identificador\_do\_parâmetro 1, \ldots)
bloco\_de\_comandos

\begin{itemize}
\item tipo\_resultado -- o tipo do valor que a função está calculando. 
\item identificador\_função -- o nome usado para invocar a função.
\item tipo\_parâmetro 1 -- tipo do primeiro parâmetro da função.
\item identificador\_parâmetro 1 -- identificador do primeiro parâmetro da função.
\item \dots -- tipo e identificador dos demais parâmetros.
\item bloco\_de\_comandos -- instruções que compõem o corpo da função.
\end{itemize}

Como mencionado, procedimentos são funções sem um resultado e, em C, são declarados como tendo resultado do tipo \verb|void|. Em funções normais, o resultado é dado pela instrução \verb|return|; em procedimentos, que não tem resultado, \verb|return| não é utilizado. Além disso, o resultado de procedimentos não podem ser usados em atribuições.

Além de funções sem resultado, C permite a definição de funções sem parâmetros. Um exemplo deste tipo de função seria uma que lesse algum dado do usuário.
\begin{lstlisting}
int ler_idade()
{
	int id;
	cout << "Qual sua idade? " <<endl;
	cin >> id;
	return id;
}
\end{lstlisting}

Finalmente, é importante relembrar que as funções precisam ser definidas \emph{antes} de serem usadas. Sendo assim, você deve incluir a definição das funções antes da definição da função \verb|main| em seu código. \footnote{É possível escrever o código de suas funções após a função \texttt{main} ou mesmo em outros arquivos. Fazer isso, contudo, requer conhecer um pouco mais do funcionamento dos compiladores do que o escopo deste livro.}. Ainda, relembrando a primeira aula, sobre a função \verb|main|: 
\begin{enumerate}
\item A função \verb|main| tem um resultado do tipo inteiro e seu resultado é sempre 0 (\lstinline{return 0;} )\footnote{Pelo menos nos programas simples que faremos.}.
\item Função \verb|main| é como um \emph{highlander}: só pode haver uma! Isto é, cada programa só pode conter a definição de uma função com este nome.
\item Finalmente, todas as funções devem ser declaradas antes da serem usadas, pois quando o computador tenta executá-la, já deve saber de sua existência.
\end{enumerate}


## {O Tipo Primitivo \lstinline|bool|}
Como vimos neste capítulo, o \lstinline|if| avalia uma expressão lógica para decidir-se por executar ou não um bloco de comandos. Expressões lógicas, como também já visto, são aquelas que são avaliadas em verdadeiro ou falso. Na linguagem C(++), quaisquer números inteiros podem também ser avaliados como verdadeiro ou falso, seguindo a seguinte regra:
\begin{itemize}
\item 0 corresponde a falso.
\item qualquer outro número corresponde a verdadeiro.
\end{itemize}

Em C++, também é possível utilizar os valores \lstinline|true| e \lstinline|false|, que correspondem, respectivamente, a 1 e 0. Estes dois valores compõem o conjuntos dos booleanos, ou melhor, o tipo primitivo \lstinline|bool|. Isto é, \lstinline|true| e \lstinline|false| estão para \lstinline|bool| assim como -100, 10, 12, \ldots estão para \lstinline|int|.

## {Exercícios}
\begin{exercicio}
Muitas pessoas acreditam que um ano é bissexto se for múltiplo de 4. Contudo, a regra é um pouco mais complexa do que esta: 
\begin{itemize}
\item Um ano é bissexto se for múltiplo de 4 mas não de 100, ou
\item se for múltiplo de 100, então for múltiplo de 400.
\end{itemize}

Escreva um programa que leia um ano, chame uma função para calcular se o ano é bissexto e imprima sim ou não de acordo.

\begin{lstlisting}
#include <iostream>

using namespace std;

bool bissexto(int ano)
{
    if(ano % 4 == 0)
    {
        if(ano % 100 == 0)
        {
           if (ano % 400 == 0)
           {
               return true;
           }
           else
           {
               return false;
           }
        }
        else
        {
            return true;
        }
    }
    else
    {
        return false;
    }
}

int main()
{
    int ano;

    cout << "Digite o ano que deseja verificar se e bissexto: ";
    cin >> ano;

    cout << "O ano " << ano;

    if(bissexto(ano))
        cout << " e bissexto" << endl;
    else
        cout << " nao e bissexto" << endl;

    return 0;
}

\end{lstlisting}
\end{exercicio}

\begin{exercicio}
Este exercício é dividido em várias partes:

\begin{enumerate}
\item Escreva uma função que receba 3 números reais e retorne a média dos três números.
\item Escreva uma função que receba 3 números reais e retorne o menor dentre eles.
\item Escreva uma função que receba 3 números reais e retorne o maior dentre eles.
\item Escreva a função \verb|main| de forma a ler três números reais, calcular a média dos mesmos e, caso a média seja menor que 0, imprima o menor dentre os três, ou, caso a média seja maior ou igual a zero, imprima o maior dentre os três. Sua função \verb|main| deve usar as funções escritas nos itens anteriores para cálculo da média e impressão dos números.
\end{enumerate}
\end{exercicio}

\begin{exercicio}
Escreva um programa que contenha
\begin{enumerate}
\item Uma função \verb|celsius_fahrenheit| que receba uma temperatura em graus celsius e converta para fahrenheit.
\item Uma função \verb|fahrenheit_celsius| que receba uma temperatura em fahrenheit e converta para graus celsius.
\item Função \verb|main| que leia uma temperatura do teclado, pergunte ao usuário se a temperatura é em celsius ou fahrenheit, e imprima a temperatura convertida para a outra medida.
\end{enumerate}
\end{exercicio}

\begin{exercicio}
Faça uma função denominada \emph{ehPar} que receba um número inteiro como argumento e retorne verdadeiro se este número for par ou falso, caso contrário. A função \verb|main| deve ler o número e imprimir o valor retornado pela função auxiliar.
\end{exercicio}

\begin{exercicio}
Elabore um programa com as seguinte descrição:
\begin{itemize}
\item Uma função que retorna verdadeiro se três números reais recebidos como argumentos formam um triângulo ou falso, caso contrário.
\item Uma função que recebe três números reais como argumento representado os lados de um triângulo e retorna 0 caso os números formem um triângulo equilátero, 1 caso formem um triângulo isósceles, ou 2 caso sejam os lados de um triângulo escaleno.
\item Por fim, a função \verb|main| deve ler os 3  números que representam os lados, e caso formem um triângulo, imprimir se o triângulo formado é equilatero, isósceles ou escaleno.
\end{itemize}
\end{exercicio}

## {Laboratório}
Refaça no computador os exercícios propostos acima.






\chapter{Seleção Simples (II)}

Uma vez apresentado a estrutura condicional \emph{if-else}, veremos agora como realizar testes mais complexos utilizando operadores lógicos.

## {\lstinline|if-else| e Operadores Lógicos}

Até o ponto atual fizemos apenas testes simples dentro da condição dos nossos \lstinline!if!, por exemplo:
\begin{lstlisting}
...
/* 
 * esta funcao retorna verdadeiro se a pessoa de sexo 
 * (1=Masculino, 2=Feminino) e idade passados como argumentos
 * for maior que idade ou falso, caso contrario
 */
bool ehMaior(int sexo, int idade)
{
	if(sexo == 1)        // masculino
	{
		if(idade >= 18) 
		{
			return true;
		}
		else 
		{
			return false;
		}
	}
	else if(sexo == 2)  // feminino
	{
		if(idade >= 21)
		{
			return true;
		else
		{
			return false;
		}
	} 
	else             // sexo informado errado
	{
		return false;
	}
}
\end{lstlisting}

Observe que na função \verb|ehMaior| temos \lstinline{if} \emph{aninhados}, ou seja, \lstinline{if} dentro de \lstinline{if}. 
Isto porque um pessoa deve ser do sexo masculino \emph{E} possuir idade maior ou igual a 18 anos para ser considerada maior de idade. \emph{OU} ainda, ela pode ser do sexo feminino \emph{E} possuir idade igual ou maior a 21 anos.

Quando esta situação ocorre, as condições podem ser combinadas em um único \lstinline!if! utilizando-se operadores lógicos. Os operadores lógicos que usaremos são o E, o OU e a NÃO (negação).

Na linguagem C, eles são representados pelos símbolos a seguir:

\begin {table}[!ht]
\begin{center}
\caption{Operadores lógicos e seus símbolos na linguagem C.}
\begin{tabular}{|c|c|c|}\hline
Operador Lógico & Símbolo & Símbolo novo\footnote{Disponível somente em compiladores C++ ISO98} \\ \hline \hline
E & \&\& & and\\ 
OU & || & or\\
NÃO & ! & not\\ \hline
\end{tabular}
\end{center}
\end{table}

Os operadores lógicos podem ser resumidos nas tabelas a seguir:

\begin {table}[!ht] 
\begin{center}
\caption{NÃO lógico.}
{
\begin{tabular}{|c|c|}
\hline \textbf{A} & \textbf{!A} \\
\hline 
\hline V & F \\
\hline F & V \\
\hline\hline
\end{tabular}
}
\end{center}
\end{table}

\begin {table}[!ht] 
\begin{center}
\caption{E lógico.}
{
\begin{tabular}{|c|c|c|}
\hline \textbf{A} & \textbf{B} & \textbf{A \&\& B} \\
\hline 
\hline V & V & V \\
\hline V & F & F \\
\hline F & V & F \\
\hline F & F & F \\
\hline\hline
\end{tabular}
}
\end{center}
\end{table}

\begin {table}[!ht] 
\begin{center}
\caption{OU lógico.}
{
\begin{tabular}{|c|c|c|}
\hline \textbf{A} & \textbf{B} & \textbf{A || B} \\
\hline 
\hline V & V & V \\
\hline V & F & V \\
\hline F & V & V \\
\hline F & F & F \\
\hline\hline
\end{tabular}
}
\end{center}
\end{table}


Voltando ao nosso exemplo, a função anterior pode ser reescrita da seguinte forma:

\begin{lstlisting}
...
/* 
 * esta funcao retorna verdadeiro se a pessoa de sexo 
 * (1=Masculino, 2=Feminino) e idade passados como argumentos
 * for maior de idade ou falso, caso contrario
 */
bool ehMaior(int sexo, int idade)
{
	if((sexo == 1 && idade >=18) || (sexo == 2 && not(idade < 21))
	{
		return true;
	}
	else             // sexo errado ou idade errada
	{
		return false;
	}
}
\end{lstlisting}

Perceba que em apenas um \lstinline!if! colocamos a condição completa, ou seja, ``se sexo igual a 1 E idade maior ou igual a 18 OU sexo igual a 2 e idade NÃO menor do que 21 então é maior de idade''.

## {Prioridade dos Operadores}
Quando mais de um operador lógico aparece em uma expressão, a precedência pode ser expressa da seguinte maneira: primeiro o NÃO, depois o E, por último o OU. Quando houver parênteses, primeiro avalia-se o que estiver dentro dos mesmos.


Em diversas expressões e testes, diversos operadores dos vários tipos podem aparecer. A avaliação dessa expressão deve obedecer à seguinte ordem de prioridade em relação aos operadores:
\begin{enumerate}
	\item Parênteses, incremento e decremento (\lstinline|++|, \lstinline|--|)
	\item \lstinline|not| (!)
	\item Multiplicação, divisão e módulo (o que aparecer primeiro);
	\item Soma e subtração;
	\item Operadores relacionais (<, <=, >, >=)
	\item Operadores relacionais (==, !=)
%	\item OU-Exclusivo (\lstinline|^| )
	\item \lstinline|and| (\&\&)
	\item \lstinline|or| (||)
	\item Atribuição (=, +=, -=, *=, /=, \%=)
	
\end{enumerate}

Embora os operadores lógicos façam sentido somente para operandos \lstinline!bool!, é importante relembrar que, para o computador, verdadeiro e falso são apenas formas de interpretar números na memória. Na linguagem C, qualquer número diferente de 0 é tratado como \lstinline!true! e 0 é tratado como \lstinline!false!. Sendo assim, é possível aplicar operadores lógicos também à números. Contudo, sempre que requisitado a representar o valor \lstinline!true! como número, o computador usará o valor 1, o que faz com que nem todas as computações tenham resultados óbvios. Por exemplo, o código \lstinline!cout<<(2||0);! imprime, na tela, o valor 1. Isto por quê 2 é tratado como verdadeiro e 0 como falso, e o resultado de verdadeiro OU falso é verdadeiro, que é então convertido para 1.

Da mesma forma, \lstinline|!!3| é 1, pois \lstinline|!3| é falso e sua negação é verdadeiro, que é 1.

## {Exercícios}
\begin{exercicio}
Avalie o resultado de cada expressão a seguir (verdadeiro ou falso):
\begin{itemize}
\item \lstinline|2 < 5 && 15/3 == 5|
\item \lstinline|pow(3,2) - 5 > 0 && 5/2 == 3 - 4|
\item \lstinline?F || 20 == 18/3 != 21/3 / 2?
\item \lstinline?!V || 3*3/3 < 15 - 35%7?
\item \lstinline?!(5 != 10/2) || V && 2 - 5 > 5 - 2 || V?
\item \lstinline?pow(2,4) != 4 + 2 || 2 + 3 * 5/3%5 < 0?
\item \lstinline|!1+1| %1
\item \lstinline|!2+1| %1
\item \lstinline|!0+1| %2
\end{itemize}
\end{exercicio}

\begin{exercicio}
Faça um programa que:
\begin{enumerate}
	\item contenha uma função que retorna verdadeiro se um número for divisível por 3 ou 5, mas não simultaneamente pelos dois, e;
	\item na função principal sejam lidos dois números inteiros, que deverão ser passados para a função criada, tendo seu resultado impresso.
\end{enumerate}
\end{exercicio}

\begin{exercicio}
Faça uma função que receba 3 números reais (\lstinline|float|) correspondentes aos lados de um triângulo e retorne \lstinline|true| caso esse triângulo seja retângulo ou \lstinline|false| caso não o seja. A função principal deve ler os valores dos lados do triângulo, verificar se realmente formam um triângulo e imprimir "sim" se é ou "não", caso não seja triângulo retângulo; se não formar um triângulo, imprimir "não forma".
\end{exercicio}


## {Laboratório}
\begin{lab}
Escreva um programa que implemente uma calculadora com as quatro operações +,-,* e /.

Sua calculadora deve ler um número real X, seguido de um inteiro representando um dos operadores definidos (1 para -, 2 para +, 3 para * e 4 para /), seguido de outro número real Y.

Finalmente, seu programa deve escrever o resultado da operação desejada.
\end{lab}




\todo{Revisado até aqui}

\chapter{Switch}
Em diversas situações em programação, é necessário testar se uma determinada variável tem um dentre diversos possíveis valores. Nesta situação, embora seja possível usar vários \lstinline|if|, outra solução nos é dada em linguagem C: o uso de \lstinline|switch|.

## {\lstinline|switch-case-default|}
Considere o problema de transformar o mês de uma representação numérica de uma data em sua representação textual. Isto é, transformar, por exemplo, 25/12/2012 em 25 de Dezembro de 2012. Uma possível solução para este problema, em C(++), é o seguinte.

\begin{lstlisting}
#include <iostream>

using namespace std;

int main()
{
    int dia, mes, ano;

    cout << "Dia? " <<endl;
    cin >> dia;

    cout << "Mes? " <<endl;
    cin >> mes;

    cout << "Ano? " <<endl;
    cin >> ano;

    cout << dia << " de ";

    if(mes == 1)
        cout << "Janeiro";
    else if(mes == 2)
        cout << "Fevereiro";
    else if(mes == 3)
        cout << "Marco";
    else if(mes == 4)
        cout << "Abril";
    else if(mes == 5)
        cout << "Maio";
    else if(mes == 6)
        cout << "Junho";
    else if(mes == 7)
        cout << "Julho";
    else if(mes == 8)
        cout << "Agosto";
    else if(mes == 9)
        cout << "Setembro";
    else if(mes == 10)
        cout << "Outubro";
    else if(mes == 11)
        cout << "Novembro";
    else if(mes == 12)
        cout << "Dezembro";
	else
		cout << "Hein?-zembro";
    cout << " de " << ano << endl;
    return 0;
}
\end{lstlisting}

Em vez de usar vários \lstinline|if| e \lstinline|else-if|, uma solução melhor seria usar \lstinline|switch|, criado exatamente para tratar estas situações. A sintaxe do uso do \lstinline|switch| é a seguinte.\\
\lstinline|switch| (identificador)\\
\{\\
\lstinline|case| valor1: bloco\_comandos1\\
\lstinline|case| valor2: bloco\_comandos2\\
\ldots\\
\lstinline|case| valorN: bloco\_comandosN\\
\lstinline|default|: bloco\_comandos\_default\\
\}

\begin{itemize}
\item identificador: Identificador da variável a ser testada
\item valor1: primeiro caso a ser testado
\item bloco\_comandos1: bloco de comandos a ser executado caso a variável tenha valor igual a valor1
\item valor2: segundo caso a ser testado
\item bloco\_comandos2: bloco de comandos a ser executado caso a variável tenha valor igual a valor2
\item \ldots outros casos a serem testados
\item valor n: último caso a ser testado
\item bloco\_comandosN: bloco de comandos a ser executado caso a variável tenha valor igual a valorN
\item default: um valor especial, que sempre ``casa'' com o valor da variável
\item bloco\_comandos\_default: bloco de comandos a ser executado caso a variável ``case'' com default.
\end{itemize}

Usando \lstinline|switch-case-default|, o exemplo acima pode ser reescrito assim.

\begin{lstlisting}
#include <iostream>

using namespace std;

int main()
{
    int dia, mes, ano;

    cout << "Dia? " <<endl;
    cin >> dia;

    cout << "Mes? " <<endl;
    cin >> mes;

    cout << "Ano? " <<endl;
    cin >> ano;

    cout << dia << " de ";

    switch(mes)
    {
    case 1:
        cout << "Janeiro";
    case 2:
        cout << "Fevereiro";
    case 3:
        cout << "Marco";
    case 4:
        cout << "Abril";
    case 5:
        cout << "Maio";
    case 6:
        cout << "Junho";
    case 7:
...
    case 11:
        cout << "Novembro";
    case 12:
        cout << "Dezembro";
    default:
        cout << "Hein?-zembro";
    }
    cout  << " de " << ano << endl;
    return 0;
}
\end{lstlisting}

Execute este código e digite, por exemplo, a data 1/1/2012 para ver que ele funciona ``quase'' corretamente. O problema, você deve ter observado, é que além de imprimir o nome do mês correto, o programa imprime também o nome de todos os meses subsequentes e o valor \lstinline|default|.  Isso ocorre por que, na verdade, o \lstinline|switch| começa a executar o bloco correspondente ao \lstinline|case| com o valor da variável mas, a partir daí, executa todos os blocos a não ser que seja instruído a fazer diferente, o que é feito via a instrução \lstinline|break|.

## {\lstinline|break|}
A instrução \lstinline|break| diz ao computador que pare de executar o \lstinline|switch| no ponto em que é invocada.\footnote{Mais tarde veremos outros blocos no qual o \lstinline|break| pode ser utilizado.} Sendo assim, podemos reescrever o programa mais uma vez para obter exatamente o comportamento da versão usando \lstinline|if|.

\begin{lstlisting}
#include <iostream>

using namespace std;

int main()
{
    int dia, mes, ano;

    cout << "Dia? " <<endl;
    cin >> dia;

    cout << "Mes? " <<endl;
    cin >> mes;

    cout << "Ano? " <<endl;
    cin >> ano;

    cout << dia << " de ";

    switch(mes)
    {
    case 1:
        cout << "Janeiro";
        break;
    case 2:
        cout << "Fevereiro";
        break;
    case 3:
        cout << "Marco";
        break;
    case 4:
        cout << "Abril";
        break;
    case 5:
        cout << "Maio";
        break;
    case 6:
        cout << "Junho";
        break;
    case 7:
        cout << "Julho";
        break;
    case 8:
        cout << "Agosto";
        break;
    case 9:
        cout << "Setembro";
        break;
    case 10:
        cout << "Outubro";
        break;
    case 11:
        cout << "Novembro";
        break;
    case 12:
        cout << "Dezembro";
        break;
    default:
        cout << "Hein?-zembro";
        break;
    }

    cout << " de " << ano << endl;
    return 0;
}
\end{lstlisting}




## {Exercícios}
\begin{exercicio}
\label{exe:switch:1}
Implemente uma função chamada \lstinline|menu| que imprima o seguinte menu na tela:
\begin{enumerate}
\item Soma
\item Média
\item Menor
\item Maior
\end{enumerate}
Leia e que retorne o número da opção escolhida.

Implemente a função \lstinline|main| de forma a ler três números e, então, invocar a função definida acima para decidir o que fazer. O resultado da função deve ser armazenando em uma variável e seu conteúdo testado com \lstinline|switch|. Cada opção deve invocar a função respectiva, que calculará e retornará o que se pede. A função \lstinline|main| imprimirá então o resultado.

\begin{lstlisting}
#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;

int menu()
{
    int opcao;
    cout << "1 Soma" << endl << "2 Media" << endl << "3 Menor" << endl << "4 Maior" << endl;
    cout << "Qual sua opcao? ";

    cin >> opcao;
    return opcao;
}

int menor(int x, int y, int z)
{
    if(x <= y && x <= z)
        return x;

    if(y <= x && y <= z)
        return y;

    return z;
}

int maior(int x, int y, int z)
{
    if(x >= y && x >= z)
        return x;
    else if(y >= x && y<= z)
        return y;
    else
        return z;
}

int soma(int x, int y, int z)
{
    return x+y+z;
}

float media(int x, int y, int z)
{
    float somatorio = soma(x,y,z);
    return somatorio / 3.0;
}

int main()
{
    int a, b, c;
    int opcao;

    cout << "digite tres numero inteiros" <<endl;

    cin >> a >> b >> c;

    opcao = menu();

    switch(opcao)
    {
        case 1:
            cout << "A soma dos tres numeros eh " << soma(a,b,c);
            break;
        case 2:
            cout << "A media dos tres numeros eh " << media(a,b,c);
            break;
        case 3:
            cout << "O menor dentre os tres numeros eh " << menor(a,b,c);
            break;
        case 4:
            cout << "O maior dentre os tres numeros eh " << maior(a,b,c);
            break;
        default:
            cout << "Opcao invalida. Execute o programa novamente e leia direito as opcoes.";
    }

    return 0;
}
\end{lstlisting}
\end{exercicio}

\begin{exercicio}
Escreva um programa com uma função que receba um inteiro entre 1 e 7, inclusive, e escreva o dia correspondente da semana (1 para domingo e 7 para sábado).
\end{exercicio}

\begin{exercicio}
\label{exe:switch:3}
Escreva um programa com uma função que receba um inteiro de 1 a 12 e retorne a quantidade de dias no mês correspondente (assuma que o ano não é bisexto).

Para este exercício, a solução mais simples envolve não colocar \lstinline|break| em alguns dos \lstinline|case|.
\end{exercicio}

## {Laboratório}
Implemente os exercícios de \ref{exe:switch:1} a \ref{exe:switch:3}.







\chapter{Repetição (I)}

Em certas situações é necessária a repetição de um conjunto de comandos. Em situações como esta, temos duas opções: ou copiamos e colamos todo o trecho que desejamos repetir, fazendo os ajustes necessários; ou utilizamos uma saída mais inteligente por meio de comandos especiais que permitem automatizar a repetição. Neste capítulo veremos o comando de repetição \lstinline|while| e alguns exemplos de seu uso.

## {Motivação}

Suponha de você deseja fazer um programa para ler duas notas, calcular e imprimir a média de dez alunos da disciplina. A maneira menos prática de fazer isso seria:

\begin{lstlisting}
...
float nota1, nota2, media;
cout << "Entre nota 1 e nota 2 do aluno 1: " << endl;
cin >> nota1 >> nota2;
media = (nota1 + nota2) / 2;
cout << "A media das notas eh " << media << endl;
cout << "Entre nota 1 e nota 2 do aluno 2: " << endl;
cin >> nota1 >> nota2;
media = (nota1 + nota2) / 2;
cout << "A media das notas eh " << media << endl;
cout << "Entre nota 1 e nota 2 do aluno 3: " << endl;
cin >> nota1 >> nota2;
media = (nota1 + nota2) / 2;
cout << "A media das notas eh " << media << endl;
cout << "Entre nota 1 e nota 2 do aluno 4: " << endl;
cin >> nota1 >> nota2;
media = (nota1 + nota2) / 2;
cout << "A media das notas eh " << media << endl;
cout << "Entre nota 1 e nota 2 do aluno 5: " << endl;
cin >> nota1 >> nota2;
media = (nota1 + nota2) / 2;
cout << "A media das notas eh " << media << endl;
cout << "Entre nota 1 e nota 2 do aluno 6: " << endl;
cin >> nota1 >> nota2;
media = (nota1 + nota2) / 2;
cout << "A media das notas eh " << media << endl;
cout << "Entre nota 1 e nota 2 do aluno 7: " << endl;
cin >> nota1 >> nota2;
media = (nota1 + nota2) / 2;
cout << "A media das notas eh " << media << endl;
cout << "Entre nota 1 e nota 2 do aluno 8: " << endl;
cin >> nota1 >> nota2;
media = (nota1 + nota2) / 2;
cout << "A media das notas eh " << media << endl;
cout << "Entre nota 1 e nota 2 do aluno 9: " << endl;
cin >> nota1 >> nota2;
media = (nota1 + nota2) / 2;
cout << "A media das notas eh " << media << endl;
cout << "Entre nota 1 e nota 2 do aluno 10: " << endl;
cin >> nota1 >> nota2;
media = (nota1 + nota2) / 2;
cout << "A media das notas eh " << media << endl;
...
\end{lstlisting}

Este código tem vários problemas. Primeiro, ele é mais propenso a erros; se, por exemplo, você resolve renomear a variável \lstinline|nota2| para \lstinline|notab|, você terá que fazê-lo em diversos pontos do programa, aumentando a possibilidade de esquecer algum.
Em segundo lugar, o código exigiu grande retrabalho, isto é, a repetição de uma mesma tarefa por parte do programador.
Finalmente, se você precisar aumentar a quantidade de repetições para, digamos, 100 alunos, terá que estender o código por páginas e páginas.

Para evitar tais problemas, para estas situações a linguagem C(++) fornece estruturas de repetições, as quais permitem repetir um determinado conjunto de comandos.

## {O comando \lstinline|while|}

Um destes comandos é o comando \lstinline|while| (enquanto, em português). Sua forma geral é muito simples:

\begin{lstlisting}
while (<condicao>)
{
	// bloco de comandos a ser repetido
}
\end{lstlisting}

O bloco de comandos entre as chaves será repetido \textbf{enquanto a condição dentro dos parênteses for verdadeira}.

Utilizando o \lstinline|while|, o exemplo anterior pode ser reescrito de maneira bem mais prática:

\begin{lstlisting}
...
float nota1, nota2, media;
int i = 1;  // valor inicial do identificador do aluno

while (i <= 10)
{
	cout << "Entre nota 1 e nota 2 do aluno: " << endl;
	cin << nota1 << nota2;
	media = (nota1 + nota2) / 2;
	cout << "A media das notas eh " << media << endl;
	i = i +1; // aumentamos o valor de i no final de cada calculo da media
}
...
\end{lstlisting}

Observe as seguintes modificações:
\begin{itemize}
	\item Uma nova variável, \lstinline|i|, foi criada para contabilizar o número de alunos.
	\item Esta variável é inicializada com o valor 1, representando o primeiro aluno.
	\item A condição dentro do comando de repetição será verdadeira enquanto o valor de \lstinline|i| for menor ou igual a 10.
	\item Por este motivo, devemos incrementar o valor de \lstinline|i| ao fim de cada ciclo.
\end{itemize}

Normalmente, a variável que conta a quantidade de iterações executadas, \lstinline|i| no exemplo dado, é chamada de contadora. No exemplo, a variável contadora foi usada apenas para este fim, contar, e não aparece no bloco de comandos sendo repetido. Isto nem sempre é o caso, como veremos em outros exemplos. Antes, porém, vejamos uma variação do \lstinline|while|.

## {O comando \lstinline|do-while|}

Se por acaso a condição verificada no \lstinline|while| for inicialmente falsa, o bloco não será repetido nem mesmo uma vez. Para situações em que é preciso executar o bloco pelo menos uma vez, uma variação do comando \lstinline|while| é fornecida pela linguagem C. Trata-se do comando \lstinline|do-while| (faça-enquanto ou repita-enquanto, em português). Sua forma geral é dada por:
\begin{lstlisting}
do
{
	\\ bloco de comandos
	\\ a ser repetido
}
while (<condicao>);
\end{lstlisting}

O mesmo exemplo anterior pode ser reescrito utilizando este comando:

\begin{lstlisting}
do {
	cout << "Entre nota 1 e nota 2 do aluno : " << endl;
	cin >> nota1 >> nota2;
	i = 1+1; // aumentamos o valor de i no final de cada calculo da media
	media = (nota1 + nota2) / 2; 
	cout << "A media das notas eh " << media << endl;
}
while (i <= 10);
\end{lstlisting}

Em comparação ao comando \lstinline|while|, a única diferença existente é o fato do teste da condição ser feito após a execução do bloco de comandos que se deseja repetir. Uma implicação disto é que, em casos em que a condição é falsa logo no primeiro teste, o bloco de comandos é executado com \lstinline|do-while|, mas não é executado com \lstinline|while|. Isto aconteceria para a variável \lstinline|i| com valor inicial de 11, por exemplo.

## {Mais exemplos}

Considere que deseja-se somar todos os números pares entre 1 e 999. Ou fazemos uma soma com todos os valores em uma linha enorme, ou utlizamos o que apresendemos sobre comandos de repetição. Utilizando o \lstinline|while|, teríamos:

\begin{lstlisting}
...
int n = 2, // primeiro par maior do que 1
    soma = 0; // soma inicialmente zerada
while (n < 999)
{
	soma = soma + n;
	n = n + 2;
}
cout << "O valor da soma eh " << soma << endl;
...
\end{lstlisting}

Observe que a cada iteração o valor de soma é acrescido do próximo número par, o qual é obtido somando-se 2 ao valor de \lstinline|n|.

Imagine que se deseja obter o maior entre 10 números inteiros lidos. Utilizando o \lstinline|do-while|, uma possível solução seria:



\begin{lstlisting}
...
int i = 0, // contador da qtde de numeros lidos
    maior,
    n; 
do
{
	cout << "Entre um numero: ";
	cin >> n;
	if (i == 0) // se for o primeiro numero lido
	{           // ele sera o menor
		maior = n;
	}
	else        // a partir do segundo
	{
		if(n > maior) // atualizo o maior
		{
			maior = n;
		}
	}
    i = i + 1;
}
while (i < 10);
...
\end{lstlisting}

Neste exemplo temos uma situação especial em que, no primeiro caso (\lstinline|i = 0|), o maior valor é o único valor lido. A partir do segundo número, se o número lido for maior do que o valor armazenado na variável \lstinline|maior|, esta será atualizada.

Em outro exemplo, imagine que queira ler números até que leia um número maior que 100. Neste caso, o seguinte programa resolveria nosso problema.

\begin{lstlisting}
...
int num; 
do
{
	cout << "Entre um numero: ";
	cin >> num;
}
while (! num > 100);
...
\end{lstlisting}

Neste exemplo utilizamos \lstinline|do-while| pois é necessário ler pelo menos um número. Reescreva o código utilizando \lstinline|while| e veja como fica, necessariamente, mais complexo.


### {Operadores de incremento e outras construções especiais}
Nos exemplos apresentados, a variável contadora foi manipulada em todas as repetições de uma forma bem comum, sendo incrementada de 1 em 1 ou de 2 em 2. Repetições tem esta característica, embora as operações aplicadas aos contadores não sejam sempre simples incrementos e decrementos. Com a finalidade de agilizar o desenvolvimento e simplificar algumas operações aritméticas mais comuns, a linguagem C(++) permite algumas construções especiais envolvendo operadores. Considere o seguinte trecho de código:
\begin{lstlisting}
int a, b;
...
a = a + b;
b = b * 2;
a = a / 7;
\end{lstlisting}

Observe que nas três atribuições (indicadas pelo sinal de igualdade), as variáveis que são atualizadas também aparecem como primeiro elemento da operação aritmética à esquerda. Nestas situações, podemos reescrever as atribuições assim:
\begin{lstlisting}
int a, b;
...
a += b;
b *= 2;
a /= 7;
\end{lstlisting}

As operações de incremento (aumento de uma unidade) e o decremento (diminuição de uma unidade) de uma variável são muito comuns em programação. Sendo assim, a linguagem C define dois operadores para as mesmas: \verb|++| e \verb|--|, respectivamente. Veja o exemplo.

\begin{lstlisting}
int a = 0;
a = a + 1;
cout << "a = " << a << endl;
a += 1;
cout << "a = " << a << endl; 
a++;
cout << "a = " << a << endl; 
a--;
cout << "a = " << a << endl;
\end{lstlisting}

O trecho acima deve imprimir os valores de \lstinline|a|, ou seja, 1, 2, 3 e 2.

\newpage
## {Exercícios}
\begin{exercicio}
Diga o que será escrito na tela durante a execução do
seguinte trecho de código:
\begin{lstlisting}
int a, b = 0, c = 0;
a = ++b + ++c;
cout << a << ", " << b << ", " << c << endl;
a = b++ + c++;
cout << a << ", " << b << ", " << c << endl;
a = ++b + c++;
cout << a << ", " << b << ", " << c << endl;
a = b-- + --c;
cout << a << ", " << b << ", " << c << endl;
\end{lstlisting}
\end{exercicio}




\todo{Incluir exercícios mais simples como os da lista 1 do Prof. Anilton.}

Faça os exercícios a seguir à mão.

\begin{exercicio}
Faça uma função que recebe um número inteiro positivo e retorna o fatorial deste número. A função principal deve ler o número do qual se deseja calcular o fatorial e imprimir o resultado.
\end{exercicio}

\begin{exercicio}
Faça uma função que recebe um número inteiro positivo e retorna \lstinline|true| se o número for primo ou \lstinline|false|, caso contrário. A função principal (\lstinline|main|) deve ler o número e imprimir o resultado.
\end{exercicio}

\begin{exercicio}
Modifique o programa anterior para imprimir todos os números primos abaixo de dois milhões.
\end{exercicio}

\begin{exercicio}
Faça um programa que leia um número inteiro positivo e imprima esse número de trás pra frente.
A impressão deve ser feita pela função auxiliar \texttt{inverteNumero}.
\end{exercicio}


\newpage
## {Laboratório}
\begin{lab}
Implemente os exercícios acima no Code::Blocks.
\end{lab}


\begin{lab}
Escreva uma função que receba dois parâmetros inteiros, $x$ e $y$, $x < y$ e que imprima $y$ pontos na tela e que a cada $x$ pontos, imprima um acento circunflexo.
\end{lab}


\begin{lab}
\label{exer:floyd}
O exercício \ref{exer:menu} pedia que você escrevesse uma função que gerasse um menu na tela. A função que você escreveu tinha um problema: ela aceitava qualquer valor, mesmo algum não correspondendo a nenhuma opção do menu.

Usando \lstinline|do-while|, altere sua função para que continue exibindo o menu e lendo uma opção até que uma opção válida seja digitada pelo usuário.
\end{lab}


\begin{lab}
Implemente uma função chamada \lstinline|pot| que receba um número real e um inteiro, respectivamente \lstinline|base| e \lstinline|expoente|, como parâmetros e que calcule \small{$\texttt{base}^\texttt{expoente}$}. 

A função \lstinline|pot|, que você implementará, deve usar multiplicações sucessivas para calcular seu resultado (isto é, é proibido o uso da função \lstinline|pow|).
\end{lab}


\begin{lab}
Execute o seguinte programa em seu computador e observe o que acontece.

\begin{lstlisting}
...
int num = 10; 
do
{
	cout << num;
	num *= 2;
}
while (1);
...
\end{lstlisting}

À propósito, para terminar um programa basta digitar a combinação de teclas \texttt{ctrl+c}.

\end{lab}


\begin{lab}
Escreva um programa que leia um numero inteiro positivo \texttt{n} e em seguida imprima \texttt{n} linhas do chamado Triângulo de Floyd:\\
\begin{verbatim}
 1
 2  3
 4  5  6
 7  8  9 10
11 12 13 14 15
16 17 18 19 20 21
\end{verbatim}
\end{lab}

\begin{lab}
Faça um programa que gera um número inteiro aleatório de 1 a 1000 em uma função denominada \lstinline|geraNumero|. Na função principal, o usuário deve tentar acertar qual o número foi gerado. A cada tentativa o programa deverá informar se o chute é menor ou maior que o número gerado. O programa acaba quando o usuário acerta o número gerado. O programa deve informar em quantas tentativas o número foi descoberto.
\end{lab}

\begin{lab}
Escreva um programa que receba como entrada o valor do saque realizado pelo cliente de um banco e retorne quantas notas de cada valor serão necessárias para atender ao saque com a menor quantidade de notas possível. Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 reais. O cálculo e impressão do resultado deve ser efetuado por uma função auxiliar denominada \texttt{imprimeNotas}.
\end{lab}













\chapter{Repetição (II)}
Você deve ter percebido que no uso de \lstinline|do-while| e  \lstinline|while| quase sempre seguimos os mesmos passos:
\begin{itemize}
\item declarar uma variável que sirva de controle para a iteração;
\item iniciar a variável de controle (e possivelmente outras);
\item verificar a condição para iteração
\item executar iteração
\item executar incremento/decremento (mudança da variável de controle)
\end{itemize}

A linguagem C tem um comando iteração que agrega todos estes passos, chamado \lstinline|for|.

## {\lstinline|for|}
Sua forma geral do comando \lstinline|for| é a seguinte:
\begin{lstlisting}
for(DI; C; I)
{
	\\bloco de comandos a ser repetido
}
\end{lstlisting}

O comando \lstinline|for| tem três partes em sua declaração, além dos comandos a serem repetidos.
\begin{itemize}
\item DI -- em DI variáveis podem ser \textbf{D}eclaradas e \textbf{I}niciadas. Variáveis já existentes também podem ter seus valores ajustados em DI;
\item C -- C define a \textbf{C}ondição necessária à execução do bloco de comandos. \emph{Enquanto} a condição for verdadeira, o bloco será executado.
\item I -- comandos de modificação de variáveis, como \textbf{I}ncremento e decremento, são colocados diretamente na declaração do \lstinline|for|. O comando é executado ao final de cada iteração.
\end{itemize}

A execução do \lstinline|for| segue os seguintes passos:
\begin{enumerate}
\item Iniciação (execução de DI)
\item Avaliação (teste da condição em C)
\item Execução do bloco de comandos
\item Incremento
\item De volta ao passo 2
\end{enumerate}

Considere o exemplo do capítulo anterior em que deseja-se somar todos os números pares entre 1 e 999. O código pode ser escrito, como vimos, usando \lstinline|while|.

\begin{lstlisting}
...
int n = 2, // primeiro par maior do que 1
    soma = 0; // soma inicialmente zerada
while (n < 999)
{
	soma = soma + n;
	n += 2;
}
cout << "O valor da soma eh " << soma << endl;
...
\end{lstlisting}

O código equivalente, usando \lstinline|for| é essencialmente o mesmo.

\begin{lstlisting}
...
int n, // primeiro par maior do que 1
    soma = 0; // soma inicialmente zerada
for (n = 2; n < 999; n += 2)
{
	soma = soma + n;
}
cout << "O valor da soma eh " << soma << endl;
...
\end{lstlisting}

O código, contudo, pode ser simplificado colocando-se a declaração da variável de controle no próprio \lstinline|for|.

\begin{lstlisting}
...
int soma = 0; // soma inicialmente zerada
for (int n = 2; n < 999; n += 2)
{
	soma = soma + n;
}
cout << "O valor da soma eh " << soma << endl;
...
\end{lstlisting}

É possível declarar e iniciar mais de uma variável no DI, mas não é possível definir novas variáveis e iniciar outras já definidas. No exemplo abaixo, errado, a variável soma sendo iniciada no \lstinline|for| é diferente da variável definida antes do comando, apesar do nome ser igual.

\begin{lstlisting}
...
int soma = 0; // soma inicialmente zerada
for (int n = 2, soma = 0; n < 999; n += 2)
{
	soma = soma + n;
}
cout << "O valor da soma eh " << soma << endl;
...
\end{lstlisting}


## {Mais Exemplos}
Também do capítulo anterior, imagine o exemplo em que se deseja obter o maior entre 10 números inteiros lidos. Utilizando o \lstinline|for|, uma possível solução seria:

\begin{lstlisting}
...
int i, // contador da qtde de numeros lidos
    maior,
    n; 

cout << "Entre um numero: ";
cin >> n;
maior = n;

for(i = 0; i < 9; i++)
{
	cout << "Entre um numero: ";
	cin >> n;
	if(n > maior) // atualizo o maior
	{
		maior = n;
	}
}
...
\end{lstlisting}

Observe que a primeira leitura aconteceu fora do \lstinline|for|.


## {Declarações especiais}
Em certas situações pode ser desejável omitir partes da declaração do \lstinline|for|. Por exemplo, se as variáveis de controle já tiverem sido iniciadas ou, simplesmente, se não existirem, ou se não houver incremento a ser feito, então estas partes da declaração podem ser deixadas em branco. Por exemplo,

\begin{lstlisting}
int menu()
{
    int opcao = 0;
    
    for( ; opcao < 1 || opcao > 4 ; )
    {
        cout << "1 Soma" << endl 
             << "2 Media" << endl 
             << "3 Menor" << endl 
             << "4 Maior" << endl;

        cout << "Qual sua opcao? ";

	    cin >> opcao;
    }
    return opcao;
}
\end{lstlisting}


Observe que embora neste exemplo tanto DI quanto I estão vazias, isso não é necessário. Isto é, qualquer das partes da declaração podem estar vazias independentemente, inclusive a segunda parte.

## {Alterando a repetição com o \lstinline!break! e \lstinline!continue!}
Caso a segunda parte do comando esteja vazia, a repetição será executada \emph{ad infinitum} ou até que seja interrompida. A interrupção de uma iteração pode ser feita usando-se o comando \lstinline{break}. Veja o exemplo anterior reescrito para usar tal comando.

\begin{lstlisting}
int menu()
{
    int opcao;
    
    for(;;)
    {
        cout << "1 Soma" << endl 
             << "2 Media" << endl 
             << "3 Menor" << endl 
             << "4 Maior" << endl;

        cout << "Qual sua opcao? ";

	    cin >> opcao;
	    
	    if(opcao > 0 && opcao < 5)
	        break;
	    else
	    	cout << "Opcao invalida" << endl << endl;
    }

    return opcao;
}
\end{lstlisting}

Outra forma de se alterar o fluxo é via o comando \lstinline{continue}, que faz com que a o restante do bloco de comandos seja ignorado e, conseqüentemente, incremento e condição sejam reavaliados. Por exemplo, reescrevendo o código acima para o usar o \lstinline{continue}.

\begin{lstlisting}
int menu()
{
    int opcao;
    
    for(;;)
    {
        cout << "1 Soma" << endl 
             << "2 Media" << endl 
             << "3 Menor" << endl 
             << "4 Maior" << endl;

        cout << "Qual sua opcao? ";

	    cin >> opcao;
	    
	    if(opcao < 1 || opcao > 4)
	        continue;
	    
	    cout << "A opcao escolhida foi " << opcao;
	    break;
    }

    return opcao;
}
\end{lstlisting}

## {Exercícios}
\begin{exercicio}
Refaça os execícios do capítulo anterior usando \lstinline|for|.
\end{exercicio}

## {Laboratório}
\begin{lab}
Refaça o laboratório do capítulo anterior usando \lstinline|for|.
\end{lab}

\begin{lab}
Escreva uma função que receba dois parâmetros inteiros, X e Y, e imprima X linhas na tela, cada uma com Y ``.''.
Por exemplo, se sua função for invocada com X igual 3 e Y igual 2, o resultado deveria ser o seguinte
\begin{verbatim}
..
..
..
\end{verbatim}

\end{lab}

\begin{lab}
Escreva uma função que receba dois parâmetros inteiros, X e Y, e imprima de forma decrescente os números de X*Y até 1, em X linhas de Y números.
Por exemplo, se sua função for invocada com X igual 4 e Y igual 3, o resultado deveria ser o seguinte
\begin{verbatim}
12 11 10
9 8 7
6 5 4
3 2 1
\end{verbatim}
\end{lab}
















\chapter{Arranjos Unidimensionais}
Tente resolver o seguinte problema: 
\begin{enumerate}
\item ler um conjunto de 6 números inteiros
\item calcular sua média
\item imprimir todos os números maiores que a média na tela do computador
\end{enumerate}
Fácil, certo? Basta declarar 6 variáveis do tipo \lstinline|int|, ler seus valores, somar seus valores e dividir por 6, calculando a média. Finalmente, basta escolher aquelas variáveis com números maiores que a média e imprimí-las.

Mas e se alterássemos o problema para que, em vez de 6, precisasse ler 10 números, ou 100? Ainda assim se poderia usar o mesmo algoritmo, com 10 ou 100 variáveis em vez de 6. Mas ter muitas variáveis distintas com a mesma finalidade não é viável por duas razões:
\begin{itemize}
\item difícil de manter: se você precisar renomear uma variável, terá que fazê-lo em todas as variáveis;\\
	se precisar aumentar ou diminuir o número de variáveis, terá que apagar/copiar e renomear.
\item evita reuso de código: se uma mesma operação precisa ser aplicada a cada variável, o mesmo código deve ser reescrito para cada variável, dificultado o reuso de código.
\end{itemize}


A solução para esta situação é o uso de vetores (ou variáveis indexadas, ou arranjo, ou \emph{array}).

## {Vetores}
Continuando com nossa analogia da memória do computador como uma planilha eletrônica, um vetor é uma variável que nomeia diversas células contíguas da memória do computador. Isto é, de certa forma, enquanto uma variável \lstinline|int| corresponde a uma área da memória que cabe 1 inteiro, um vetor de 10 \lstinline|int| é uma variável que cabe 10 inteiros.

A sintaxe para a declaração estática de vetores é bem simples (em capítulos futuros veremos como declarar vetores dinâmicos, isto é, que podem variar seus tamanhos).

\begin{verbatim}
tipo identificador[tamanho];
\end{verbatim}

Onde
\begin{itemize}
\item tipo -- é o tipo do dado a ser armazenado em cada posição do vetor;
\item identificador -- é o nome do vetor;
\item tamanho -- é a quantidade de células no vetor;
\end{itemize}

O acesso a uma célula, para leitura ou atribuição, é feito usando-se o identificador seguido pela posição a ser acessada, entre colchetes (\lstinline{[]}). Por exemplo, \lstinline{x[3] = 0} atribui o valor 0 à posição de índice 3 do vetor \lstinline|x|. Algo importante a ser observado aqui é que a primeira posição de um vetor de tamanho $n$ tem índice 0 e a última tem índice $n-1$.

O exemplo a seguir resolve o problema apresentado na seção anterior usando vetores.

\begin{lstlisting}
#include<iostream>

using namespace std;

#define TAMANHO 10

int main()
{
  int num[TAMANHO];
  int soma = 0;
  int media;
  
  for(int i = 0; i < TAMANHO; i++)
  {
      cout << "Digite o " << i << "-esimo valor: ";
      cin >> num[i]; 
      soma += num[i];
  }
  
  media = soma/TAMANHO;
  
  cout << "Os valores acima da media " << media << " sao" << endl;
  for(int i = 0; i < TAMANHO; i++)
  {
     if(num[i] > media)
         cout << num[i] << endl;
  }
  
  return 0;
}
\end{lstlisting}

Observe a definição e o uso da palavra \lstinline{TAMANHO} no programa. Uma vez definido que \lstinline{TAMANHO} tem o valor 10, o computador substituirá toda ocorrência desta palavra no programa pelo valor correspondente, \emph{antes} da compilação.


Uma variação interessante do problema calcula a média apenas de números positivos e a entrada de um número negativo serve para finalizar o fim da entrada. O código seguinte resolve o problema.
\begin{lstlisting}
#include<iostream>

using namespace std;

#define TAMANHO 100

int main()
{
  int num[TAMANHO];
  int soma = 0;
  int media;
  int contador = 0;
  
  for(int i = 0; i < TAMANHO; i++)
  {
      cout << "Digite o " << i << "-esimo valor: ";
      cin >> num[i];
      
      if(num[i] >= 0)
      { 
         soma += num[i];
         contador++;
      }
      else
      {
         break;
      }
  }
  
  media = soma/contador;
  
  cout << "Os valores acima da media " << media << " sao" << endl;
  for(int i = 0; i < contador; i++)
  {
     if(num[i] > media)
         cout << num[i] << endl;
  }
  
  return 0;
}
\end{lstlisting}
Observe como a variável \lstinline|contador| é usada para contar a quantidade de números válidos lidos e como ela é usada como limitante da varredura do vetor no segundo \lstinline|for|. Observe também como o \lstinline|break| é utilizado para interromper o \lstinline|for|.


## {Exercícios}

\begin{exercicio}
Escreva um programa que leia 10 números e imprima o menor e o maior entre eles (não é necessário usar vetores aqui).
\end{exercicio}

\begin{exercicio}
Escreva um programa que leia 10 números e calcule e imprima a média e desvio padrão dos mesmos. Lembre-se que o desvio padrão é definido como a raiz quadrada dos quadrados das diferenças dos valores para a média dos valores.
\end{exercicio}

\begin{exercicio}
Escreva um programa que leia 11 números reais e imprima os valores dos 10 primeiros multiplicados pelo 11-ésimo. 
Por exemplo, se os valores digitados foram 1, 2, 3 ,4 ,5 ,6, 7, 8, 9, 10 e 1.1, então seu programa deve imprimir 1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9 e 11.0.
\end{exercicio}

## {Laboratório}
\begin{lab}
Escreva um programa que leia um número inteiro \lstinline|n| e então leia \lstinline|n| números reais. Em seguida, seu programa deve imprimir a média e desvio padrão dos números lidos. Seu programa deve \textbf{ignorar} números negativos.
\end{lab}


\begin{lab}
Escreva um programa que leia \lstinline|n| números reais e imprima seus valores na tela. Em seguida, leia mais um número real \lstinline|x| e imprima o valor dos \lstinline|n| números multiplicados \lstinline|x|. 
\end{lab}

\begin{lab}
Escreva um programa que leia \lstinline|n| booleanos e imprima seus valores na tela. Em seguida, imprima todos os booleanos invertidos, na linha seguinte. 
\end{lab}





















\chapter{Caracteres, Vetores de Caracteres e Strings}
## {Representação de caracteres}
Além dos tipos de dados numéricos com os quais temos trabalhado até agora, outro tipo de dado é muito importante no desenvolvimento de programas de computador, o tipo caractere. Estes tipos são a base para representação de informação textual como, por exemplo, a frase "eu amo programar em C"? 

Variáveis com caracteres, em C(++), são declarados com sendo do tipo \lstinline|char|, e sua leitura e escrita ocorre como para qualquer outro tipo de dados. Por exemplo, 

\begin{lstlisting}
#include<iostream>

using namespace std;

int main()
{
  char letra;

  cout << "digite uma letra qualquer seguida de enter ";
  cin >> letra; 
  cout << "voce digitou "<< letra << endl;
  
  return 0;
}
\end{lstlisting}

Se você pretende atribuir um caracter diretamente a uma variável, é importante se atentar à seguinte notação: caracteres são sempre escritos entre aspas simples. Por exemplo, \lstinline|'a'|, \lstinline|'3'| ou \lstinline|'.'|. 

Raramente você trabalhará com caracteres um a um, normalmente usando vetores para armazenar palavras e frases.

## {Vetores de Caracteres}
Vetores podem conter dados de quaisquer tipos. Isto é, você pode declarar vetores de números reais ou inteiros, booleanos, e até tipos definidos por você, uma vez que aprenda como definir novos tipos. Um outro tipo interessante é o caractere, ou simplesmente \lstinline|char|. Por exemplo, vamos definir um programa que leia um vetor de 10 caracteres e depois os escreva de volta à tela.

\begin{lstlisting}
#include<iostream>

using namespace std;

#define TAMANHO 10

int main()
{
  char nome[TAMANHO];

  cout << "Digite " << TAMANHO << " caracteres: ";
  
  for(int i = 0; i < TAMANHO; i++)
  {
      cin >> nome[i]; 
  }
  
  cout << "Os caracteres digitados foram: ";
  for(int i = 0; i < TAMANHO; i++)
  {
         cout << nome[i];
  }
  
  cout << endl;
  
  return 0;
}
\end{lstlisting}

Agora, só para tornar as coisas mais interessantes, alteremos o programa para que leia \emph{até} 100 caracteres, mas que pare de lê-los tão logo um ``.'' seja digitado. Para representar um caractere em C(++), use aspas simples, isto é, \lstinline|'.'|.

\begin{lstlisting}
#include<iostream>

using namespace std;

#define TAMANHO 100

int main()
{
  char nome[TAMANHO];
  int i = 0;
  
  cout << "Digite ate " << TAMANHO << " caracteres. Para terminar antes, digite '.' ";

  do
  {
      cin >> nome[i]; 
      i++;
  }while( i < TAMANHO && nome[i-1] != '.');
  
  cout << "Os caracteres digitados foram: "
  for(int i = 0; i < TAMANHO && nome[i] != '.'; i++)
  {
         cout << nome[i];
  }
  
  cout << endl;
  
  return 0;
}
\end{lstlisting}


Caracteres são, na verdade, números disfarçados e seguem uma codificação específica. Uma pessoa pode decidir que o 'a' será o 1, o 'b' será o 2 e assim por diante. Mas como outra pessoa que receber a informação saberá disso? Para evitar este problema a representação de caracteres como números foi padronizada. Os principais padrões existentes são: ASCII, EBCDIC e Unicode.

### *{ASCII}

ASCII, ou \emph{American Standard Code for Information Interchange}, é o padrão mais utilizado, presente em todos os nossos computadores pessoais. Trata-se de uma codificação de caracteres de oito bits baseada no alfabeto inglês.

A codificação define 256 caracteres ($2^8$). Desses, 33 não são imprimíveis, como caracteres de controle atualmente não utilizáveis para edição de texto, porém amplamente utilizados em dispositivos de comunicação, que afetam o processamento do texto. Exceto pelo caractere de espaço, o restante é composto por caracteres imprimíveis.

A Figura~\ref{fig:ascii} exibe a tabela ASCII.

\begin{figure}[!ht]
\centering
\subfigure{
\includegraphics[width=0.3\textwidth]{imagens/ascii-1.png}
}
\subfigure{
\includegraphics[width=0.3\textwidth]{imagens/ascii-2.png}
}
\subfigure{
\includegraphics[width=0.3\textwidth]{imagens/ascii-3.png}
}
\caption{Tabela ASCII}
\label{fig:ascii}
\end{figure}

A linguagem C provê um atalho para que você não tenha que recorrer à tabela ASCII sempre que precisar do valor de um caractere: para obter o valor de um caractere qualquer, basta colocá-lo entre aspas simples. Isto é, para verificar se um caracter \lstinline{c} é uma letra maiúscula, por exemplo, basta efetuar o teste \lstinline{if(c >= 'A' && c <= 'Z')}.

### *{Outras representações}

As representações EBCDIC (\textit{Extended Binary Coded Decimal Interchange Code}) e Unicode também mapeiam os caracteres em números de 8 e 16 bits, respectivamente.

EBCDIC é utilizado principalmente em \textit{mainframes} IBM. O padrão Unicode foi criado para acomodar alfabetos com mais de 256 caracteres.



## {Exercícios}
\begin{exercicio}
Escreva um programa que leia 10 caracteres e os imprima na ordem inversa àquela em que foram digitados.
\end{exercicio}


\begin{exercicio}
Escreva um programa que leia 10 caracteres e os imprima na ordem inversa àquela em que foram digitados, trocando maiúsculas por minúsculas e vice-versa.
\end{exercicio}

\begin{exercicio}
Escreva seu nome na codificação ASCII.
\end{exercicio}

## {Laboratório}
\begin{lab}
Escreva um programa que leia 100 caracteres ou até que \lstinline|'#'| seja digitado e os imprima na ordem inversa àquela em que foram digitados.
\end{lab}

\begin{lab}
Escreva um programa que leia e imprima \textit{strings} até que o usuário digite a palavra 'fim'. Considere que cada \textit{string} não possui espaços.
\end{lab}

\begin{lab}
Escreva um programa que leia e imprima \textit{strings} até que o usuário digite a palavra 'fim'. As \textit{strings} podem conter espaços.
\end{lab}


\begin{lab}
Acompanhe as atividades a seguir:

Execute o seguinte programa e observe o que será impresso. Atente para as atribuições!
\begin{lstlisting}
#include<iostream>

using namespace std;

int main()
{
  int a;
  char c;
  for(a = 65; a < 91; a++)
  {
    c = a;
    cout << c << endl;
  }
  return 0;
}
\end{lstlisting}

Você deve ter observado que os números não foram impressos, e sim as letras de 'A' a 'Z'. Olhe a tabela na Figura \ref{fig:ascii} e descubra o porquê.
\end{lab}

\begin{lab}
Modifique o programa a seguir para imprimir as letras de 'a' a 'z', ou seja, as letras minúsculas do alfabeto inglês.
\end{lab}

\begin{lab}
Agora faça um programa que leia caracteres informados pelo usuário enquanto ele não pressionar a tecla ESC. Para cada caractere informado pelo usuário, escreva o número correspondente na tabela ASCII.
\end{lab}

\begin{lab}
Modifique o programa anterior para que solicite que o usuário entre com letras minúsculas de 'a' a 'z' e imprima na tela, para cada letra, a maiúscula correspondente.
\end{lab}



## {Vetores de Caracteres como \textit{Strings}}

Um vetor de caracteres é essencialmente uma palavra ou uma frase. Assim, durante a leitura de um vetor de caracteres dificilmente sabe-se quantos caracteres serão digitados pelo usuário, por exemplo, quando deseja-se ler o nome de um indivíduo. Por este motivo, a maioria das linguagem de programação fornece métodos especiais de leitura, impressão e manipulação desses vetores de caracteres, ou como chamaremos agora, \textit{strings}.

Na linguagem C++, os comandos \lstinline|cout| e \lstinline|cin| permitem imprimir e ler \textit{strings} de maneira direta:

\begin{lstlisting}
#include<iostream>

using namespace std;

#define TAMANHO 100

int main()
{
  char nome[TAMANHO];
  
  cout << "Digite ate " << TAMANHO << " caracteres. Para terminar pressione ENTER:";

  cin >> nome;
  cout << "Os caracteres digitados foram: " << nome << endl;
  
  return 0;
}
\end{lstlisting}

Entretanto, o comando \lstinline|cin|, não permite, da forma como vimos até agora, a leitura de uma \textit{string} que contenha espaços (uma frase, por exemplo). Para que isso seja possível precisamos utilizar a função \lstinline|cin.getline()|. Esta função necessita de dois argumentos: o vetor de caracteres representando a \textit{string} e o tamanho máximo de caracteres que será lido. A leitura é realizada até que seja atingido ou número máximo de caracteres ou o usuário pressione a tecla ENTER. A seguir uma modificação do exemplo anterior:

\begin{lstlisting}
#include<iostream>

using namespace std;

#define TAMANHO 100

int main()
{
  char nome[TAMANHO];
  
  cout << "Digite seu nome completo. Para terminar pressione ENTER:";

  cin.getline(nome, TAMANHO);
  cout << "Seu nome eh: " << nome << endl;
  
  return 0;
}
\end{lstlisting}

Por último, é importante entender que para marcar no vetor de caracteres até onde foi feita a leitura a linguagem C adiciona o caractere especial \lstinline{'\0'} após o último caractere digitado pelo usuário. Desta forma, quando se deseja percorrer uma string, diferentemente de um vetor número, define-se como condição de parada a posição em que se encontra o \lstinline{'\0'} e não o fim do vetor.

## {Laboratório}
\begin{lab}
Faça um programa que leia uma string e calcule e imprima o tamanho desta string em uma função auxiliar.
\end{lab}

\begin{lab}
Faça um programa que leia uma string e verifique se a string lida é uma palíndrome. A verificação deve ser feita em uma função auxiliar, que deve retornar \lstinline{true} em caso afirmativo ou \lstinline{false} caso contrário.
\end{lab}

\begin{lab}
Faça um programa que leia uma string e a imprima de trás para frente, trocando as vogais pelo caractere '*'.
\end{lab}

\begin{lab}
Faça um programa que leia duas strings e concatene a segunda na primeira, separadas por um espaço em branco. A concatenação deve ser feita em uma função auxiliar.
\end{lab}


## {Funções para manipulação \textit{Strings}}

Quando trabalhamos com \textit{strings} é muito comum a realização de algumas tarefas como descobrir
o tamanho da palavra digitada pelo usuário, comparar duas palavras para saber a ordem, ou ainda,
concatenar duas palavras em uma única.

Para isso, a biblioteca \texttt{string.h} fornece algumas funções prontas, como pode ser visto na
tabela \ref{tab:string_func}
\begin{table}[!ht]
  \centering
  \begin{tabular}{l|l}
    Função & Descrição \\\hline
    strlen & retorna o tamanho (em caracteres) da palavra passada como argumento.\\
    strcpy & copia o conteúdo da segunda \textit{string} para a primeira.\\
    strcat & concatena o texto da segunda \textit{string} na primeira.\\
    strcmp & compara duas \textit{strings} (vide exemplo a seguir).\\
    stricmp & compara duas \textit{strings} sem diferenciar maiúsculas e minúsculas.\\
    atoi & converte uma \textit{string} para o inteiro correspondente.\\
    atof & converte uma \textit{string} para o número real correspondente.\\\hline
  \end{tabular}
  \caption{Algumas funções para trabalhar com \textit{strings}.}
  \label{tab:string_func}
\end{table}

O exemplo a seguir mostra a utilização destas funções:

\begin{lstlisting}
  #include<string.h>
  #include<iostream>

  using namespace std;

  int main()
  {
    char str1[50], str2[50];
    int i;
    float f;

    cout << ``Entre primeiro nome:'';
    cin >> str1;
    cout << ``Entre ultimo nome:'';
    cin >> str2;
    strcat(str1, `` ''); //junto espaco com str1
    strcat(str1, str2);
    cout << ``Seu nome completo eh '' << str1 << endl;
    cout << ``Ele possui '' << strlen(str1) << `` caracteres.'' << endl;
    
    cout << ``Entre outro nome:''.
    cin >> str2;

    //comparacao de strings
    if(strcmp(str1, str2) == 0)
    {
      cout << ``os dois nomes sao iguais.'' << endl;
    }
    else if(strcmp(str1, str2) < 0)
    {
      cout << str1 << `` vem antes de'' << str2 << endl;
    }
    else
    {
      cout << str2 << `` vem antes de '' << str1 << endl;
    }
    return 0;
  }
\end{lstlisting}

No uso destas funções, é importante manter-se em mente que o espaço adequado deve ser alocado para a string resultante das operações. Por exemplo, ao se concatenar duas strings de no máximo 100 caracteres, o resultado terá, no máximo, 200 caracteres.


## {Funções com vetores como parâmetros}
As funções descritas acima recebem strings como parâmetros. Agora, veremos como definir suas funções próprias funções que recebem não somente strings, mas vetores de outros tipos de dados.

A declaração de uma variável do tipo vetor segue, como já visto, a seguinte forma.

\begin{verbatim}
tipo identificador[tamanho];
\end{verbatim}

A declaração de parâmetros segue uma sintaxe parecida, no qual o tamanho do vetor não aparece
\begin{verbatim}
tipo identificador[]
\end{verbatim}
Isto ocorre por que, para que a função seja genérica e opere em qualquer vetor passado, o parâmetro não pode ser especificado em código. Assim, a declaração de uma função que recebe um vetor como parâmetro segue a seguinte receita:

\begin{verbatim}
tipo identificadorDaFuncao(tipo identificador1[], int tamanho1, ...)
{
    Corpo da Funcao
}
\end{verbatim}

Por exemplo, veja como definir uma função que transforme todos os caracteres de uma string para letras maíusculas.


\begin{lstlisting}
  #include<string.h>
  #include<iostream>

  using namespace std;

  void maiusculas(char str[], int tam)
  {
     for(int i = 0; i < tam && i < strlen(str); i++)
     if(str[i] >= 'a' && str[i] <= 'z')
     	str[i] = str[i] - 'a' + 'A';
  }

  int main()
  {
    char str[50];
    cout << ``Digite seu primeiro nome:'';
    cin >> str;
    
    maiusculas(str, 50)
    
    cout << str << endl;
    return 0;
  }
\end{lstlisting}

Observe que a função \textbf{altera} a string passada como parâmetro, um comportamento diferente do que aconteceu quando uma variável que não é um vetor é passada. Este comportamento será estudado mais a fundo em capítulos posteriores.



Da mesma forma que uma string, um vetor de outro tipo de dados pode ser passado como parâmetro. A função a seguir, por exemplo, calcula qual o maior inteiro em um vetor de inteiros.

\begin{lstlisting}
  #include<iostream>

  using namespace std;

  int maior(int v[], int tam)
  {
     int maior = -1;
     for(int i = 0; i < tam ; i++)
        if(v[i] > maior)
            maior = v[i];
            
     return maior;
  }
\end{lstlisting}


## {Laboratório}


\begin{lab} 
Faça um programa que dado uma string, retorne 1 se ela for palíndromo e 0 se ela não for palíndromo. Lembrando que um palíndromo é uma palavra que tenha a propriedade de poder ser lida tanto da direita para a esquerda como da esquerda para a direita. Deve-se obrigatoriamente utilizar uma \texttt{string} auxiliar e a função \texttt{strcmp} para fazer a resolução.

Ex: SUBI NO ONIBUS\\ ARARA \\ANOTARAM A DATA DA MARATONA
\end{lab}

\begin{lab} 
Faça um programa que troque todas as ocorrências de uma letra L1 pela letra L2 em uma \textit{string}. A \textit{string} e as letras L1 e L2 devem ser fornecidas pelo usuário.
\end{lab}

\begin{lab} 
Faça um programa que leia 3 \textit{strings} e as imprima em ordem alfabética.
\end{lab}

\begin{lab} 
Faça um programa com uma função que receba um vetor de inteiros e um inteiro X, e que retorne como resultado o maior inteiro do vetor que é menor que o inteiro X.
\end{lab}

\begin{lab} 
Usando a resposta do problema anterior, faça um programa com uma função que receba dois vetores de inteiros, e que faça com que o segundo torne-se uma cópia do primeiro, ordenado de forma decrescente.
\end{lab}

\chapter{Bits, bytes e bases numéricas}

Até agora temos trabalhado essencialmente com os tipos numéricos, inteiros e reais, e booleanos. Para que possamos usar outros tipos, é essencial que antes entendamos como os dados são representados na memória do computador.

## {Bit \& Byte}
Como dito anteriormente, a memória do computador pode ser entendida como uma grande planilha eletrônica, podendo cada célula ser endereçada (atribuída, lida, nomeada) individualmente. Na memória do computador não existem números ou caracteres, mas várias ``lampâdas'' que podem estar ligadas ou desligadas. Nós humanos atribuímos significado a tais estados como sendo 0's e 1's. Cada posição da memória, que pode armazenar 0 ou 1, é denominado um \emph{bit}. Por serem mínimos, normalmente trabalhamos com conjuntos de 8 bits por vez, o que denominamos \emph{bytes}.


### {Base Binária}
Os bits de um byte podem assumir todas as combinações de ligado e desligado (0 e 1). Dado um contexto, cada combinação corresponde a um certo valor. Por exemplo, se estiver usando um byte para representar números inteiros, então provavelmente a correspondência na Tabela~\ref{tab:bindec} se aplica.

\begin{table}
\caption{Exemplos de valores em binário e decimal correspondente.}
\centering
\begin{tabular}{c|r}
\hline
bits & Número\\
\hline
00000000 & 0\\
00000001 & 1\\
00000010 & 2\\
00000011 & 3\\
00000100 & 4\\
00000101 & 5\\
00000110 & 6\\
00000111 & 7\\
00001000 & 8\\
00001001 & 9\\
00001010 & 10\\
\ldots\\
11111101 & 253\\
11111110 & 254\\
11111111 & 255\\
00000000 & 0\\
\ldots\\
\end{tabular}
\label{tab:bindec}
\end{table}

Talvez isso seja novidade para você, mas você representa números na base decimal usando 10 dígitos (de 0 a 9). 
Contudo, outras bases existem. Como os bits só possuem dois estados, é natural na computação usar a base binária, que usa 2 dígitos (0 e 1). Os valores à esquerda na tabela podem ser entendidos como números nesta base.\footnote{sempre que não for colocada a base, considera-se a base 10, mais natural aos seres de vida baseada em carbono do nosso planeta, A.K.A., você.}

Para conseguir converter números de uma base para a outra, basta entender o que exatamente significa a representação de um número em uma base genérica X. Nesta base, $ABCD_X$ significa $A*X^3 + B*X^2 + C*X^1 + D*X^0$. O número $1234_{10}$, por exemplo, significa $1*X^3 + 2*X^2 + 3*X^1 + 4*X^0 = 1*1000 + 2 * 100 + 3*10 + 4*1$ que é igual a, tá dá, $1234_{10}$.
Para um exemplo mais interessante, o número $10101010_2 = 1*2^7 + 0*2^6 + 1*2^5 + 0*2^4 + 1*2^3 + 0*2^2 + 1*2^1 + 0*2^0 = 128+0+32+8+2 = 170$.

Observe que, pela tabela, o maior número que se pode representar com 8 bits é $11111111_2 = 255_{10}$. Via de regra, com X bits pode se representar $2^X$ na base binária, de 0 a $2^X-1$.

### {Base Hexadecimal}
Embora se possa usar qualquer base numérica, as que fazem mais sentido no mundo computacional são as binária e hexadecimal.
A base hexadecimal usa 16 dígitos em cada posição representando valores de 0 a 15. Para isto, usa os valores de 0 a 9 iguais aos da base decimal e também as letras de A a F representado os valores de 10 a 15.
Por exemplo, o número 1A2F$_{16}$ equivale a $1*16^3 + 10*16^2 + 2*16^1 + 15*16^0 = 4096 + 2560 + 32 + 15 = 6703$.

## {Conversão entre bases numéricas}
Enquanto nós trabalhamos com base decimal, o computador armazena informação e realiza operações na base binária. Por isso, a todo momento ocorre a conversão entre um decimal que informamos como entrada em um programa, por exemplo, para a base binária (para efetuar o cálculo), bem como da base binária (resultado do cálculo) para a base decimal exibida na tela.

### *{Conversão de Binário para Decimal}

A conversão de binário (e qualquer outra base) para decimal pode ser feita facilmente usando a notação da base genérica apresentada acima. Isto é, para realizar a conversão basta multiplicar o valor de cada posição pelo seu peso (base elevada à posição). 
Por exemplo, o número $1111011_2$ equivale a $1*2^6 + 1*2^5 + 1*2^4 + 1*2^3 + 0*2^2 + 1*2^1 + 1*2^0 = 64 + 32 + 16 + 8 + 0 + 2 + 1 = 123_{10}$.

### *{Conversão de Decimal para Binário}

A conversão de decimal para binário é feita realizando-se divisões sucessivas pela base de interesse (2, no nosso caso) até que o resultado seja zero. Os restos das divisões, na ordem inversa, correspondem ao número convertido.

Por exemplo, considere a conversão do número 169 para a base binária. O processo de conversão é o seguinte:\\
$169 / 2 = 84, Resto = 1$\\
$84 / 2 = 42, Resto = 0$\\
$42 / 2 = 21, Resto = 0$\\
$21 / 2 = 10, Resto = 1$\\
$10 / 2 = 5, Resto = 0$\\
$5 / 2 = 2, Resto = 1$\\
$2 / 2 = 1, Resto = 0$\\
$1 / 2 = 0, Resto = 1$\\
O número binário equivalente é, portanto, $10101001_2$.

### *{Conversão entre Binário e Hexadecimal}
Sabendo-se que com 4 bits é possível representar até 16 números (de 0 a 15) e que a base hexadecimal tem exatamente 16 dígitos, concluímos que é possível representar cada dígito hexadecimal com 4 dígitos binários. Sendo assim, a conversão binário/hexadecimal pode ser feita facilmente substituindo conjuntos de 4 bits binários por um dígito hexadecimal e vice-versa.

Por exemplo, para convertermos $11101010_2$ convertemos $1110_2$ para E$_{16}$ e $1010_2$ para A$_{16}$, obtendo o número EA$_{16}$. Na direção inversa, para convertermos o número 7B$_{16}$ para binário convertemos 7$_{16}$ para $0111_2$ e B$_{16}$ para $1011_2$, obtendo o número $01111011_2$.

\begin{table}
\caption{Exemplos de valores em binário, decimal e hexadecimal correspondentes.}
\centering
\begin{tabular}{c|r|r}
\hline
Binário & Decimal & Hexadecimal\\
\hline
00000000 & 0 & 0\\
00000001 & 1 & 1\\
00000010 & 2 & 2\\
00000011 & 3 & 3\\
00000100 & 4 & 4\\
00000101 & 5 & 5\\
00000110 & 6 & 6\\
00000111 & 7 & 7\\
00001000 & 8 & 8\\
00001001 & 9 & 9\\
00001010 & 10 & A\\
00001011 & 11 & B\\
00001100 & 12 & C\\
00001101 & 13 & D\\
00001110 & 14 & E\\
00001111 & 15 & F\\
00010000 & 16 & 10\\
\ldots\\
11111101 & 253 & FD\\
11111110 & 254 & FE\\
11111111 & 255 & FF\\
00000000 & 0  & 0\\
\ldots\\
\end{tabular}
\label{tab:bindechex}
\end{table}


## {Tipos Numéricos Inteiros}

Na linguagem C, os principais tipos, a quantidade de bits utilizada para sua representação e o intervalo de valores aceitos são resumidos na tabela a seguir: \footnote{A quantidade de bits pode variar de acordo com o compilador e a arquitetura do sistema}

\begin{table}[h!]
\caption{Intervalo de representação dos tipos numéricos inteiros.}
\centering
\begin{tabular}{l|c|c}
\hline
Tipo & Quantidade de Bits & Intervalo\\
\hline
char & 8 & -128 a 127\\
unsigned char & 8 & 0 a 255\\
int & 16 & -32.768 a 32.767\\
unsigned int & 16 & 0 a 65.535\\
long & 32 & -2.147.483.648 a 2.147.483.647\\
unsignet long & 32 & 0 a 4.294.967.295\\
\end{tabular}
\end{table}

Observe que o tipo caractere também é armazenado internamente como um número inteiro de 8 bits.
Com 8 bits podemos representar $2^8$ números. Se considerarmos números sem sinal (\textit{unsigned}) teremos de 0 a 255; se considerarmos números com sinal, teremos metade para positivos e metade para negativos, ou seja, de -128 a 127. O mesmo raciocínio se aplica para os outros tipos de dados da tabela.

A partir desta tabela podemos observar a importância da escolha adequada do tipo correto de acordo com sua aplicação. Se utilizarmos um inteiro para somarmos 20.000 e 50.000, por exemplo, o resultado será inesperado, uma vez que o maior valor que um inteiro aceita é 32.767. Quando isto ocorre, dizemos que houve um \textit{overflow}.

### {Números Binários Negativos}

Os exemplos que vimos até agora de conversão não contemplam números negativos. Na base decimal, o sinal de menos (-) antes do valor do número tem a finalidade de representar números negativos.

Como a memória do computador armazena apenas 0's e 1's, uma possível estratégia é ``desperdiçar'' um dos bits do número para o sinal. Adota-se, por padrão, o zero para representar um número positivo e o um para negativo. O bit do sinal é armazenado na posição mais à esquerda.

Para representar o valor de um número negativo há duas principais abordagens: \textbf{sinal-magnitude} e \textbf{complemento de 2}.

Na representação \textbf{sinal-magnitude}, o número negativo tem seu valor absoluto (magnitude) representado da mesma forma que um número positivo e o bit mais significativo, que representa o sinal, será igual a um. A tabela a seguir mostra alguns exemplos de números na base decimal e na representação sinal-magnitude.

\begin{table}[!ht]
\caption{Exemplos de valores na representação sinal-magnitude.}
\centering
\begin{tabular}{c|c}
\hline
Decimal & Binário Sinal-Magnitude\\
\hline
+20 & \textbf{0}0010100\\
-20 & \textbf{1}0010100\\
+115 & \textbf{0}1110011\\
-115 & \textbf{1}1110011\\
\end{tabular}
\end{table}

Com 8 bits, temos, então números de $11111111_2$ a $01111111_2$ (-127 a +127). Um problema que aparece com esta representação é o zero. Qual a representação correta, $00000000$ ou $10000000$? E por que precisaríamos de duas representações?

A representação \textbf{complemento de 2} utiliza uma maneira um pouco diferente de representar números negativos. Para expressá-los devemos inverter cada bit do número positivo e somar 1 ao resultado. Por exemplo, o número -15 é representado em complemento de 2 com 5 bits como 10001, ou seja, calcula-se o valor de +15 = $01111_2$, e, em seguida invertemos e somamos 1: $10000_2 + 1_2 = 10001_2$. Se a representação usar 8 bits, então $15_{10} = 00001111_{2}$ e $-15_{10} = 11110001_{2}$.


## {Aritmética Inteira Binária}
Aritmética binária é tão simples como $1 + 1 = 10$. Sério, é assim que se faz: $0 + 0 = 0, 0+1 = 1+0 = 1, 1 + 1 = 10_2$. Logo, em sistemas computacionais as somas e subtrações geralmente são realizadas aos pares, da mesma forma que na base binária.

### {Números positivos}
A \textbf{adição} de números positivos é muito simples. Para fazê-la, basta somar os valores na mesma posição, do menos significativo para o mais significativo. O ``vai-um'' funciona da mesma forma como fazemos na base decimal. Por exemplo, para somarmos 5 e 9, fazemos:
\begin{verbatim}
  1
0101 +
1001
----
1110
\end{verbatim}
Como a quantidade de bits para determinado tipo de dados é limitado, durante uma soma pode ocorrer de o resultado ultrapassar o maior valor permitido para aquela quantidade de bits, quando isto ocorre, temos um \emph{overflow} (derramamento). Considere a soma de 7 e 9, ambos com 4 bits.
\begin{verbatim}
1 111
  0111 +
  1001
  ----
1 0000  <-- overflow!
\end{verbatim}

Houve um ``vai-um'' além do bit mais significativo, caracterizando um \textit{overflow}. Neste caso, o resultado da operação está errado.

### {Números em Complemento de 2}
Como vimos anteriormente, o computador usa duas principais representações para números negativos. A representação complemento de 2 é a mais utilizada porque permite que a soma de números negativos seja feita da mesma maneira que a soma de números positivos. Por exemplo considere as soma de -2 + 5 e -1+(-1), em complemento de 2:
\begin{verbatim}
    1 1
(-2)  1110 +
(+5)  0101
      ----
    1 0011  <-- Não é overflow! Esse "vai-um" deve ser desprezado!
    
    1 111
(-1)  1111 +
(-1)  1111
      ----
    1 1110  <-- Não é overflow! Esse "vai-um" deve ser desprezado!

\end{verbatim}
Observe que nestes exemplos tivemos um ``vai-um'' além do bit mais significativo. Em soma de números em complemento de 2 isto não é suficiente para caracterizar um \textit{overflow}. Um \emph{overflow} apenas ocorrerá quando, ao somarmos dois números de mesmo sinal, obtivermos um número de sinal diferente. Desta maneira, no exemplo apresentado, este ``vai-um'' a mais deve simplesmente ser ignorado.

Já os exemplos a seguir mostram operações problemáticas.
\begin{verbatim}
      111
(+7)  0111 +
(+7)  0111
      ----
      1110  <-- O resultado começa com 1, logo é negativo. Absurdo!

    1 
(-3)  1101 +
(-6)  1010
      ----
    1 0111  <-- O resultado começa com 0, logo é positivo. Absurdo!
\end{verbatim}

### {E a subtração?}
Na verdade, a maioria dos computadores não sabe fazer subtração. O que eles fazem é utilizar um truque para transformar uma subtração em uma soma.

Por exemplo, a operação $7 - 5$ pode ser reescrita como $7 + (-5)$, ou seja, para realizar a subtração basta inverter o segundo número (em complemento de 2) e somá-lo ao primeiro da maneira usual.

## {Tipos Numéricos Reais}
Para representarmos números reais no computador, definimos que uma quantidade de bits do número será usada para representar a mantissa e o restante o expoente do número. Por exemplo, se dispusermos de 8 bits, podemos definir que os quatro primeiros bits serão a mantissa e os quatro últimos serão o expoente, em notação científica. Assim, $10101010_2 = 1,0*10^{11}$ e $10111010_2 = 1,1*10^{11}$.

Antes que você saia dizendo por aí que o ideal é usar tais números pois podemos representar números tão grandes como $11111111_2 = 15*10^{15}$, que é muito mais que os $2^{16}-1$ da notação binária  convencional, pense em como representaria o número 161$_{10}$, já que a maior mantissa representável é 1,5. Além disso, como representar 1,1111, já que só dispomos de 4 dígitos na mantissa?

Além disso, se representações de números reais pecam em sua precisão, também pecam na velocidade de processamento. A aritmética de números binários é muito mais simples que a de números reais (ou de ponto flutuante, como costumamos dizer na computação). Para manipular números reais, computadores normalmente precisam de componentes dedicados a este fim e que tem alto tempo de execução.

Para saber mais sobre representações de números em pontos flutuantes visite a URL \url{http://en.wikipedia.org/wiki/Floating_point}


## {Exercícios e laboratório}

### {}
Quantos números se pode representar, na base binária, com 1, 8, 16, 32 e 64 bits?

### {}
Escreva os seguintes números nas bases binária e hexadecimal:
\begin{enumerate}
	\item 16
	\item 45
	\item 129
	\item 23
	\item 1290
\end{enumerate}

### {}
Converta os números a seguir para a base decimal:
\begin{enumerate}
	\item $16_{16}$
	\item D5$_{16}$
	\item $1100101101_2$
	\item 2C04$_{16}$
	\item $11101_2$
\end{enumerate}

### {}
Escreva os números a seguir nas representações sinal-magnitude e complemento de 2 com 8 bits:
\begin{enumerate}
	\item -19
	\item +47
	\item -29
	\item -37
	\item -105
\end{enumerate}

### {}
Realize as seguintes operações aritméticas em complemento de 2 com números de 8 bits:
\begin{enumerate}
	\item 16 - 9
	\item -45 - 7
	\item -12 + 12
\end{enumerate}

### {}

\begin{lab}
Faça um programa para descobrir quantos bits tem uma variável do tipo \lstinline{int}? E um \lstinline{unsigned int}?
\end{lab}

\begin{lab}
Escreva um programa que leia um número de 2 dígitos na base decimal e imprima o mesmo número na base binária.
\end{lab}

\begin{lab}
Escreva um programa que leia um número binário de até 10 bits e imprima o mesmo número na base decimal.
\end{lab}

%\chapter{Strings e Funções}

%Neste capítulo veremos algumas funções muito usadas na manipulação de (\textit{strings}) assim como definir suas próprias funções que recebem vetores como %parâmetros.




\chapter{Funções Úteis I}
## {Funções Matemáticas}

A biblioteca \texttt{math.h} fornece algumas funções aritméticas muito úteis no desenvolvimento de programas. A Tabela~\ref{tab:math_func} apresenta algumas destas funções.

\begin{table}[!ht]
  \centering
  \begin{tabular}{l|l}
    Função & Descrição/Exemplo \\\hline
    abs & valor absoluto do argumento. Ex: \verb|int x = abs(-9);| \\
    sin & seno do argumento (em radianos). Ex: \verb|double x = sin(3.14159);|\\
    cos & cosseno do argumento (em radianos). Ex: \verb|double x = cos(3.14159);|\\
    tan & tangente do argumento (em radianos). Ex: \verb|double x = tan(3.14159);|\\
    asin& arco cujo seno é passado como argumento. Ex: \verb|double x = asin(1);|\\
    acos& arco cujo cosseno é passado como argumento. Ex: \verb|double x = acos(1);|\\
    atan& arco cuja tangente é passada como argumento. Ex: \verb|double x = atan(sqrt(2)/2);|\\
    floor& piso do valor passado como argumento. Ex: \verb|double x = floor(3.2); //=3|\\
    ceil& teto do valor passado como argumento. Ex: \verb|double x = floor(3.2); //=4|\\
    round& arredonda o argumento para o inteiro mais próximo. Ex: \verb|double x = round(9.9); //=10|\\
    pow& eleva o primeiro argumento ao expoente no segundo. Ex: \verb|double x = pow(2,3); //=8|\\
    sqrt& retorna a raiz quadrada do argumento. Ex: \verb|double x = sqrt(169); //=13|\\
    log& retorna logaritmo natural do argumento.\\
    log10& retorna log. do argumento na base 10.\\
    log2& retornar log do argumento na base 2\\\hline
  \end{tabular}
  \caption{Algumas funções aritméticas.}
  \label{tab:math_func}
\end{table}

Além das funções em \lstinline{math.h}, duas outras funções, da biblioteca \lstinline{stdlib.h}, são particularmente interessantes na manipulação de números. Estas funções são apresentadas na Tabela~\ref{tab:rand_func}.

\begin{table}[!ht]
  \centering
  \begin{tabular}{l|l}
    Função & Descrição/Exemplo \\\hline
    rand & retorna um número aleatório (biblioteca \texttt{stdlib.h})\\
    srand& define a semente para a geração de números aleatórios por \texttt{rand} (biblioteca
    \texttt{stdlib.h})\\\hline
  \end{tabular}
  \caption{Funções para geração de números aleatórios.}
  \label{tab:rand_func}
\end{table}

A função \lstinline{rand()} é utiliza para gerar números aleatórios. Um número aleatório é gerado
internamente pelo computador aplicando-se operações aritméticas que o usuário desconhece a partir de
um valor inicial chamado de \emph{semente}. O valor dessa semente é definido com a função
\lstinline{srand()}. O exemplo a seguir imprime na tela 30 números ``aleatórios''.

\newpage

\begin{lstlisting}
#include<stdlib.h>
#include<time.h>
  . . .
int main()
{
  for (int i = 0; i < 10; i++)
  {
    cout << rand() << endl;
  }

  for (int i = 0; i < 10; i++)
  {
    cout << rand() << endl;
  }

  //Configuracao da semente
  //com valor que depende da hora atual.
  //Isto garante maior 'aleatoriedade'
  srand(time(NULL)); 
  for (int i = 0; i < 10; i++)
  {
    cout << rand() << endl;
  }
  return 0;
}
\end{lstlisting}

O codigo a seguir é para um jogo de adivinhação. O programa gera um número aleatório entre 1 e 10, e o usuário deve descobrir qual é este número\footnote{\url{http://www.cplusplus.com/reference/clibrary/cstdlib/rand/}}.

\begin{lstlisting}
/* rand example: guess the number */
#include <iostream>
#include <stdlib.h>
#include <time.h>

using namespace std;

int main ()
{
  int iSecret, iGuess;

  /* initialize random seed: */
  srand ( time(NULL) );

  /* generate secret number: */
  iSecret = rand() % 10 + 1;

  do {
    printf ("Guess the number (1 to 10): ");
    cin >> iGuess;
    if (iSecret<iGuess) puts ("The secret number is lower");
    else if (iSecret>iGuess) puts ("The secret number is higher");
  } while (iSecret!=iGuess);

  puts ("Congratulations!");
  return 0;
}
\end{lstlisting}


## {Laboratório}

\begin{lab} 
Faça um programa que leia os catetos de um triângulo e imprima o valor de sua
hipotenusa. Utiliza as funções aritméticas.
\end{lab}

\begin{lab}
O valor de $\pi$ pode ser dado pela série:

$\pi = \sum_{n=0}^{\infty} (-1)^n\frac{4}{2n+1}$

Faça uma função chamada \texttt{pi} que recebe o valor de \texttt{n} e retorna o valor calculado de
acordo com a função informada. A função principal deve ler o valor de \texttt{n}, invocar a função
\texttt{pi} e imprimir o resultado.
\end{lab}

\begin{lab}
Faça um programa que leia dois números $x$ e $y$ e calcule $log_y x$. O cálculo deve ser feito em uma função auxiliar.
\end{lab}

\begin{lab}
Faça uma função que receba como parâmetro o valor de um ângulo em graus e o número de iterações (n) e calcule o valor do cosseno hiperbólico desse ângulo usando sua respectiva série de Taylor:

$cosh(x) = \sum_{n=1}^{\infty} \frac{x^{2n}}{(2n)!}$

, onde x é o valor do ângulo em \emph{radianos}. Considerar pi = 3.141593.
\end{lab}



\chapter{Arranjos Multidimensionais}

Embora os arranjos unidimensionais sejam úteis em várias situações, eles não são suficientes para resolver todos os problemas relacionados a arranjos. Em certas situações, várias dimensões precisam ser representadas. Um exemplo simples é o problema de multiplicação de matrizes.\footnote{A bem da verdade, é possível representar qualquer matriz finita como um arranjo unidimensional, mas a complexidade é muito maior em relação ao uso de arranjos multidimensionais.}


## {Declaração e Iniciação}
Como já visto, a declaração de arranjos tem a seguinte sintaxe,
\begin{verbatim}
tipo identificador[tamanho];
\end{verbatim}

A declaração de uma variável do tipo matriz tem uma forma semelhante, apenas aumentando uma segunda dimensão ao arranjo, como a seguir.
\begin{verbatim}
tipo identificador[tamanho1][tamanho2];
\end{verbatim}

Assim, uma declaração como
\begin{lstlisting}
int matriz[10][20];
\end{lstlisting}
declara uma matriz de 10 linhas por 10 colunas, cujas células são números inteiros.

A matriz pode ser iniciada como em arranjos unidimensionais, colocando-se os valores do elemento dentro de chaves após a declaração da matriz. Os valores para cada linha devem ficar dentro de chaves próprias e são
separados por vírgula:

\begin{lstlisting}
{int matriz[2][3] = {{1, 2, 3}, {4, 5, 6}};
\end{lstlisting}

A matriz criada pode ser visualizada da seguinte maneira:
\begin{center}
  \begin{tabular}{|ccc|}
    1 & 2 & 3\\
    4 & 5 & 6
  \end{tabular}
\end{center}


### {Acesso aos elementos}
O acesso às células é feito também como em arranjos unidimensionais, exceto que ambas as coordenadas devem ser especificadas. O exemplo a seguir mostra a criação, iniciação, e impressão dos elementos de uma matriz bidimensional.

\begin{lstlisting}
#include<iostream>

#define M 5
#define N 10

using namespace std;

int main()
{
   int m[M][N];
   
   cout << "Digite o valor dos elementos de uma matriz " << M << " por " << N;
   for(int i = 0; i < M; i++)
      for(int j = 0; j < N; j++)
      {
         cout << i << "," << j;
         cin >> m[i][j];
      }
      
   cout << "A matriz lida foi a seguinte "<< endl;
   
   for(int i = 0; i < M; i++)
   {
      for(int j = 0; j < N; j++)
      {
         cout << m[i][j] << " ";
      }
   
      cout << endl;  
   }
}

\end{lstlisting}

Observe que tanto na leitura como impressão da matriz, o laço mais externo percorre as linhas. Para cada valor da variável \lstinline!i!, a variável \lstinline|j|, dentro do laço interno percorre os valores de 0 a $N-1$. Desta maneira, a matriz é lida e impressa linha a linha. 

Observe a impressão. Para que serve o comando \lstinline|cout<<endl;|?

## {Mais Dimensões}
Agora você já deve ter deduzido que para adicionar mais dimensões aos seus arranjos, basta colocar esta dimensão na declaração dos mesmos. Por exemplo, o seguinte trecho de código declara um arranjo com três dimensões, em que cada célula é um inteiro. 
\begin{lstlisting}
char matriz[100][100][100];
\end{lstlisting}

Outra forma de ver tal arranjo é como um livro com várias ``páginas'', em que cada uma é uma matriz bidimensional.


## {Multiplicação de Matrizes} 
Agora que você viu alguns exemplos de declarações de arranjos multidimensionais, vejamos alguns usos reais, como a já mencionada multiplicação de matrizes.

Sejam duas matrizes $A$ e $B$, tal que $A$ tem dimensões $m \times n$ e $B, n \times o$; então, a matriz $AB$ tem dimensões  $m\times o$, e $C_i,j = \sum_{k = 1}^{m}A_{m,n}B_{n,o}$. 

Observe que na matemática os índices começam, normalmente, em 1. Na computação, contudo, os arranjos tem seu menor índice igual a zero. Logo, o código para multiplicar as duas matrizes fica assim.

\begin{lstlisting}
int main()
{
   int soma = 0, m, n, o;
   int a[100][100], b[100][100], ab[100][100]; //m,n e 0 precisam ser menores que 100.

   //ler as dimensoes
   cout << "Quais as dimensoes das matrizes?";
   cin >> m >> n >> o;
   
   for(int i = 0; i < m; i++)
      for(int j = 0; j < n; j++)
   	     cin >> a[i][j];


   for(int j = 0; j < m; j++)
      for(int k = 0; k < n; k++)
   	     cin >> a[j][k];



   for(int i = 0 ; i < m ; i++ )
   {
      for(int j = 0 ; j < o ; j++ )
      {
         for(int k = 0 ; k < n ; k++ )
         {
            sum = sum + a[i][k] * b[k][j];
         }
 
         ab[i][j] = sum;
         sum = 0;
      }
    }
}
\end{lstlisting}

Observe que fizemos nosso código de manipulação da matriz dentro da função \lstinline!main!. Fizemos isso por que usar matrizes como parâmetro é bem mais complicado do que vetores unidimensionais. Contudo, não se aflija, pois veremos isso logo a seguir.

## {Passagem de matriz como parâmetro em funções}            

Vimos que, ao passar vetores para uma função, não era necessário especificar o número de elementos
no vetor. Em matrizes bidimensionais, não é necessário especificar o número de linhas na matriz,
apenas o número de colunas. O programa a seguir usa a função \lstinline|exibeMatriz| para exibir o conteúdo
de matrizes bidimensionais:
\begin{lstlisting}
#include <iostream>
#define ncol 10

using namespace std;

void exibeMatriz(int matriz[][ncol], int linhas)
{
  int i, j;
  for (i = 0; i < linhas; i++)
  {
    for (j = 0; j < 10; j++)
    {
      cout << matriz[i][j] << ``\t'';
    }
    cout << endl;
  }
}

int main()
{
  int a[1][10] = {{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}};

  int b[2][10] = {{1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
                 {11, 12, 13, 14, 15, 16, 17, 18, 19,20}};

  int c[3][10] = {{1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
		{11, 12, 13, 14, 15, 16, 17, 18, 19, 20},
		{21, 22, 23, 24, 25, 26, 27, 28, 29, 30}};

  exibeMatriz(a, 1);
  exibeMatriz(b, 2);
  exibeMatriz(c, 3);
  return 0;

}
\end{lstlisting}

Via de regra, não é necessário especificar a primeira dimensão da matriz. Isto é, em vetores, você não passava qualquer dimensão. Em matrizes bidimensionais, não precisa especificar a quantidade de linhas. Em uma matriz tridimensional, não precisaria especificar a quantidade de ``páginas'', e assim por diante.

Lembre-se, semelhante ao que acontece com vetores, matrizes alteradas em funções auxiliares implicam em alteração na matriz original.



## {Matrizes de Caracteres}
Da mesma forma que vetores de caracteres podem ser manipuladas de forma especial no C(++), também podem as matrizes de caractere. Na verdade, se um vetor de caracteres é o que chama-se de uma string, então uma matriz bidimensional de caracteres é, na verdade, um vetor de strings. Por exemplo,

\begin{lstlisting}
char nomes[10][20];
\end{lstlisting}
pode ser visto como um vetor de 10 strings, cada uma com 20 caracteres, e cada string pode ser manipulada como tal, como no exemplo a seguir.

\begin{lstlisting}
#include<iostream>

#define M 10
#define N 11

using namespace std;

int main()
{
   char m[M][N];
   
   cout << "Digite " << M << " palavras de no maximo " << N-1 << " caracteres" << endl;
   for(int i = 0; i < M; i++)
   {
         cout << i << ": ";
         cin >> m[i];
   }  
   
   cout << "As palavras lidas foram as seguintes "<< endl;
   
   for(int i = 0; i < M; i++)
   {
      cout << m[i] << "  (com tamanho = " << strlen(m[i]) << ")" << endl;
   }
}

\end{lstlisting}

## {Exercicios}

\begin{lab}
Escreva um programa com uma função que receba como parâmetro uma matriz bidimensional e suas dimensões, e que incremente cada elemento da matriz em 10\%.
\end{lab}

\begin{lab}
Escreva um programa que leia e \href{http://pt.wikipedia.org/wiki/Adição_de_matrizes}{some} duas matrizes, imprimindo o resultado. Utilize funções auxiliares para leitura, impressão e soma.
\end{lab}

\begin{lab}
Escreva um programa que leia uma matriz e diga se ela é a matriz \href{http://pt.wikipedia.org/wiki/Matriz_identidade}{identidade} ou não.
\end{lab}

\begin{lab}
Escreva um programa que leia uma matriz e imprima sua 
\href{http://pt.wikipedia.org/wiki/Matriz_transposta}{transposta}.
\end{lab}


\iffalse
\chapter{Arranjos Multidimensionais (II)}

## {Introdução}
Como você já percebeu, arranjos multidimensionais são muito divertidos. Neste capítulo, veremos alguns tópicos mais avançados em seu uso.



## {Matrizes Bidimensionais Como Unidimensionais e Vice-Versa}

Uma matriz bidimensional pode ser utilizada sem precisar acessar os elementos em suas posições de
linha ou coluna. Ela pode ser tratada como se tivesse uma única dimensão. O programa a seguir calcula a
soma dos valores em uma matriz bidimensional, inicialmente utilizando as duas dimensões e em seguida
da mesma forma que com vetores.

\begin{lstlisting}
#include <iostream>
#define ncol 10

using namespace std;

int somaMatrizBi(int matriz[][ncol], int linhas)
{
  int soma = 0;
  for (int i = 0; i < linhas; i++)
    for (int j = 0; j < ncol; j++)
      soma += matriz[i][j];

  return soma;
}

int somaMatrizUni(int matriz[], int elementos)
{
  int soma = 0;
  int i;
  for (i = 0; i < elementos; i++)
    soma += matriz[i];

  return soma;
}

int main()
{
  int a[10] =   {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

  int b[2][10]={{1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
               {11, 12, 13, 14, 15, 16, 17, 18, 19,20}};

  int c[3][10]={{1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
               {11, 12, 13, 14, 15, 16, 17, 18, 19, 20},
               {21, 22, 23, 24, 25, 26, 27, 28, 29,30}};

  cout << "Soma dos elementos da primeira matriz: " 
       << somaMatrizUni(a, 10);
  cout << "Soma dos elementos da primeira matriz de novo: " 
       << somaMatrizBi(a, 1);
  
  cout << "Soma dos elementos da segunda matriz: " 
       << somaMatrizUni(b, 20);
  cout << "Soma dos elementos da segunda matriz de novo: " 
       << somaMatrizBi(b, 2);
  
  cout << "Soma dos elementos da terceira matriz: " 
       << somaMatrizUni(c, 30);
  cout << "Soma dos elementos da terceira matriz de novo: " 
       << somaMatrizBi(c, 3);

  return 0;
}
\end{lstlisting}

Observe que a função \lstinline!somaMatrizUni! recebe como argumento o total de elementos e percorre a matriz da mesma forma que um vetor. Isto pode ser feito porque na memória do computador a matriz é armazenada como um vetor de \lstinline|nlinha| $\times$ \lstinline|ncolunas| elementos. A função \lstinline|somaMatrizBi| recebe o
número de linhas e faz a mesma soma utilizando as duas dimensões.

Uma vez que a matriz multidimensional pode ser acessada como unidimensional, você pode criar funções que recebam uma matriz unidimensional e passar, como parâmetro, todas as suas dimensões. Internamente a esta função, a matriz pode ser percorrida usando-se as dimensões e um pouco de aritmética básica.


\begin{lstlisting}
#include <iostream>

using namespace std;

int somaMatrizBiDisfarcadaDeUni(int matriz[], int linhas, int colunas)
{
  int soma = 0;
  for (int i = 0; i < linhas; i++)
    for (int j = 0; j < colunas; j++)
      soma += matriz[i * colunas + j];

  return soma;
}

int main()
{
  int a[10] =   {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

  int b[2][8]={{1, 2, 3, 4, 5, 6, 7, 8},
               {11, 12, 13, 14, 15, 16, 17, 18}};

  int c[3][7]={{1, 2, 3, 4, 5, 6, 7},
               {11, 12, 13, 14, 15, 16, 17},
               {21, 22, 23, 24, 25, 26, 27}};

  cout << "Soma dos elementos da primeira matriz: " 
       << somaMatrizBiDisfarcadaDeUni(a, 1, 10);
  
  cout << "Soma dos elementos da segunda matriz: " 
       << somaMatrizBiDisfarcadaDeUni(b[0], 2, 8);
  
  cout << "Soma dos elementos da terceira matriz: " 
       << somaMatrizBiDisfarcadaDeUni(c[0], 3, 7);

  return 0;
}
\end{lstlisting}

%TODO: escrever o vice-versa.

## {Exercícios}

\fi

\chapter{Ordenação de Arranjos}

## {Introdução}
Uma das aplicações mais estudadas e realizadas sobre arranjos é a \textbf{ordenação}. Ordenar um
arranjo significa permutar seus elementos de tal forma que eles fiquem em ordem crescente, ou
seja, $v[0] <= v[1] <= v[2] <= \dots{} <= v[n-1]$.  Por exemplo, suponha o vetor\\
$v = {5, 6, -9, 9, 0, 4}$. \\
Uma ordenação desse vetor resultaria em um rearranjo de seus elementos: \\
$v = {-9, 0, 4, 5, 6, 9}$.

Exitem diversos algoritmos de ordenação para vetores. Eles variam em relação à dificuldade de
implementação e desempenho. Usualmente algoritmos mais fáceis de serem implementados apresentam
desempenho inferior.  Veremos 3 algoritmos diferentes de ordenação:
\begin{enumerate}
  \item Algoritmo de Inserção (\textit{Insertion Sort});
  \item Algoritmo de Seleção (\textit{Selection Sort}); e
  \item Algoritmo de Ordenação por Troca (\textit{Bubble Sort}).
\end{enumerate}

## {Algoritmos de Ordenação}
### {Algoritmo de Inserção (\textit{Insertion Sort})}
Trata-se de um dos algoritmos de implementação mais simples. Seu método de ordenação semelhante ao
que usamos para ordenar as cartas de um baralho.  A idéia básica do algoritmo é descrita a seguir:
\begin{itemize}
  \item Compare a chave (\texttt{x}) com os elementos à sua esquerda, deslocando para direita cada elemento maior do que a chave;
  \item Insira a chave na posição correta à sua esquerda, onde os elementos já estão ordenados;
  \item Repita os passos anteriores atualizando a chave para a próxima posição à direita até o fim do vetor.
\end{itemize}
A figura \ref{fig:insertion_sort} apresenta um exemplo de uma etapa da execução do algoritmo.
\begin{figure}[ht]
  \begin{center}
    \includegraphics[width=.7\textwidth]{imagens/insercao.png}
  \end{center}
  \caption{Exemplo do algoritmo \textit{Insertion Sort}.}
  \label{fig:insertion_sort}
\end{figure}

O código a seguir implementa o algoritmo em C, considerando um vetor \texttt{v} de tamanho \texttt{n}.
\begin{lstlisting}
void insertionSort(int v[], int n)
{
  int i, j, x;
  for(i = 1; i < n; i++) 
  {
    x = v[i];
    j = i - 1;
    while(j >= 0 && v[j] > x) 
    {
      v[j+1] = v[j];
      j--;
    }
    v[j+1] = x;
  }
}
\end{lstlisting}


### {Algoritmo de Seleção (\textit{Selection Sort})}
A implementação deste método de ordenação é muito simples. A idéia básica é descrita a seguir:
\begin{itemize}
  \item Selecione o menor elemento do vetor de tamanho \texttt{n};
  \item Troque esse elemento com o elemento da primeira posição do vetor;
  \item Repita as duas operações anteriores considerando apenas os \texttt{n-1} elementos restantes, em
    seguida repita com os \texttt{n-2} elementos restantes; e assim sucessivamente até que reste apenas um
    elemento no vetor a ser considerado.
\end{itemize}
A figura \ref{fig:selection_sort} apresenta um exemplo da execução do algoritmo.
\begin{figure}[h]
  \begin{center}
    \includegraphics[width=.7\textwidth]{imagens/selecao.png}
  \end{center}
  \caption{Exemplo do algoritmo \textit{Selection Sort}.}		
  \label{fig:selection_sort}
\end{figure}

O código a seguir implementa o algoritmo em C, considerando um vetor \texttt{v} de tamanho \texttt{n}.
 \begin{lstlisting}
void selectionSort(int v[], int n)
{
  int i, j, aux, min;
  for(i = 0; i < n-1; i++) 
  {
    min = i;
    for(j = i+1; j < n; j++) 
    {
      if(v[j] < v[min]) 
      {
	min = j;
      }
    }
    aux = v[i]; v[i] = v[min]; v[min] = aux; //troca
  }
}
\end{lstlisting}

### {Algoritmo de Ordenação por Troca (\textit{Bubble Sort})}
Outro algoritmo simples, muito útil para ordenação de vetores pequenos, mas não indicado para
vetores maiores devido ao seu baixo desempenho computacional. Sua déia básica é apresentada a
seguir:
\begin{itemize}
  \item Compare o primeiro elemento com o segundo. Se estiverem desordenados, então efetue a troca
    de posição. Compare o segundo elemento com o terceiro e efetue a troca de posição, se
    necessário;
  \item Repita a operação anterior até que o penúltimo elemento seja comparado com o último. Ao
    final desta repetição o elemento de maior valor estará em sua posição correta, a n-ésima posição
    do vetor;
  \item Continue a ordenação posicionando o segundo maior elemento, o terceiro,..., até que todo o
    vetor esteja ordenado.
\end{itemize}
A figura \ref{fig:bubble_sort} apresenta um exemplo de um vetor sendo ordenado pelo algoritmo.
\begin{figure}[h]
  \begin{center}
    \includegraphics[width=.9\textwidth]{imagens/bubblesort.png}
  \end{center}
  \caption{Exemplo de ordenação usando o algoritmo \textit{Bubble Sort}.}
  \label{fig:bubble_sort}
\end{figure}

O código a seguir implementa o algoritmo em C, considerando um vetor \texttt{v} de tamanho \texttt{n}.
\begin{lstlisting}
void bubbleSort(int v[], int n)
{
  int i, j, aux;
  for(i = n-1; i > 0; i--) 
  {
    for(j = 0; j < i; j++) 
    {
      if(v[j] > v[j+1]) 
      {
	aux = v[j]; v[j] = v[j+1]; v[j+1] = aux; //troca
      }
    }
  }
}
\end{lstlisting}

## {Exercícios}
### {}
Implemente na linguagem C o algoritmo de ordenação \textit{insertion sort}. Utilize funções
auxiliares para implementar a ordenação, a leitura do vetor desordenado e a impressão do vetor
ordenado.
### {}
Implemente na linguagem C o algoritmo de ordenação \textit{selection sort}. Utilize funções
auxiliares para implementar a ordenação, a leitura do vetor desordenado e a impressão do vetor
ordenado.
### {}
Implemente na linguagem C o algoritmo de ordenação \textit{bubble sort}. Utilize funções auxiliares
para implementar a ordenação, a leitura do vetor desordenado e a impressão do vetor ordenado.



%TODO: Busca binária
%TODO: Inserção ordenada


\part{Intermediário}
\chapter{Estruturas Não-Homogêneas}

## {Introdução}
Imagine que você deseje armazenar informações sobre um funcionário de uma empresa. Entre estas informações podemos ter, por exemplo, nome, endereço, telefone, sexo, estado civil, cargo, setor e salário. 
Em um programa, isto seria representado por oito variáveis apenas para um funcionário. Se
você desejar incluir mais informações, isto implicará em mais variáveis, aumentando a complexidade do programa. 

Por esta razão, em muitas aplicações, é importante a capacidade de se tratar todas as
informações de uma entidade (uma pessoa, por exemplo), como sendo uma única unidade de
armazenamento, ou seja, uma única variável. 
Por outro lado, deve ser possível, que esta única variável permita acesso a cada informação em separado.
Outros exemplos de informação com esta característica é o endereço, que pode ser decomposto em:
logradouro, número, complemento, CEP, cidade, estado, país.

Neste tipo de informação é possível observar que, diferentemente de variáveis indexadas (vetores e matrizes), não há homogeneidade quanto ao tipo de dados tratado.  Por isso, deve haver um mecanismo para trabalhar com variáveis estruturadas heterogêneas, também conhecidas simplesmente como \textit{estruturas} ou \textit{structs}.

## {Declaração}
Na linguagem C, a palavra reservada \lstinline|struct| é destinada à declaração de variáveis não-homogêneas, e seu uso segue a seguinte sintaxe:

\begin{verbatim}
struct identificador{
	tipo_campo_1 nome_campo_1;
	...
	tipo_campo_n nome_campo_n;
};
\end{verbatim}

Em primeiro lugar, cada estrututura tem um identificador, usado na declaração de variáveis do tipo desta estrutura. Em seguida, são declarados os campos da estrutura, especificadas entre as chaves. Os campos podem ter qualquer tipo, inclusive ser outra estrutura. O exemplo a seguir declara uma estrutura para o armazenamento de endereços e várias variáveis deste tipo.

\begin{lstlisting}
struct endereco {
  char logradouro[15];
  int numero;
  char complemento[6], bairro[10];
  char cidade[10], estado[3], pais[10];
};
...
struct endereco e1, e2, e3;
\end{lstlisting}

O uso da palavra reservada \lstinline|struct| é obrigatório na declaração de variáveis, pois ela faz parte do tipo da variável. O uso repetido desta palavra reservada pode ``poluir'' o código, e por essa razão recomenda-se a definição de novos tipos baseados na estrutura.

### {\lstinline|typedef|}
A palavra chave \lstinline!typedef! permite que se defina novos tipos de dados a partir de tipos já existentes. Por exemplo, é possível definir um tipo ``numero\_real'' ou um tipo ``caractere''. A sintaxe para o uso \lstinline|typedef| é a seguinte:

\begin{verbatim}
typedef tipo_antigo tipo_novo;
\end{verbatim}

Os exemplos apenas dados são implementados assim:
\begin{lstlisting}
typedef float numero_real;
typedef char caractere;
\end{lstlisting}

Mais importante, é possível definir um tipo basedo na estrutura. Neste caso, há duas formas de fazê-lo. O exemplo a seguir mostra a mais verborrágica.

\begin{lstlisting}
struct end{
  char logradouro[15];
  int numero;
  char complemento[6], bairro[10];
  char cidade[10], estado[3], pais[10];
};
...
typedef end endereco;

endereco e1, e2, e3;
\end{lstlisting}

Embora mais explícita, esta forma não é usada normalmente, em função forma mais compacta a seguir.

\begin{lstlisting}
typedef struct{
  char logradouro[15];
  int numero;
  char complemento[6], bairro[10];
  char cidade[10], estado[3], pais[10];
} endereco;
...
endereco e1, e2, e3;
\end{lstlisting}

## {Acesso aos Campos de Uma Estrutura}
Embora as estruturas agreguem vários campos, com raras exceções, o manuseio da mesma deve ser feito campo a campo, como variáveis normais.
Para acessar um dos campos de uma estrutura, usa-se o operador '.' (ponto). Diferentemente de variáveis indexadas, variáveis do tipo estrutura podem receber o valor de outra do mesmo tipo (desde que nenhum dos campos seja vetor). Por exemplo:
\begin{lstlisting}
typedef struct st1 st1;
struct st1 {
  char l;
  int i;
  float b;
};
...
st1 s1 = {'c', -9, 4.76},       //Atribuicao na iniciacao.
    s1Copia, s2; 
s2.l = 'z';                     //Atribuicao...
s2.i = -4;                      //... campo a ...
s2.b = 0.89;                    //... campo.
s1Copia = s1;                   //Copia de valores de todos os campos.
...
\end{lstlisting}

## {Exemplo}

Considere a estrutura \texttt{complexo}, a qual representa um número imaginário na forma $a + b \times i$, em que o valor de $a$ é armazenado na variável \texttt{real} e o valor de $b$ é armazenado na variável \texttt{imag}. O exemplo a seguir apresenta uma matriz de $3 \times 3$ em que cada elemento é do tipo \texttt{complexo}.

\begin{lstlisting}
#include <iostream>

using namespace std;

typedef struct{
  float real, imag;
} complexo;

int main() {
  int i, j;
  complexo A[3][3] = {
                      { {1.0, -0.1}, {2.0, -0.2}, {2.0, -0.2} }, //real
                      { {4.0, -3.4}, {5.0, 4.1}, {6.0, -2.6} }   //imag
                     };
  for ( i= 0; i < 3; i++) {
    for (j = 0; j < 3; j++)
      cout << A[i][j].real << " + " A[i][j].imag << "*i" << \t;
    cout << endl;
  }
  return 0;
}    
\end{lstlisting}


## {Exercícios}
### {}
Faça um programa que leia informações sobre 15 pessoas. Essa informação deve ficar em um vetor de variáveis do tipo estruturado \texttt{pessoa}, o qual deve conter as seguintes informações:
\begin{itemize}
  \item Nome: string de tamanho 30;
  \item Sexo: tipo enumerativo com os valores \texttt{masc}, \texttt{fem};
  \item Idade: valor inteiro;
  \item Estado Civil: tipo enumerativo com os valores \texttt{solteiro}, \texttt{casado}, \texttt{separado}, \texttt{viúvo}.
   \item Salário: valor real.
\end{itemize}
Em seguida, imprima o número de homens, número de mulheres e informações da pessoa com maior salário.

### {}
Faça um programa que leia o nome, duas notas e número de faltas de 10 alunos. As informações desses alunos devem ser armazenadas em um vetor de variáveis do tipo estruturado \texttt{aluno}, o qual deve conter as seguintes informações de cada aluno:
      \begin{itemize}
       \item Nome: string de tamanho 30;
       \item Média: número real resultado da média das duas notas lidas;
       \item Situação: caractere representando situação, isto é, 'A' (Aprovado), se média maior ou igual a 6 e número de faltas menor que 10, e 'R' (Reprovado), caso contrário.
       \item Faltas: número de faltas (valor inteiro).
      \end{itemize}
      Por fim, devem ser impressas as informações de cada aluno.

## {Laboratório}
Primeiramente, implemente sua solução para o exercício anterior. Em seguida, implemente duas funções, que ordenem os dados das pessoas por Nome e Idade, e imprimam todos os dados na tela. Finalmente, demonstre o uso destas funções.

%TODO: usar a analogia com planilha eletronica para mostrar como estrutura é alocada na memória.

## {Estruturas e funções}
Estruturas são utilizadas em funções da mesma forma que os tipos básicos que vimos 
(\lstinline|int, float, char|, \ldots). Veja o exemplo a seguir:
\begin{lstlisting}
#include<iostream>

using namespace std;

typedef struct pessoa pessoa;
struct pessoa
{
  char nome[40];
  char sobrenome[40];
  int idade;
    float salario;
};
pessoa maisVelho(pessoa p1, pessoa p2)
{
  return p1.idade > p2.idade ? p1 : p2;
}

int main()
{
  pessoa pes1, pes2, mv;
  cout << ``entre nome, sobrenome, idade e salario da primeira pessoa: '';
  cin >> pes1.nome >> pes1.sobrenome >> pes1.idade >> pes1.salario;
  cout << ``entre nome, sobrenome, idade e salario da segunda pessoa: '';
  cin >> pes2.nome >> pes2.sobrenome >> pes2.idade >> pes2.salario;
  mv = maisVelho(pes1, pes2);
  cout << ``O mais velho eh '' << mv.nome << `` '' << mv.sobrenome << ``, com '';
  cout << mv.idade << `` anos e salario de '' << mv.salario << endl; 
  return 0;
}
\end{lstlisting}

De maneira análoga, vetores de estruturas devem ser utilizados da mesma forma que vetores dos tipos
básicos:

\begin{lstlisting}
#include<iostream>
#define T 5
using namespace std;

typedef struct pessoa pessoa;
struct pessoa
{
  char nome[40];
  char sobrenome[40];
  int idade;
  float salario;
};

void lePessoas(pessoa p[])
{
  for(int i = 0; i < T; i++)
  {
    cout << ``entre nome, sobrenome, idade e salario da pessoa '' << (i+1) << ``:'' << endl;
    cin >> p[i].nome >> p[i].sobrenome >> p[i].idade >> p[i].salario;
  }
}
	  
int maisVelho(pessoa p[])
{
  int idade = p[0].idade, posicao = 0;
  for(int i = 1; i < T; i++)
  {
    if(p[i].idade > idade)
    {
      idade = p[i].idade;
      posicao = i;
    }
  } 
  return posicao;
}
			    
int main()
{
  pessoa p[T];
  int pos;
  lePessoas(p);
  pos = maisVelho(p);
  cout << ``O mais velho eh '' << p[pos].nome << `` '' << p[pos].sobrenome << ``, com '';
  cout << p[pos].idade << `` anos e salario de '' << p[pos].salario << endl; 
  return 0;
}
\end{lstlisting}


## {Laboratório}
\begin{lab}
Considerando a estrutura:
\begin{lstlisting}
struct Ponto {
  int x;
  int y;
};
\end{lstlisting}
para representar um ponto em uma grade 2D, implemente uma função que indique se
um ponto \texttt{p} está localizado dentro ou fora de um retângulo. O retângulo é definido
por seus vértices inferior esquerdo \texttt{v1} e superior direito \texttt{v2}. A função deve retornar 1
caso o ponto esteja localizado dentro do retângulo e 0 caso contrário.
\end{lab}

\begin{lab}
  Faça um função que recebe um valor em segundos e retorna o valor equivalente para o tipo horário,
  o qual é composto por hora, minuto e segundos. Em seguida imprima os campos da estrutura
  retornada.
\end{lab}

\begin{lab}
  Crie a estrutura baralho, baseado em um “baralho tradicional” (cada carta tem seu naipe e seu
  valor). Implemente uma função que faça parte de distribuição (sorteio) de cartas para 2 jogadores,
  considerando que cada jogador irá receber 5 cartas. Exiba na tela as cartas que cada um dos
  jogadores recebeu.
\end{lab}

\begin{lab}
  Faça um programa que controla o consumo de energia dos eletrodomésticos de uma casa. Leia um
  inteiro \texttt{n} e, utilizando funções auxiliares:
  \begin{itemize}
    \item Crie e leia \texttt{n} eletrodomésticos que contém nome (máximo 15 letras), potencia (real, em kW)
      e tempo ativo por dia (real, em horas).
    \item Leia um tempo \texttt{t} (em dias), calcule e mostre o consumo total na casa e o consumo relativo
      de cada eletrodoméstico (consumo/consumo total) nesse período de tempo. Apresente este último
      dado em porcentagem.
  \end{itemize}
\end{lab}


\chapter{Referências}

O uso da analogia da memória do computador com uma planilha eletrônica nos permitiu entender como variáveis simples e também arranjos são alocados em nossos programas. Agora que já conhecemos vetores, usaremos uma analogia mais precisa para entendermos referências, ou como são mais popularmente conhecidas, os famigerados ponteiros.

## {A memória é um grande vetor}
\label{sec:referencias.intro}
A memória de um computador pode ser vista como um grande vetor de bytes. O primeiro byte é denominado byte 0, o segundo, byte 1 e assim por diante até o tamanho da memória disponível ao seu programa.

Quando em seu programa você, por exemplo, declara uma variável do tipo caractere (\lstinline|char|) com o nome \lstinline|c|, o compilador separa um byte da memória, digamos o byte 7542, e passa a chamá-lo de \lstinline|c|. Assim, toda vez que se referir à variável \lstinline|c| em seu programa, o computador sabe que está se referindo ao byte 7542. Neste caso, dizemos que o endereço da variável \lstinline|c| é 7542.

Similarmente, quando você aloca uma variável do tipo inteiro, o compilador reserva quatro bytes para você, digamos, os bytes 8012, 8013, 8014 e 8015. Tal variável tem o endereço 8012 (como os tipos tem sempre tamanho fixo, o endereço do primeiro byte mais a informação sobre o tipo da variável é suficiente para o computador determinar de onde até onde na memória cada variável fica armazenada).

Finalmente, quando você aloca um vetor de tamanho $n$ de algum tipo qualquer, o compilador reserva um espaço de tamanho $n \times t$, onde $t$ é o tamanho do tipo em questão. Se são 10 inteiros, por exemplo, então o vetor terá tamanho 40 bytes. O endereço desta variável é o endereço do primeiro byte da primeira célula. Assim, quando você, por exemplo, acessa a posição 5 de um vetor de inteiros cujo endereço é 1000, o computador faz o seguinte cálculo para determinar a posição de memória que você está acessando, sabendo que cada inteiro ocupa 4 bytes: $1000+5*4$.

## {Variáveis do Tipo Referência}
Em certas situações, o poder de se referir a posições de memória pelo seus endereços em vez de por um nome de variável é muito útil. Por exemplo, imagine que precisemos calcular uma série de estatísticas sobre os dados em um vetor. Neste caso, gostaríamos de definir uma função que analisasse o vetor e desse como resultados as várias estatísticas, como média, desvio padrão, variância, intervalo de confiança etc. Entretanto, como bem sabemos, funções em C(++) retornam um único resultado. Se, contudo, pudéssemos passar como parâmetro para a função as referências de onde gostaríamos que os resultados fossem colocados, então a função poderia colocá-los diretamente nestas posições de memória. Esse mecanismo é o que chamamos de passagem de parâmetro por referência.

Antes de se poder exercitar a passagem de parâmetros por referência, contudo, precisamos aprender a declará-las, a obter referências para posições de memória, e a usar tais referências. Estas operações são feitas pelos operadores \lstinline|*| e \lstinline|&|. A declaração de variáveis segue a seguinte sintaxe:

\begin{verbatim}
tipo  *identificador;
\end{verbatim}

Assim, para se declarar variáveis de referência para uma posições de memória que armazenam um inteiro, um caractere, e um float, você usaria as seguintes declarações:
\begin{lstlisting}
int *ref_int;
char *ref_char;
float *zabumba;
\end{lstlisting}

Observe que o \lstinline|*| é sempre considerado como ligado ao identificador e não ao tipo da variável. Assim, a linha de código
\begin{lstlisting}
int *a, b, *c;
\end{lstlisting}
declara duas referências para inteiro (\lstinline|a| e \lstinline|c|), e um inteiro (\lstinline|b|). Para se evitar confusões, sugere-se que não se declare variáveis do tipo referência e não referência em conjunto. Ou seja, a código acima deveria ser reescrito como
\begin{lstlisting}
int *a, *c;
int b;
\end{lstlisting}


O operador \lstinline|&| permite que se extraia o endereço (ou uma referência) de uma variável. No código,
\begin{lstlisting}
int *a;
int b;

a = &b;
\end{lstlisting}
\lstinline|a| recebe o endereço da variável \lstinline|b|. Logo, se \lstinline|b| está nos bytes 2012, 2013, 2014 e 2015, a variável a recebe o valor 2012. 

Aqui, gostaríamos de chamar a atenção para o seguinte fato: \emph{em raríssimas situações  é necessário saber o endereço de uma variável. Na maior parte dos casos, basta saber que uma variável tem tal endereço.}.

Finalmente, o operador \lstinline|*| também nos permite acessar o conteúdo de uma variável referenciada, em do valor da referência. No código,
\begin{lstlisting}
int *a;
int b;
int c;

a = &b;
*a = 20;
c = *a;
c++;
\end{lstlisting}
a variável \lstinline|b| termina com o valor 20, enquanto que a variável c termina com o valor 21.

## {Passagem de Referências como Parâmetros}
Variáveis do tipo referência, como outros tipos de variáveis, podem ser passadas como parâmetro em chamadas de função. A grande vantagem desta técnica, também conhecida como passagem de parâmetros por referência, é a possibilidade de modificação da memória para qual a referência foi passada. Por exemplo, analise o seguinte código.

\begin{lstlisting}
#include<iostream>
#include<cmath>

using namespace std;

void sen_cos_tan(float val, float *seno, float *cosseno, float *tangente)
{
    *seno = sin(val);
    *cosseno = cos(val);
    *tangente = tan(val);
}

int main()
{
    float v = 0, s, c, t;
    
    sen_cos_tan(v, &s, &c, &t);
    
    cout << "seno: " << s << " cosseno: " << c << " tangente: "<< t;
    
    return 0;
}
\end{lstlisting}

Esse programa calcula em uma única chamada, os valores do seno, cosseno e tangente da variável \lstinline|v|. Enquanto o feito não parece muito impressionante, pense no caso em que você precisa calcular diversas estatísticas de um vetor de números. Neste caso, devido à forte dependência do cálculo de uma estatística no cálculo de outras, esta função poderia simplificar em muito o seu código.


## {Laboratório}
\begin{lab}
Escreva um programa que contenha funções que calculam a média, variância e desvio padrão de um vetor de números reais (uma função por dado estatístico).
\end{lab}

\begin{lab}
Altere o programa do exercício anterior para que calcule as três estatísticas em uma função apenas, reaproveitado os cálculos uns dos outros.
\end{lab}

\chapter{Referências II}

Continuando com o estudo de ponteiros, vamos ver como utilizá-los para referenciar estruturas
e arranjos.

## {Ponteiros para Structs}

Se você recordar-se da anologia apresentada na seção \ref{sec:referencias.intro}, em que a memória é comparada a um grande vetor e cada tipo de dados tem um tamanho pré-definido, é fácil entender como uma estrutura é representada na memória.

Considere a seguinte estrutura e responda: qual o tamanho desta estrutura na memória do computador? 
\begin{lstlisting}
typedef struct
{
  int i;
  char c;
  float j;
} exemplo1;
\end{lstlisting}


Para responder a esta pergunta precisamos entender que uma estrutura ocupa espaço equivalente à soma do espaço ocupado por cada um de seus campos. Desta forma, o espaço total ocupado por uma variável do tipo \lstinline|exemplo1| será a soma dos tamanhos de 1 \lstinline|int|, 1 \lstinline|char| e 1
\lstinline|float|, ou seja, $4 + 1 + 4 = 9$ bytes.

Assim, e você cria uma variável \lstinline{exemplo1 v[10]}, o compilador deve reservar um espaço de $10 \times 9 = 90$ bytes.

Assim como nos referimos a variáveis dos tipos primitivos (inteiro, real, caractere) utilizando ponteiros, podemos também utilizar ponteiros para acessar uma variável do tipo \lstinline|struct| e seus campos. Veja o exemplo para a estrutura declarada anteriormente.

\begin{lstlisting}
exemplo1 a = {-5, 'z', 0.89}, b;
exemplo1 *p;
p = &a;
cout << (*p).i << endl;
p = &b;
cin >> (*p).c;
\end{lstlisting}

Este trecho mostra na linha 1 a criação de duas variáveis do tipo \lstinline|exemplo1| e na linha 2 a criação de uma variável do tipo ponteiro para \lstinline|exemplo1|. As linhas 3 e 5 atualizando o ponteiro, fazendo com que referencie as variáveis \lstinline|a| e \lstinline|b|, respectivamente.
Desta maneira, a linha 4 irá imprimir o valor de \lstinline|a.i|, enquanto a linha 6 irá ler a partir do teclado um valor para \lstinline|b.c|.

Quando usamos ponteiros e estruturas, aparece o incoveniente de termos que digitar toda vez entre parênteses a variável do tipo ponteiro (\lstinline{(*p).c}). Para simplificar a utilização de ponteiros no acesso a campos de uma estrutura, a linguagem C permite escrever esta mesma instrução de uma maneira mais fácil de digitar: \lstinline{p->c}. O código anterior pode ser reescrito como:

\begin{lstlisting}
exemplo1 a = {-5, 'z', 0.89}, b;
exemplo1 *p;
p = &a;
cout << p->i << endl;
p = &b;
cin >> p->c;
\end{lstlisting}

Por fim, a passagem de estruturas por referência em funções auxiliares é feita da mesma forma que
vimos no capítulo anterior:

\begin{lstlisting}
  void inverte_structs(exemplo1 *s1, exemplo2 *s2) {
    exemplo1 aux
    aux.i = s2->i;
    s2->i = s1->i;
    s1->i = aux.i;
    aux.c = s2->c;
    s2->c = s1->c;
    s1->c = aux.c;
    aux.j = s2->j;
    s2->j = s1->j;
    s1->j = aux.j;
  }

  int main()
  {
    exemplo1 a = {1, 'a', 1.0}, b = {2, 'b', 2.0};
    inverte_structs(&a, &b);
    cout << a.i << ", " << a.c << "," << a.j << endl;
    cout << b.i << ", " << b.c << "," << b.j << endl;
    return 0;
  }
\end{lstlisting}

A função auxiliar troca os valores de duas variáveis do tipo \lstinline|exemplo1| passadas por referência. Após a invocação da função auxiliar a partir da \lstinline|main| os valores iniciais das variáveis \lstinline|a| e \lstinline|b| serão trocados.

## {Arranjos e Ponteiros}

Até agora vimos vetores sem nenhuma relação com ponteiros. No fundo, quando criamos um vetor com a instrução \lstinline{int a[10]}, estamos dizendo ao compilador para reservar na memória espaço para 10 inteiros (40 bytes) e armazenar o endereço em que começa o vetor na variável \lstinline|a|. Em outras palavras, a variável \lstinline|a| é um \textit{ponteiro} para o primeiro elemento do vetor.

Por esta razão, a relação entre vetores e ponteiros é mais direta e mais fácil de utilizar.  Uma vez
que a variável que usamos contém o endereço do começo do vetor, um ponteiro pode receber diretamente
seu valor, sem necessidade do operador \&. Considere o exemplo a seguir:

\begin{lstlisting}
float a[10];
float *p;
p = a;
cout << "Digite 10 numeros reais: ";
for(int i = 0; i < 10; i++)
  cin >> a[i];
cout << "Num. digitados: ";
for(int i = 0; i < 10; i++)
  cout << p[i];
\end{lstlisting}

Observe a linha 3 e perceba como a atualização da referência do ponteiro \lstinline|p| para o vetor \lstinline|a| não utilizou o \&. Isto porque \lstinline|a| também é um ponteiro. A diferença entre \lstinline|p| e \lstinline|a| é que a primeira pode ter sua referência atualizada, enquanto a segunda não. A partir da linha 3, o vetor pode ser acessado tanto pela variável \lstinline|a| (linha 6) quanto pela variável \lstinline|p| (linha 9).

É por este motivo que vetores sempre são passados por referência em funções auxiliares, sem a necessidade do \& e do *.

### {Percorrendo vetores com ponteiros}
\label{ssec:referencias2-percorrendo_vetores}
Já sabemos a relação entre ponteiros e vetores. Veremos a seguir algumas maneiras diferentes de acessar os elementos de um vetor utilizando ponteiros. Considere o trecho de um programa a seguir:

\begin{lstlisting}
char str[100];
char *s;
int totalletras = 0;
s = str;
cout << "entre uma frase com letras minusculas" << endl;
cin.getline(s,100);
for(int i = 0; i < strlen(s); i++)
{
  if(s[i] >= 'a' && s[i] <= 'z')
  {
    totalletras++;
  }
}
cout << "O total de letras da frase eh " << totalletras;
\end{lstlisting}

Neste trecho utilizamos o ponteiro \lstinline|s| como o vetor \lstinline|str|, pois a partir da linha 3 ele ``aponta'' para o vetor. Este mesmo trecho pode ser reescrito:

\begin{lstlisting}
char str[100];
char *s;
int totalletras = 0;
s = str;
cout << "entre uma frase com letras minusculas" << endl;
cin.getline(s,100);
for(int i = 0; i < strlen(s); i++)
{
  if( *(s+i) >= 'a' && *(s+i) <= 'z' )
  {
    totalletras++;
  }
}
cout << "O total de letras da frase eh " << totalletras;
\end{lstlisting}

Observe a linha 9 de cada um dos dois trechos anteriores e veja a diferença na notação. Quando utilizamos ponteiro, podemos acessar um vetor pelo índice (colchetes) ou por um deslocamento sobre o valor do endereço inicial do vetor armazenado em \lstinline{s}, ou seja, a notação \lstinline{*(s+i)}, significa o caractere localizado \lstinline{i} caracteres a partir do caractere na primeira posição do vetor.

O mesmo trecho pode ser reescrito  ainda de uma terceira forma:

\begin{lstlisting}
char str[100];
char *s;
int totalletras = 0;
s = str;
cout << "entre uma frase com letras minusculas" << endl;
cin.getline(s,100);
for(int i = 0; i < strlen(str); i++) //Observe que aqui usamos str e nao s. Por que?
{
  if( *s >= 'a' && *s <= 'z' )
  {
    totalletras++;
  }
  s++;
}
cout << "O total de letras da frase eh " << totalletras;
\end{lstlisting}

Qual a diferença entre esta versão e as versões anteriores? Qual a diferença entre \lstinline{s++} e \lstinline{(*s)++}? 
Qual o valor de \lstinline|s[0]| em cada versão? 
E de \lstinline|*s|? 
E de \lstinline|str[0]|?

## {Laboratório}

\begin{lab}
Crie uma estrutura com os campos nome, idade e salario dos tipos \textit{string}, inteiro e real, respectivamente. 

Em seguida, crie uma função que receba referências para duas variáveis de tal tipo e uma variável correspondente a uma porcentagem de aumento que deve ser aplicada sobre o campo salário de cada estrutura. 
A função principal deve ler cada campo das duas variáveis e imprimir o novo salário.

Finalmente, crie uma função que recebe duas variáveis de tal tipo e que troque os valores de todos os campos das duas estruturas. A função principal deve agora imprimir as estruturas antes e depois da troca.
\end{lab}

\begin{lab}
Execute as três versões do programa da seção \ref{ssec:referencias2-percorrendo_vetores} e veja se há diferença no resultado. Responda às perguntas no final da seção. 
\end{lab}


\chapter{Alocação Dinâmica}
Por mais interessante que seja poder criar ponteiros para variáveis já existentes e passar
parâmetros por referência, o poder dos ponteiros só fica mesmo evidente quando se trabalha com
alocação dinâmica de memória.

Alocação dinâmica é a habilidade de se criar novas variáveis durante a execução do programa, sem que
elas tenham sido declaradas antes. Justamente por não terem sido declaradas antes da compilação,
estas variáveis alocadas dinamicamente não têm nomes e, assim, só podem ser acessadas por meio de
referências.

## {Alocação Dinâmica de Tipos Simples}
Existem várias formas de se alocar memória dinamicamente, todas elas via funções que retornam como
resultado uma referência para o começo da memória alocada, na forma de uma referência genérica.

A função mais simples para alocação de memória é a \lstinline|malloc|. Esta função recebe como único
parâmetro o tamanho da memória a ser alocada, em bytes. Observe o seguinte código para alguns
exemplos.

\begin{lstlisting}
char *s1;
int *i1;
float *f1;

s1 = (char *) malloc(1);
i1 = (int *) malloc(4);
f1 = (float *) malloc(4);
\end{lstlisting}

No exemplo acima você percebe que antes de cada \lstinline|malloc| há, entre parênteses, o tipo da
variável que guardará a referência. Isso é o que chamamos de \emph{casting}, e serve para
transformar a referência genérica retornada pela função para o tipo de referência da variável.
\textbf{Este \emph{casting} é obrigatório em seu código}.

Você também percebe que cada alocação especifica exatamente o tamanho do tipo para o qual estamos
alocando a memória. Isto é, 1 para caracteres e 4 para inteiros e números reais. Estes tamanhos,
contudo, podem variar de uma máquina/sistema operacional para outra, o que tornaria complicado
especificar tais tamanhos em cada invocação à \lstinline|malloc|. É por isso que a linguagem C(++)
especifica o construto \lstinline|sizeof|, que ``descobre'' o tamanho do tipo para você, conforme o
seguinte exemplo.

\begin{lstlisting}
char *s1;
int *i1;
float *f1;
double *d1;

s1 = (char *) malloc(sizeof(char));
i1 = (int *) malloc(sizeof(int));
f1 = (float *) malloc(sizeof(float));
d1 = (double *) malloc(sizeof(double));
\end{lstlisting}

## {Alocação Dinâmica de Vetores}
Como visto nos capítulos anteriores, a diferença entre referências para tipos simples e vetores é...
\textbf{nenhuma}! Isso quer dizer que podemos alocar vetores usando um código similar ao anterior,
alterando apenas a quantidade de memória alocada, como no seguinte exemplo.

\begin{lstlisting}
char *s2;
int *i2;
float *f2;
double *d2;

s2 = (char *) malloc(sizeof(char) * 100);
i2 = (int *) malloc(sizeof(int) * 10);
f2 = (float *) malloc(sizeof(float) * 6);
d2 = (double *) malloc(sizeof(double) * 8);

cin.getline(s2,100);
cout << s2;

for(int i = 0; i < 10; i++)
  cin >> i2[i];

for(int i = 0; i < 10; i++)
  cout << i2[i] << endl;


for(int i = 0; i < 6; i++)
  cin >> f2[i];

for(int i = 0; i < 6; i++)
  cout << f2[i] << endl;


for(int i = 0; i < 8; i++)
  cin >> d2[i];

for(int i = 0; i < 8; i++)
  cout << d2[i] << endl;
\end{lstlisting}


## {Liberação de memória}
Todos os exemplos mostrados até agora neste capítulo são incompletos. Isso por quê nenhum programa
que faça alocação dinâmica em C(++) pode ser completo sem que se faça a liberação da memória
alocada. Liberar ou ``desalocar'' a memória consiste simplesmente na invocação da função
\lstinline|free|, passando-se como parâmetro a referência a ser desalocada. O uso de
\lstinline|free| será exemplificado na próxima seção.


## {Alocação Dinâmica de Estruturas}
Assim como declarar uma referência para uma estrutura é tão simples quanto declarar uma referência
para um tipo primitivo(simples), alocar um vetor de estruturas dinamicamente é tão simples quanto
alocar um vetor de tipos primitivos dinamicamente. O exemplo a seguir mostra exatamente como alocar
um vetor com 10 estruturas do tipo definido.

\begin{lstlisting}
#define NUM_PESSOAS 10
typedef struct
{
  char prim_nome[20],
  char ult_nome[20],
  int idade,
  float salario,
  char regiao,
  char sexo
} pessoa_t;

int main()
{
  pessoa_t *pessoas;

  pessoas = (pessoa_t *) malloc(sizeof(pessoa) * NUM_PESSOAS);

  for(int i = 0; i < NUM_PESSOAS; i++)
  {
	  cin >> pessoas[i].prim_nome;	
	  cin >> pessoas[i].ult_nome;	
	  cin >> pessoas[i].idade;	
	  cin >> pessoas[i].salario;	
	  cin >> pessoas[i].sexo;
	  cin >> pessoas[i].regiao;
  }

  //Uso dos dados
  ...
  
  //Liberacao da memoria
  free(pessoas);
  
  return 0;
}
\end{lstlisting}

## {Exercícios}
### {}
Escreva um programa que leia um numero inteiro N, aloque dinamicamente um vetor de N inteiros, leia cada um dos N inteiros, e imprima os N inteiros na tela.

### {} 
Escreva um programa que repita o seguinte procedimento X vezes: leia um numero inteiro N, aloque dinamicamente um vetor de N carateres, leia uma palavra de N caracteres, transforme todas as maiúsculas em minúsculas e vice-versa na palara e imprima o resultado na tela. X deve ser lido no início da execução do programa.


## {Laboratório} 
### {} Implemente os exercícios acima.

### {} 
Escreva um programa que aloque um vetor de 100000 float e imprima os 10 primeiros e os 10 últimos (o lixo que estiver na memória). \footnote{Se tudo funcionar, aumente o vetor para 1000000 e assim por diante. O objetivo neste laboratório é mostrar que a quantidade de memória disponível para seu programa é limitada, e que se extrapolada, seu programa incorrerá em um erro.}



%TODO: \chapter{Vetores de Referências}
%TODO: Combinando vetores para referências para tipos simples e estruturados.


%TODO: \chapter{Alocação Dinâmica II}
%TODO: Alocação de arranjos multi-dimensionais (caso contíguo)



\chapter{Arquivos}
%\todo{Mover para 4 ou 5 capítulo. Alunos vêem mais exemplos práticos de aplicabilidade}

Muitas vezes desejamos guardar o resultado de alguma computação para consulta posterior. Imagine, por exemplo, que você fez um programa que calcula a média final e situação de toda a turma. Se o resultado deste processamento não puder ser armazenado, toda vez que for necessário consultar a situação de algum aluno, o programa deverá ser executado e todos os dados inseridos novamente. 
Para solucionar este problema, o usuário pode salvar resultados de computação em uma estrutura persistente. Esta estrutura de dados manipulada fora do ambiente do programa (memória principal) é conhecida como \textbf{arquivo}.  

Um arquivo é armazenado em um dispositivo de memória secundária (CD, DVD, disco rígido, pendrive) e pode ser lido ou escrito por um programa. Em C, um arquivo pode representar diversas coisas, como documentos, uma impressora, um teclado, ou qualquer dispositivo de entrada ou saída.  Consideraremos apenas dados  em disco, iniciando por dados na forma textual.


## {Arquivos de texto}
Nesta seção estudaremos apenas arquivos texto, ou seja, arquivos que contêm apenas caracteres e podem ser visualizados em editores de textos como Notepad, Gedit, Vim, etc.

A linguagem C++ dá suporte à utilização de arquivos por meio da biblioteca \lstinline|fstream|. Esta biblioteca fornece várias funções para manipulação de arquivos e define alguns tipos de dados para serem usados especificamente com arquivos.  O principal tipo definido nessa biblioteca que será usado é o tipo \lstinline|fstream|.  Um variável do tipo \lstinline|fstream| é capaz de identificar um arquivo no disco, direcionando-lhe todas as operações.  Essas variáveis são declaradas da seguinte
maneira:

\lstinline|fstream arq;|

### {Abertura e Fechamendo de Arquivos}
Antes que o arquivo seja manipulado, é preciso abrí-lo, o que é feito via ``função'' \lstinline|open| do arquivo. Uma vez aberto, o arquivo funciona como o \lstinline|cin|  e \lstinline|cout|, com os quais você já está acostumado a usar \lstinline|<<| e \lstinline|>>|, como no exemplo a seguir. Ao terminar o uso do arquivo, é importante fechá-lo, para garantir que tudo que, em teoria, está escrito no arquivo, realmente foi colocado no disco.

\begin{lstlisting}
#include <iostream>
#include <fstream>
using namespace std;

int main () {
  fstream arquivo;
  arquivo.open ("arquivo.txt");
  arquivo << "O que eu deveria escrever neste arquivo?" << endl;
  arquivo.close();
  return 0;
}
\end{lstlisting}

Nem sempre é possível abrir o arquivo como no exemplo, o que será explicado adiante. Para testar se o arquivo foi aberto ou não, use a função \lstinline|is_open()|. É importante que você teste se o arquivo realmente está aberto, antes de tentar usá-lo.

\begin{lstlisting}
#include <iostream>
#include <fstream>
using namespace std;

int main () {
  fstream arquivo;
  arquivo.open("arquivo.txt");
  
  if(arquivo.is_open())
  {
     arquivo << "O que eu deveria escrever neste arquivo?" << endl;
     arquivo.close();
     cout << "tudo escrito";
  }
  else
     cout << "falhou";
     
  return 0;  
}
\end{lstlisting}

Se você tentou executar o código acima, percebeu que a mensagem "falhou" foi escrita na tela. O problema é que o código abre um arquivo e escreve no mesmo, mas somente se ele já existir, o que não é o caso. Por enquanto, vá até a pasta onde está o seu projeto e crie o arquivo manualmente. Na seção seguinte veremos como criar um arquivo ``de dentro'' do programa. Já no código a seguir, veja como os dados do arquivo podem ser lidos.

\begin{lstlisting}
#include <iostream>
#include <fstream>
using namespace std;

int main () {
  fstream arquivo;
  arquivo.open ("arquivo.txt");

  if(arquivo.is_open())
  {
    cout << "yeah";
    arquivo << "Sera que isso foi escrito?" << endl;
    arquivo.close();
    
    arquivo.open ("arquivo.txt");
    char str[1000];
    arquivo.getline(str,1000);
    arquivo.close();

    cout << str;  
  }
  else
    cout << "O arquivo nao foi aberto";

  return 0;
}
\end{lstlisting}


### {Criação de Arquivos}
Para abrir um arquivo que não existe, ou seja, criar o arquivo, é necessário passar um conjunto especial de instruções para a função de abertura. Infelizmente, o único jeito de passar estas instruções é bem mais complicado do que o que vimos até agora. Veja o seguinte código, em especial a linha que abre o arquivo.

\begin{lstlisting}
#include <iostream>
#include <fstream>
using namespace std;

int main () {
  fstream arquivo;
  arquivo.open ("arquivo.txt", ios::out | ios::in | ios::trunc);

  if(arquivo.is_open())
    cout << "yeah";
  else
    cout << "nope";

  arquivo << "O que eu deveria escrever neste arquivo?" << endl;
  arquivo.close();

  arquivo.open ("arquivo.txt");
  char str[1000];
  arquivo.getline(str,1000);
  arquivo.close();

  cout << str;

  return 0;
}
\end{lstlisting}

Na frente do parâmetro com o nome do arquivo, na função \lstinline|open|, foram passadas três opções para o modo de abertura do arquivo, que especifica o tipo de operações que se intende fazer no arquivo (o caractere \lstinline-|- combina as opções passadas). Algumas das opções possíveis são:

\begin{itemize}
\item ios::in		--	 Operações de escrita.
\item ios::out 	--	 Operações de leitura.
\item ios::app	--	 Posiciona no fim do arquivo. Não pode ser reposicionado. Não pode ser usado com ios::in.
\item ios::trunc	--	 Posiciona no início do arquivo. Se o arquivo já existe, então seu conteúdo anterior é perdido.
\end{itemize}

As opções para leitura e escrita do arquivo, e somente estas, são implícitas, quando nenhuma opção é especificada. Se você quiser, pode usar apenas uma destas por questões de segurança (o arquivo pode ser lido mas não escrito, ou o arquivo pode ser aumentado mas não lido). Usando somente as opções de leitura e escrita, contudo, o arquivo não é criado caso não exista. Para que seja criado, é necessário que se especifique ou \lstinline|ios::trunc|  ou \lstinline|ios::app|, que farão com que o arquivo seja ou truncado ou que toda modificação seja adicionada ao fim do arquivo (\emph{append}).

### {Cuidados com a Formatação dos Dados}
Quando se escreve um dado em um arquivo de texto, precisa-se entender que o dado ocupa somente o espaço que você especificar. Isto é, se você escrever a sequência de caracteres ``C(++) é bom!!!'', 14 caracteres serão escritos, e pronto. Se escrever algo na linha seguinte depois resolver mudar a string acima para ``C(++) não é bom!!!'', então a divisão entre as linhas (o \lstinline|endl|) terá sido sobrescrito e as duas linhas se tornarão uma. Estes cuidados não precisam ser tomados agora, com os exemplos simples com os quais estamos lidando, mas nos próximos capitulos você terá que tomá-los. Assim, melhor que você já saiba sobre estes problemas desde agora.

\begin{lstlisting}
#include <iostream>
#include <fstream>
using namespace std;

int main () {
  fstream arquivo;
  arquivo.open ("arquivo.txt", ios::out | ios::in | ios::trunc);
  char str[1000];

  if(arquivo.is_open())
  {
        cout << "O arquivo foi aberto!";
        arquivo << "Escrevendo um numero pequeno:" << endl;
        arquivo << 10 <<endl;
        arquivo << "Numero pequeno escrito." << endl;

        cout << "Fechando o arquivo.";
        arquivo.close();

        cout << "Reabrindo o arquivo.";

        arquivo.open ("arquivo.txt");

        arquivo << "Escrevendo um numero pequeno:" << endl;
        arquivo << 10000 <<endl;

        cout << "Fechando o arquivo.";
        arquivo.close();

        cout << "Reabrindo o arquivo.";
        arquivo.open ("arquivo.txt");

        arquivo.getline(str,1000);
        cout << str;
        arquivo.getline(str,1000);
        cout << str;
        arquivo.getline(str,1000);
        cout << str;

        arquivo.close();
  }

  else
    cout << "nope";

  return 0;
}

\end{lstlisting}


## {Laboratório}
\begin{lab}
Faça um programa que leia o nome e sobrenome de 30 alunos e armazene em um arquivo, de tal forma que o arquivo tenha um aluno por linha. Abra o arquivo usando um editor de textos qualquer, como o Notepad.
\end{lab}

\begin{lab}
Faça um programa que tente abrir um arquivo e, caso não consiga, tente criá-lo e abrí-lo. Com arquivo aberto, leia um vetor A de inteiros de tamanho 20 e guarde seus valores em um arquivo, um por linha. Em seguida, reabra o arquivo e leia os elementos para o vetor B, verificando se os valores foram gravados corretamente.
\end{lab}

\begin{lab}
Faça um programa em Linguagem C que receba do usuário um arquivo, e mostre na tela quantas linhas esse arquivo possui.
\end{lab}
 
\begin{lab}
Faça um programa que receba dois arquivos do usuário, e crie um terceiro arquivo com o conteúdo dos dois primeiros juntos (o conteúdo do primeiro seguido do conteúdo do segundo).
\end{lab}
 
\begin{lab}
Desenvolver um programa em C que lê o conteúdo de um arquivo e cria um arquivo com o mesmo conteúdo, mas com todas as letras minúsculas convertidas para maiúsculas. Os nomes dos arquivos serão fornecidos, via teclado, pelo usuário. A função que converte minúscula para maiúscula é o toupper(). Ela é aplicada em cada caractere da string.
\end{lab}
 
\begin{lab}
Faça um programa no qual o usuário informa o nome do arquivo, e uma palavra, e retorne o número de vezes que aquela palavra aparece no arquivo.
\end{lab}

\chapter{Navegação dentro do arquivo}
Embora seja possível trabalhar com arquivos usando apenas as ferramentas apresentadas até agora,
alguns problemas são de difícil resolução, a não ser que extendamos nosso conhecimento.

Suponha por exemplo que você tenha o seguinte arquivo:

\begin{verbatim}
O rato roeu a roupa do
rei de Roma e a rainha
Ruinha resolveu rir-se
pois o rei que remente
suas roídas roupagens.
\end{verbatim}

Observe que todas as linhas tem o mesmo tamanho (22 caracteres) e que a palavra ``remende'' está
escrita de forma incorreta. Para corrigir esta palavra, podemos reescrever toda a frase, ou
posicionar o cursor do arquivo exatamente sobre o caractere errado e corrigi-lo. Há várias formas de
se fazer isso, como veremos agora.

## {Posicionamento no arquivo}
Como visto no capítulo anterior, operações de leitura e escrita no arquivo vão mudando a posição em
que as próximas operações serão executadas. Isto é, se considerarmos que há um cursor dentro do
arquivo, na posição em escreveremos, caso uma escrita seja feita, ou leremos, caso uma leitura seja
executada, então se lermos ou escrevermos 3 caracteres, então o cursor ``andará'' 3 caracteres. Se
quisermos colocar o cursor no fim do arquivo, podemos reabrí-lo usando \lstinline|ios::app|. Caso
queiramos colocar o cursor no começo do arquivo, podemos simplesmente reabri-lo sem especificar
qualquer opção ou usando \lstinline|ios::trunc| (e com isso também zerarmos nosso arquivo). 

Caso precisemos posicionar o cursor no meio do arquivo, podemos usar a função \lstinline|seekg|, que
pode ser usada duas formas:

\begin{verbatim}
seekg(nova posição [em bytes])

seekg(diferença [em bytes] em relação ao marco, marco)
\end{verbatim}

Na primeira forma você pode especificar onde o cursor deve ser posicionado em relação ao início do
arquivo, em número de bytes. Por exemplo, \lstinline|arq.seekg(10)| posiciona o cursor no décimo
byte do arquivo \lstinline|arq|. Já pela segunda forma, você especifica onde posicionar o cursor em
relação a um marco no arquivo, que pode ser seu início (\lstinline|ios_base::beg|), fim
(\lstinline|ios_base::end|), ou posição atual (\lstinline|ios_base::cur|). A diferença em relação ao
marco é especificada como um inteiro com sinal. Por exemplo,
\lstinline|arq.seekg(-10,ios_base::end)| posiciona o cursor no décimo caractere \emph{antes do fim}
do arquivo \lstinline|arq|.

Para resolver o problema apresentado acima, podemos então usar as seguintes soluções.

\begin{lstlisting}
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    fstream arq;
    arq.open("arquivo.txt"); //Posicionando o cursor no inicio.
    arq.seekg(23*3+20);
    arq << 'd';
    arq.close();


    arq.open("arquivo.txt"); //Buscando a partir do fim.
    arq.seekg(-23-3, ios_base::end);
    arq << 'd';
    arq.close();

    arq.open("arquivo.txt", ios::out | ios::trunc); //Recriando o arquivo.
    arq << "O rato roeu a roupa do" << endl
        << "rei de Roma e a rainha" << endl
        << "Ruinha resolveu rir-se" << endl
        << "pois o rei que remende" << endl
        << "suas roidas roupagens.";
    arq.close();

    return 0;

}
"
\end{lstlisting}

## {Arquivos formatados}
Para que se possa movimentar o cursor dentro de um arquivo, é importante que se conheça a estrutura
do mesmo, principalmente se pretender sobrescrevê-lo sem destruí-lo. Por exemplo, considere o
seguinte problema.

Escrever um programa que leia matrícula e nome de alunos do curso de Engenharia Química e armazene
estas informações em um arquivo. Em seguida, seu programa deve escrever todas as informações na
tela, precedidas por um número identificando cada aluno. Finalmente, o programa deve ler números
correspondentes a alunos e sobrescrever os dados do aluno com novas informações.

\begin{lstlisting}
#include <iostream>
#include <fstream>

#define NOME_ARQ "arquivo.txt"

using namespace std;


bool mais_info()
{
    char resp = 'x';
    cout << "Entrar com mais informacoes? (s/n)";

    while(true)
    {
        cin >> resp;

        switch(resp)
        {
        case 's':
        case 'S':
            return true;
        case 'n':
        case 'N':
            return false;
        }
    }
}

void ler_aluno(char mat[], int tmat, char nome[], int tnome)
{
    cin.ignore(1000,'\n');
    cin.clear();
    cout << "Digite a matricula (max " << tmat-1 << " caracteres:)";
    cin.getline(mat,tmat);
    cout << "Digite o nome (max " << tnome-1 << " caracteres";
    cin.getline(nome,tnome);
}

int main()
{
    fstream arq;

    int totalcount = 0;
    int count;
    char linha[1000];

    char mat[15];
    char nome[100];

    arq.open(NOME_ARQ);
    if(! arq.is_open())
        arq.open(NOME_ARQ, ios::in | ios::out | ios::trunc);


    while(mais_info())
    {
        ler_aluno(mat, 15, nome, 100);
        arq << mat << " " << nome << endl;
    }

    count = 1;
    arq.clear();
    arq.seekg(0);

    cout << "Dados atuais" << endl;
    while(arq.getline(linha,1000))
    {

        cout << count++ << " - "<< linha << endl;
        totalcount++;
    }

    while(mais_info())
    {
        cout << "Sobrescrever qual linha?";
        cin >> count;
        if(count > totalcount)
        {
            cout << "Linha nao existente";
        }
        else
        {
            ler_aluno(mat, 15, nome, 100);

            arq.clear();
            arq.seekg(0);
            while(count > 1)
            {
                arq.getline(linha,1000);
                count--;
            }
            arq << mat << " " << nome << endl;
        }
    }




    arq.clear();
    count = 1;
    arq.seekg(0, arq.beg);
    cout << "Dados atuais" << endl;
    while(arq.getline(linha,1000))
    {
        cout << count++ << " - "<< linha << endl;
    }

    return 0;
}
\end{lstlisting}

Este código possui duas particularidades. Primeiro, ele usa a função \lstinline|arq.clear()|, ainda
não mencionada e, segundo, ele está errado.

Toda vez que o arquivo é lido até o seu fim, seu estado interno é mudado para identificar o fato.
Isto é verificável pela função \lstinline|arq.eof()|, que testa se o arquivo chegou ao \emph{end of
file}. Quando isso é verdade, as funções de reposicionamento não funcionarão, a não ser que este
status seja reiniciado, o que é feito com a função \lstinline|clear()|. No código simplesmente
usamos esta função sempre que formos fazer um \emph{seek}, por simplicidade.

Sobre o código não funcionar como esperado, execute-o e insira um aluno apenas, com matrícula
"aaaaaaaaaa" e nome "bbbbbbbbbb". Em seguida, altere os dados da linha 1 e insira matrícula "cc" e
nome "dd". Ao final, os dados impressos serão os seguintes:

\begin{verbatim}
Dados atuais
1 - cc dd
2 - aaaa bbbbbbbbbb
\end{verbatim}

## {Exercícios}
### {}
Corrija o programa exemplo mostrado acima para que escreva sempre linhas de um mesmo tamanho e que,
portanto, não tenha o problema de fragmentação de registros.










\begin{tabular}{l-l}
ios::ate		& Posiciona no fim do arquivo. Se não for usado, é posicionado no início.\\
\end{tabular}


## {Arquivos binários}

\begin{tabular}{l-l}
ios::binary		& Modo não formatado. (Próximo capítulo)\\
\end{tabular}


















O argumento \lstinline{nome_do_arquivo} é o caminho do arquivo que se deseja abrir, e
\lstinline{modo_de_abertura} representa como o arquivo será aberto, de acordo com a tabela a seguir:
\begin{table}[h]
  \centering
    \begin{tabular}{|c|l|}\hline
\textbf{Modo} & \textbf{Descrição}\\\hline
r & Abre arquivo texto somente para leitura\\\hline
w & Cria arquivo texto somente para escrita\\\hline
a & Anexa dados a um arquivo texto\\\hline
r+ & Abre arquivo texto para leitura e escrita\\\hline
w+ & Cria arquivo onde poderão ser realizadas leituras e escritas\\\hline
a+ & Anexa dados a um arquivo texto ou cria um para leitura e escrita\\\hline
    \end{tabular}
  \caption{Modos de abertura de arquivo texto em C.}
  \label{tab:fopen_modes}
\end{table}
      
\subsubsection{Fechamento de Arquivo}
Um arquivo aberto sempre deve ser fechado antes do fim do programa. A função que realiza essa tarefa
é \lstinline{fclose}. Seu protótipo é:

\lstinline{int fclose(FILE *arq);}

O argumento \lstinline{arq} é a variável que representa o arquivo aberto (com \lstinline{fopen})
O retorno dessa função é zero em caso de sucesso. Qualquer valor diferente de zero, significa erro.


\subsubsection{Leitura e Escrita de Arquivo}
A função \lstinline{fputc} escreve um caractere em um arquivo. Seu protótipo é:\\
      \verb|int fputc(char ch, FILE *arq);|

A função \lstinline{fputs} escreve um cadeia de caracteres em um arquivo. Seu protótipo é:\\
      \verb|char *fputs(char *cadeia, FILE *arq);|

A função \lstinline{fgetc} lê um caractere em um arquivo. Seu protótipo é:\\
      \verb|int fgetc(FILE *arq);|

A função \lstinline{fgets} lê um cadeia de caracteres em um arquivo. Seu protótipo é:\\
      \verb|char *fgets(char *cadeia, int tam, FILE *arq);|, onde \lstinline{tam} define o tamanho
      da cadeia que será lida: tam-1 ou fim de linha, o que ocorrer primeiro.

A função \lstinline{fprintf} permite escrever em um arquivo da mesma forma que escrevemos na tela
com o \lstinline{printf}. Seu protótipo é:\\
      \verb|int fprintf(FILE *arq, char *formato, ...);|

A função \lstinline{fscanf} lê informações de um arquivo da mesma forma que lemos do teclado com o
\lstinline{scanf}. Seu protótipo é:\\
      \verb|int fscanf(FILE *arq, char *formato, ...);|

\subsubsection{Exemplos}
 \begin{lstlisting}
#include <stdio.h>
#include <stdlib.h>

int main(){
  FILE *arq;
  char nome1[20], nome2[20], linha[20];
  arq = fopen("teste.txt", "w");
  printf("entre nome1: "); scanf("%s", nome1);
  printf("entre nome2: "); scanf("%s", nome2);
  fputs(nome1, arq);
  fputs("\n", arq);
  fputs(nome2, arq);
  fclose(arq);
  arq = fopen("teste.txt", "r");
  printf("lendo do arquivo:\n");
  fgets(linha, 20, arq);
  printf("\tnome1: %s", linha);
  fgets(linha, 20, arq);
  printf("\tnome2: %s\n", linha);
  return 0;
}
\end{lstlisting}


\begin{lstlisting}
#include <stdio.h>
#include <stdlib.h>

int main(){
  FILE *arq;
  char nome1[20], nome2[20], linha[20];
  arq = fopen("teste.txt", "w");
  printf("entre nome1: "); scanf("%s", nome1);
  printf("entre nome2: "); scanf("%s", nome2);
  fprintf(arq, "%s\n%s", nome1, nome2);
  fclose(arq);
  arq = fopen("teste.txt", "r");
  printf("lendo do arquivo:\n");
  fscanf(arq, "%s", nome1);
  fscanf(arq, "%s", nome2);
  printf("nome1: %s\nnome2: %s\n", nome1, nome2);
  return 0;
}
\end{lstlisting}


\part{Avançado: Estruturas de dados}
\chapter{Alocação Dinâmica}
Alocação de arranjos multi-dimensionais (caso não contíguo)

\chapter{BigNum}
Lembrar limites de variáveis númericas.

Implementando funções para manipulação de números gigantescos.

\chapter{Listas}

\chapter{Filas}

\chapter{Pilhas}

\chapter{Árvores}

