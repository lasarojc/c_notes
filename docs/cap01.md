# O computador é uma máquina burra

Computadores são máquinas "burras" que não fazem nada além de seguir instruções. 
Sendo assim, eles precisam de instruções precisas e detalhadas sobre o que fazer. 
Agora que está ciente deste fato, você está pronto para entender que quando o programa não fizer o que você quer, é por que você lhe deu instruções erradas. 

Para que não cometamos erros (ou pelo menos para minimizá-los), ao montar a sequência de instruções que resolvem determinado problema precisamos, antes de qualquer outra coisa, entender o problema e sermos capazes de resolvê-lo "na mão". 
Uma vez que tenhamos uma solução teremos o que chamamos de um *algoritmo* (<http://www.merriam-webster.com/dictionary/algorithm>).

## Algoritmo 
Um algoritmo nada mais é que um conjunto de instruções para se resolver um problema. Por exemplo, para se destrancar uma porta temos o seguinte algoritmo:

- Coloque a chave na fechadura

- Gire a chave

É claro que este algoritmo está em um nível de abstração muito alto e que poderia ser muito mais detalhado. Por exemplo, não há por quê destrancar a porta se ela já estiver destrancada e não há como destrancá-la se não estiver de posse da chave. Quanto mais detalhada sua sequência de passos, mais próximo de algo inteligível ao computador ela será. Para que isto ocorra, isto é, para que o computador entenda suas intruções, além de detalhadas, eles precisam ser escritas em uma linguagem de programação.

## Linguagem de Programação
De acordo com fontes altamente confiáveis (<http://en.wikipedia.org/wiki/Programming_language>)
> Uma linguagem de programação é uma linguagem artificial projetada para comunicar instruções a uma máquina, particularmente computadores. Linguagens de programação podem ser usadas para criar programas que controlam o comportamento da máquina e expressar algoritmos de forma precisa (não ambígua).
De forma simplificada, uma liguagem de programação é um conjunto de palavras e regras sobre como usá-las na descrição de algoritmos interpretáveis por um computador. 

Existem diversas
 (Uma listagem não completa mas ainda assim impressionante pode ser encontrada em <http://en.wikipedia.org/wiki/Categorical_list_of_programming_languages>) linguagens de programação, tendo cada uma seus pontos fortes e fracos; neste curso, usaremos as linguagens C e C++.

## A linguagem C(++)
A primeira encarnação da linguagem de programação  [C](http://en.wikipedia.org/wiki/C_(programming_language)) foi desenvolvida no fim da década de 60, tendo sido extendida, melhorada e padronizada várias vezes depois. A linguagem C++, que extende a linguagem C com diversas funcionalidades como orientação a objetos, começou a ser desenvolvida na década de 70 e, como a linguagem C, também passou por várias reformas. 
Como resultado, hoje temos uma linguagem C++ padronizada que pode ser usada, mesmo que com certa dificuldade, para se programar em vários sistemas operacionais de forma portável. 
Além disso, a linguagem C++ é um super conjunto da linguagem C. Ou seja, todo e qualquer programa em C também é um programa em C++, mesmo que o oposto não seja verdade.

Como já mencionado, neste curso usaremos primariamente a linguagem C. Contudo, uma vez que o objetivo deste curso é introduzir o uso do raciocício computacional e não aprofundar no uso de determinada linguagem, estudaremos somente os aspectos mais básicos da linguagem C. Além disso, usaremos partes da linguagem C++ para simplificar o desenvolvimento dos nossos programas. Assim, nos referiremos à linguagem usada como C(++), pois nem é toda a C, e nem é somente C, mas não chega a ser C++. Mas chega de ladainha; vamos ao nosso primeiro programa em linguagem C(++)!

### Meu Primeiro Programa
O algoritmo em linguagem C(++)
 (Usaremos também os termos "programa" e "código" para nos referirmos a tais algoritmos.), 
abaixo, descreve para o computador os passos necessários para se escrever a mensagem "Olá Mundo!" na tela do computador. Não se preocupe com os detalhes de como isso é feito agora, mas foque-se nos seguintes aspectos:
- existem várias formas de se dizer "Olá Mundo!", por exemplo se pode saltar antes de fazê-lo, agaixar, ou fechar os olhos. Todas estas formas são corretas, embora algumas possam lhe causar certo constrangimento quando em público.

- um código de computador deve ser entendido, além de pelos computadores, também por humanos. Sendo assim, é imprescindível que você mantenha o código organizado.

- usar acentos em um programa é fonte de dores de cabeça; melhor simplesmente ignorá-los em nosso curso.

```c
// Ola Mundo!
#include <iostream>

using namespace std;

int main()
{
    cout << "Ola Mundo!" << endl;
    return 0;
}
```

Analisando o Código, podemos facilmente identificar a linha que contém a frase "Ola Mundo!". Esta linha é a que efetivamente *escreve* na tela do computador. Altere esta linha para que contenha, por exemplo, seu nome em vez da palavra *Mundo*. Digamos que seu nome seja *Feissibukson*. Este programa agora escreve na tela do computador os dizeres "Ola Feissibukson!". 

Para entendermos o que as demais linhas fazem, precisamos passar para o nosso próximo problema/programa.

### Área de um Retângulo
A área de um retângulo pode ser facilmente calculada caso você saiba o comprimento de sua base e de sua altura. Matematicamente, seja $b$ o comprimento da base e $a$ a altura. A função $f$ equivalente à área do retângulo pode ser definda como: $f(a,b) = a*b$. Isto é, a função $f$ tem dois parâmetros (a altura $a$ e base $b$ do retângulo) e calcula a área como sendo a multiplicação de $a$ e $b$. 

Em linguagem C(++) a função $f$ pode-se escrever esta função como mostrado no Código, que analisaremos em seguida.

```c
// Área de um retângulo
int f(int a, int b)
{
    return a * b;
}
```

A linha 1 do código define a função `f` como uma função que aceita dois parâmetros `a` e `b`. Além disso, esta função também define que cada um destes parâmetros é um número inteiro ao preceder cada parâmetro pela palavra `int`. Finalmente, esta linha também define que o resultado da função será um número inteiro ao preceder o nome da função (`f`) pela palavra `int`. Isto quer dizer que você não pode usar esta função para calcular a área de retângulos cujos lados não sejam inteiros. Mas não se preocupe, corrigiremos esta deficiência daqui a pouco.

As linhas 2 e 4 definem o *corpo da função*, isto é, quais outras linhas são partes da função `f`. Toda função na linguagem C precisa ter definido seu começo e fim usando `{` e `}`, respectivamente.

A linha 3 do código é onde o cálculo da área é efetivamente executado: `a*b`. Além disso, esta linha define também qual é o resultado da função ao preceder o resultado da multiplicação por `return`. Como a multiplicação de dois números inteiros só pode resultar em um número inteiro, o resultado da função também é inteiro, está justificado o tipo da função ser `int`.

### Tipos Primitivos da Linguagem C
O Código, como mencionado, tem a limitação de só calcular a área de retângulos cujos lados tenham tamanhos inteiros. Para corrigir esta deficiência, vamos alterá-lo para que aceite números reais. Em computação, números reais são também chamados de números com *pontos flutuantes* e, em linguagem C, simplesmente de `float`. Sendo assim, podemos corrigir o programa simplesmente substituindo as ocorrências da palavra `int` por `float`, resultando no Código

```c
// Área de retângulo com dimensões reais.
float f(float a, float b)
{
    return a * b;
}
```

Pronto, a função agora *recebe* dois parâmetros do tipo `float` e *retorna* um resultado também deste tipo. Juntamente com outros tipos que serão vistos adiante no curso, `int` e `float` são chamados de tipos de dados primitivos da linguagem. Isto sugere, obviamente, que há também tipos não primitivos, e nada poderia ser mais verdade. Estes tipos, contudo, só serão vistos bem mais adiante no curso, no Capítulo ?<!-- TODO: Adicionar referência -->.

### Organização do Código
É possível facilmente perceber um padrão nos exemplos de código apresentados até agora:
- A linha definindo a função é seguida por uma linha contendo apenas um `{` que é alinhado com o início da linha acima.

- A última linha da função contém apenas um `}`, alinhado com o `{` do início da função.

- Todas as linhas entre o `{` inicial e o `}` final estão alinhas e mais avançadas em relação às chaves.
Esta organização do código serve para facilitar a leitura do código, uma vez que torna extremamente óbvio onde a função começa e termina. Esta técnica é chamada *indentação*.

Algo que faltou nestes exemplos e que também serve ao propósito de facilitar o entendimento do código são os chamados comentários. O exemplo no Código mostra como a função `f` poderia ser comentada.

```c
// Área do retângulo, com comentários.
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
```

Observe que há dois tipos de comentários no código. O primeiro começa com `\*` e termina com `*\` e o segundo começa com ` ` e termina no final da linha. Todos os comentários servem somente ao programador e são completamente ignorados pelo computador. Os comentários podem ser poderosos aliados na hora de procurar por erros no seu código, uma vez que permitem desabilitar trechos do mesmo.

Finalmente, é muito importante nomear suas funções e parâmetros com nomes intuitivos. Seguindo esta orientação, escreveremos a última versão de nossa função.

```c
// Área do retângulo, com comentários e nomes intuitivos.
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
```

## Saída de Dados
Em computação, diz-se que um programa está executando a saída de dados quando envia para "fora" do programa tais dados. Exemplos comuns de saída de dados são a escrita em arquivo, o envio de mensagens na rede ou, o mais comum, a exibição de dados na tela. 

Em nossos programas, a saída de dados efetuada mais comumente será para a tela do computador. Este tipo de saída, por ser tão comum, é chamada de a saída padrão do C(++), ou simplesmente *C out*. Para enviar dados para a saída do C(++), usamos a expressão `cout <<`, seguido do dado a ser impresso na tela. Por exemplo, para imprimir a mensagem "Olá João", simplesmente adicionamos `cout << "Ola Joao"` ao código. Observe que o simbolos `<<` funciona como uma seta dizendo para onde os dados devem, neste caso, `cout`.

É possível enviar vários tipos de dados para a saída, como veremos no decorrer do curso. No caso da tela, os dados são convertidos para sua forma textual, para que possam ser lidos pelo usuário. 
O computador realiza a conversão de acordo com o tipo original do dado: se o dado já for um texto, ele é simplesmente copiado para a tela; se for um número, ele é convertido para um conjunto de dígitos que o represente.
Por exemplo, o trecho de programa 
```c
cout << "numero ";
cout << 10;
```
gera a saída `numero 10` na tela.

Observe que a palavra `numero` no programa aparece entre aspas duplas e que o numero 10. Isto ocorre por quê `numero` é um texto, e `10` é um número; todos os textos devem ser colocados entre aspas duplas, para que o computador o identifique como tal, mas o mesmo não é necessário para números. Veja bem, o número `10` é bem difernte de `"10"` pois, por exemplo, `10` pode ser somado a outro número (`10 + 32`), mas `"10"` não.

Para simplificar a saída de dados, em C(++) é possível encadear várias saídas em uma só, assim
```c
cout << "numero " << 10;
```
com o mesmo efeito do código anterior. Se houver necessidade de se iniciar nova linha na "impressão" na tela, basta enviar `endl` (contração de *end line*) para a saída. Assim, o código 
```c
cout << "numero " << 10 << endl << "texto " << endl;
```
imprime na tela o texto
```
numero 10
texto
```

Finalmente, quando uma "chamada" a uma função é enviada para o `cout`, o que é impresso é o resultado da função. Assim, 
```c
cout << "sen(1)" << endl << sen(1);
```
imprime na tela o texto
```
sen(1)
0
```
Você verá vários exemplos de usos do `cout` na próxima seção.

## A Função `main`
Que o computador é uma máquina burra e executa somente o que você manda você já deve ter entendido, mas como mandá-lo executar algo? Em linguagem C(++), o computador *sempre* começa a execução de um código pela função `main`, a função principal. Sendo assim, se você quer dizer ao computador que calcule a área de um retângulo, então esta ordem dever partir, de alguma forma, da função `main`. 

Para um exemplo,veja o seguinte código.

```c
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
```

Algumas observações importantes sobre a função `main`:
1. A função `main` tem sempre um resultado do tipo inteiro e seu resultado é sempre 0 (`return 0;`) (Na verdade, nem nem sempre é 0, mas por enquanto definiremos sempre assim.)

2. Função `main` é como um *highlander*: só pode haver uma! Isto é, cada programa só pode conter a definição de uma função com este nome. Aliás, a regra vale para toda e qualquer função; se não fosse assim, o computador não saberia a qual função você está se referindo em seu código.

3. Finalmente, a função `area_retangulo` aparece antes da fução `main` no programa. Isto deve ser verdade para todas as funções do seu programa. Isto ocorre por quê, antes de executar a função `main`, o computador precisa aprender sobre a existência das outras funções.

O código como está, includindo as duas linhas iniciais que ainda não sabem para que servem, "pronto" para ser executado no seu computador. No próximo capítulo veremos exatamente como fazer isso. Até lá, executemos o código "na mão":
- O programa começa a executar pela função `main`; somente o que está no corpo desta função é executado.

- Na linha 18 não há o que executar, pois é só um comentário.

- Na linha 19, como vimos no Código, está se dizendo para o computador escrever algo na tela. Este algo é o resultado da aplicação da função `area_retangulo` aos parâmetros 3.3 e 2.0. (Observe o uso de "." como separador de casas decimais.). Para que se conheça este resultado, o programa executa a função `area_retangulo`.

- A linha 13 calcula a área do retângulo, que é então retornado para a linha 19.

- Na linha 19, a *chamada* da função é "substituída" pelo resultado, e o número 6.6 é escrito na tela do computador. Na sequência, é escrito também `endl`, que faz com que o computador salte para a próxima linha da tela do computador.

- Na linha 20 o procedimento todo é repetido, agora escrevendo o valor 4.0 na tela.

- Na linha 23 também se repete o procedimento, mas agora passando como parâmetro para a função os valores inteiros 4 e 2. Como todo número inteiro também é um número real, a função é novamente executada e o valor 8.0 é impresso na tela.

## Conclusão
Os códigos apresentados neste capítulo, apesar de simples, ilustraram vários pontos importantes da programação de computadores em geral e da linguagem C em específico. Estes pontos podem ser sumarizados assim:
- Em C(++) pode-se definir funções que executem computações bem definidas e específicas.

- C(++) tem vários *tipos* de dados, como `int` (números inteiros) e `float` (números reais).

- É importante manter o código organizado, comentado e indentado. Isso facilita seu entendimento e manutenção.

## Exercícios
!!! question "Exercício"
    Escreva um função que calcule a área de um círculo. Observe que a linguagem C é baseada na língua inglesa, na qual se separa casas decimais por `.` e não por `,`. Logo, $\Pi$ é igual 3.14 e não 3,14.

!!! question "Exercício"
    Escreva uma função que calcule a área de um triângulo.
