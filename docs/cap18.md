# Referências

O uso da analogia da memória do computador com uma planilha eletrônica nos permitiu entender como variáveis simples e também arranjos são alocados em nossos programas. Agora que já conhecemos vetores, usaremos uma analogia mais precisa para entendermos referências, ou como são mais popularmente conhecidas, os famigerados ponteiros.

## A memória é um grande vetor

A memória de um computador pode ser vista como um grande vetor de bytes. O primeiro byte é denominado byte 0, o segundo, byte 1 e assim por diante até o tamanho da memória disponível ao seu programa.

Quando em seu programa você, por exemplo, declara uma variável do tipo caractere (`char`) com o nome `c`, o compilador separa um byte da memória, digamos o byte 7542, e passa a chamá-lo de `c`. Assim, toda vez que se referir à variável `c` em seu programa, o computador sabe que está se referindo ao byte 7542. Neste caso, dizemos que o endereço da variável `c` é 7542.

Similarmente, quando você aloca uma variável do tipo inteiro, o compilador reserva quatro bytes para você, digamos, os bytes 8012, 8013, 8014 e 8015. Tal variável tem o endereço 8012 (como os tipos tem sempre tamanho fixo, o endereço do primeiro byte mais a informação sobre o tipo da variável é suficiente para o computador determinar de onde até onde na memória cada variável fica armazenada).

Finalmente, quando você aloca um vetor de tamanho $n$ de algum tipo qualquer, o compilador reserva um espaço de tamanho $n × t$, onde $t$ é o tamanho do tipo em questão. Se são 10 inteiros, por exemplo, então o vetor terá tamanho 40 bytes. O endereço desta variável é o endereço do primeiro byte da primeira célula. Assim, quando você, por exemplo, acessa a posição 5 de um vetor de inteiros cujo endereço é 1000, o computador faz o seguinte cálculo para determinar a posição de memória que você está acessando, sabendo que cada inteiro ocupa 4 bytes: $1000+5*4$.

## Variáveis do Tipo Referência
Em certas situações, o poder de se referir a posições de memória pelo seus endereços em vez de por um nome de variável é muito útil. Por exemplo, imagine que precisemos calcular uma série de estatísticas sobre os dados em um vetor. Neste caso, gostaríamos de definir uma função que analisasse o vetor e desse como resultados as várias estatísticas, como média, desvio padrão, variância, intervalo de confiança etc. Entretanto, como bem sabemos, funções em C(++) retornam um único resultado. Se, contudo, pudéssemos passar como parâmetro para a função as referências de onde gostaríamos que os resultados fossem colocados, então a função poderia colocá-los diretamente nestas posições de memória. Esse mecanismo é o que chamamos de passagem de parâmetro por referência.

Antes de se poder exercitar a passagem de parâmetros por referência, contudo, precisamos aprender a declará-las, a obter referências para posições de memória, e a usar tais referências. Estas operações são feitas pelos operadores `*` e `&`. A declaração de variáveis segue a seguinte sintaxe:

```
tipo  *identificador;
```

Assim, para se declarar variáveis de referência para uma posições de memória que armazenam um inteiro, um caractere, e um float, você usaria as seguintes declarações:
```c
int *ref_int;
char *ref_char;
float *zabumba;
```

Observe que o `*` é sempre considerado como ligado ao identificador e não ao tipo da variável. Assim, a linha de código
```c
int *a, b, *c;
```
declara duas referências para inteiro (`a` e `c`), e um inteiro (`b`). Para se evitar confusões, sugere-se que não se declare variáveis do tipo referência e não referência em conjunto. Ou seja, a código acima deveria ser reescrito como
```c
int *a, *c;
int b;
```

O operador `&` permite que se extraia o endereço (ou uma referência) de uma variável. No código,
```c
int *a;
int b;

a = &b;
```
`a` recebe o endereço da variável `b`. Logo, se `b` está nos bytes 2012, 2013, 2014 e 2015, a variável a recebe o valor 2012. 

Aqui, gostaríamos de chamar a atenção para o seguinte fato: *em raríssimas situações  é necessário saber o endereço de uma variável. Na maior parte dos casos, basta saber que uma variável tem tal endereço.*.

Finalmente, o operador `*` também nos permite acessar o conteúdo de uma variável referenciada, em do valor da referência. No código,
```c
int *a;
int b;
int c;

a = &b;
*a = 20;
c = *a;
c++;
```
a variável `b` termina com o valor 20, enquanto que a variável c termina com o valor 21.

## Passagem de Referências como Parâmetros
Variáveis do tipo referência, como outros tipos de variáveis, podem ser passadas como parâmetro em chamadas de função. A grande vantagem desta técnica, também conhecida como passagem de parâmetros por referência, é a possibilidade de modificação da memória para qual a referência foi passada. Por exemplo, analise o seguinte código.

```c
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
```

Esse programa calcula em uma única chamada, os valores do seno, cosseno e tangente da variável `v`. Enquanto o feito não parece muito impressionante, pense no caso em que você precisa calcular diversas estatísticas de um vetor de números. Neste caso, devido à forte dependência do cálculo de uma estatística no cálculo de outras, esta função poderia simplificar em muito o seu código.

## Laboratório
!!! example "Laboratório"
    Escreva um programa que contenha funções que calculam a média, variância e desvio padrão de um vetor de números reais (uma função por dado estatístico).

!!! example "Laboratório"
    Altere o programa do exercício anterior para que calcule as três estatísticas em uma função apenas, reaproveitado os cálculos uns dos outros.
