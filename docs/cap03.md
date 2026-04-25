# Variáveis, Entrada / Saída e Operadores

A todo momento precisamos representar informação do mundo a nossa volta em nossos programas. Essas informações, tais como nome, número de matrícula, nota final, temperatura, idade e outras tantas são armazenadas em entidades chamadas variáveis.

Uma variável nada mais é do que um pedaço de memória, no qual se pode ler ou escrever alguma informação. A estes pedaços de memória podemos dar nomes que nos ajude a lembrar o que exatamente está escrito ali. Por exemplo, se uma variável guarda a idade de alguém, um bom nome seria "idade", enquanto que "rataplam" ou "var13" provavelmente serão péssimas escolhas.

As alterações em uma variável resultam da interação com o usuário, isto é, quando o usuário informa valores para as mesmas em uma operação de leitura, ou da avaliação de expressões lógico-aritméticas (o tipo de cálculo nos quais o computador é especializado).

Neste capítulo veremos como criar nossas primeiras variáveis e como alterar seus valores por meio da leitura direta do teclado e da utilização de operadores.

## Declaração de Variáveis
Na linguagem C, toda variável deve ser declarada (isto é, criada) no início do corpo da função que a contem. A declaração de uma variável tem pelo menos duas partes:
**Nome:**: usado para referenciar a variável quando se precisa ler ou escrever a mesma;

**Tipo:**: para que o computador saiba como tratar a informação, ele precisa saber de que tipo ela é, ou seja, se é um número, ou uma palavra, ou uma caractere, etc; e,

Algumas regras simples devem ser seguinda na hora de se nomear uma variável:
- o nome só pode conter os caracteres [a-z], [A-Z], [0-9] e o "_"; e,

- o nome não pode começar com números.

Quanto aos tipos usaremos, por enquanto, os seguintes:
**int**: representando um número inteiro, como por exemplo 3, 4 e -78;

**float:**: representando um número real, com casas decimais separadas por *ponto*, como por exemplo 3.1416 e -1.2; e

**char:**: representando um caractere (letra, dígito, sinal de pontuação) como por exemplo 5, a, Z, ., e -.

São exemplos de declarações de variáveis válidas:
```c
int nota1, nota2;
float media;
char _caractere;
```

São exemplos de declarações inválidas:
```c
int 1nota, 2nota;
float #media;
char nome completo;
```

### Atribuição e Uso
Como já dito, uma variável é um pedaço da memória do computador no qual se pode "escrever" e "ler" dados.
Em vez de "escrever", contudo, no mundo da computação usamos a expressão *atribuir um valor a uma variável* para significar a mudança do valor da variável. Esta operação é executada pelo operador de atribuição `=`. Por exemplo, o seguinte código declara três variáveis numéricas, duas inteiras e uma real, e, em seguida, lhes atribui os valores `0`, `10` e `10.0`.
```c
int inteiro1, inteiro2;
float real;

inteiro1 = 0;
inteiro2 = 10;
real = 10.0;
```

A memória do computador sempre tem algum dado, tenha ele sido colocado por você ou não, seja ele relevante ou não. Logo, para se usar o conteúdo de uma variável, é necessário ter certeza de que a mesma contém um valor que faça sentido. Isto é, algo que tenha sido atribuído pelo seu programa àquela variável, via uma operação de leitura, via uma computação qualquer, ou via uma atribuição como a do exemplo anterior.

Denominamos a primeira atribuição de um valor a uma variável de *iniciação* (ou *inicialização*). E já que qualquer variável só deve ser usada se tiver sido iniciada, o C(++) permite que as variáveis sejam iniciadas já em sua declaração. Por exemplo, o código abaixo faz exatamente o que fazia o exemplo anterior, mas de forma mais compacta.

```c
int inteiro1 = 0, 
    inteiro2 = 10;
float real = 10.0;
```

Observe que se pode iniciar várias variáveis do mesmo tipo, declaradas na mesma linha, com valores distintos. Neste caso, note  quebra de linha entre as declarações de `inteiro1` e `inteiro2`; ela é somente estética, mas ajuda a separar a declaração e iniciação das várias variáveis.

Agora que você viu como declarar e iniciar uma variável vem a parte fácil: usá-la. Veja como no seguinte exemplo.
```c
// cod:vars
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
```
É simples assim: para se usar uma variável, basta colocar seu nome na expressão a ser computada. Na linha 9, por exemplo, atribui-se à variável `area`  o valor da multiplicação do conteúdo da variável `PI` por `raio`, ao quadrado. Na linha 10, o resultado da função é o conteúdo da variável `area`.

### Parâmetros são Variáveis
Nos exemplos de programas dos capítulos anteriores, você viu como o conteúdo de uma parâmetro é definido e usado. Por exemplo, os  dois parâmetros da função `area_retangulo`, reproduzida abaixo, são declarados dizendo-se de que tipo eles são e quais são seus nomes. Em seguida, no corpo da função, os parâmetros são usados no cálculo da área simplesmente multiplicando-se "o nome de um pelo nome do outro"; os valores dos parâmetros são aqueles passados na chamada da função. 

```c
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
```

Esta semelhança com a declaração e uso de variáveis não é coincidental: parâmetros não são mais do que variáveis declaradas e iniciadas de uma forma especial. Isto é, elas declaradas na definição da função e são iniciadas atribuindo-se os valores passados na invocação da função, na mesma órdem em que são passados. Isto é, se a função é invocada como `area_retangulo(1,2)`, então 1 é atribuído à variável/parâmetro `altura` e 2 à `base`. Se a função é invocada como `area_retangulo(X,y)`, então o valor da variável X, seja lá qual for é atribuído à variável/parâmetro `altura` e de y à `base`.

## Entrada / Saída
Além da escrita ou impressão de dados na tela, vista no Capítulo, uma das tarefas mais comuns em programação é a leitura de valores informados pelo usuário. A seguir veremos o comando que nos permitem executar tal tarefas.

### Leitura
De forma semelhante ao `cout`, há um comando para leitura denominado `cin`. Este comando permite ler valores digitados pelo usuário atualizando a(s) variável(is) passada(s) para o `cin` por meio do conector `>>`.

A seguir temos um exemplo de entrada de dados:
```c
char letra;
int idade;

cout << "Informe a letra inicial de seu nome e sua idade: ";
// a seguir eh feita a leitura
cin >> letra >> idade;
cout << "A letra eh " << letra;
cout << " e sua idade eh " << idade << endl;
```

### Impressão
Complementando o que já vimos sobre o `cout`, vejamos como escrever o conteúdo de variáveis na tela:
- Variáveis e chamadas de funções aparecem diretamente também, e seus valores (e resultado) é que são colocados na saída.
A seguir, podemos ver alguns exemplos:
```c
char letra = 'a';
int num = 2;
cout << "letra = " << letra << endl << "num = " << num << endl;
```
que gera a seguinte saída:
```c
letra = a
num = 2
```

Agora que você consegue ler do teclado e escrever para a tela, veja como é fácil fazer um programa que calcule a área de retângulo cujos lados são digitados pelo usuário.
```c
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
```

#### Formatação de Impressão

Em algumas ocasiões há necessidade de formatar a saída para, por exemplo, garantir que os dados
fiquem alinhados, imprimir uma tabela, ou simplesmente por estética. A seguir veremos algumas
maneiras de formatar, texto, números inteiros e reais. Para formatação de texto e números deve-se
incluir a biblioteca `iomanip`.

A formatação de texto é obtida mediante definição da largura do conteúdo impresso e do alinhamento. O
comando `setw(<valor>)`, define a largura do texto impresso para o valor informado como
argumento, enquanto os comandos `right` e `left` definem o alinhamento para a
direita e esquerda, respectivamente. O efeito do comando `setw` não é permamente.
O código a seguir ilustra a utilização destes comandos:
```c
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
```
A execução deste código produz a seguinte saída:
```
Entre valor da aresta do cubo:
2.5
O volume do cubo eh:          15.625
O volume do cubo eh: ---------15.625
O volume do cubo eh: ---------15.625--------------
O volume do cubo eh: -----------------------15.625
O volume do cubo eh: ---------15.625
```
O comando `setfill` permite definir o caractere que será usado para preencher os espaços
restantes, de acordo com a largura definida com `setw`

Para formatação de números reais (`float` e `double`), o exemplo a seguir mostra
alguns comandos para formatação:

```c
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
```

O comando `fixed` determina que o número de casas depois decimais será fixo, enquanto o
comando `setprecision` define quantas casas decimais serão impressas. Desta maneira, para
o exemplo anterior, teremos a seguinte saída:

```
Entre valor da aresta do cubo:
4
O volume do cubo eh: 64
O volume do cubo eh: 64.00
O volume do cubo eh: 64.0000 
```

## Operadores
Os operadores são os mecanismos por meio dos quais os computadores realizam os cálculos aritméticos e lógicos, atualizando valores das variáveis e executando as tarefas a que se destinam.

Os operadores matemáticos são os mais utilizados na maioria dos programas que serão desenvolvidos. Os principais operadores aritméticos são: $+, -, *, /$ e o %, indicando, respectivamente, as operações de soma, subtração, multiplicação, divisão e resto da divisão.

Considere o exemplo a seguir:
```c
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
```

## Exercícios
!!! question "Exercício"
    Escreva uma função em C que, dado uma temperatura em graus Célsius (do tipo float), retorne a temperatura equivalente em Farenheit. 
    Escreva também a função `main`  que leia a temperatura em Célsius do teclado, invoque a função de conversão, e imprima o resultado.
    
    Dado: $F = \frac{9C}{5} + 32$
