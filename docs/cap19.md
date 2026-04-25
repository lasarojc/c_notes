# Referências II

Continuando com o estudo de ponteiros, vamos ver como utilizá-los para referenciar estruturas
e arranjos.

## Ponteiros para Structs
Se você recordar-se da anologia apresentada na seção, em que a memória é comparada a um grande vetor e cada tipo de dados tem um tamanho pré-definido, é fácil entender como uma estrutura é representada na memória.

Considere a seguinte estrutura e responda: qual o tamanho desta estrutura na memória do computador? 
```c
typedef struct
{
  int i;
  char c;
  float j;
} exemplo1;
```

Para responder a esta pergunta precisamos entender que uma estrutura ocupa espaço equivalente à soma do espaço ocupado por cada um de seus campos. Desta forma, o espaço total ocupado por uma variável do tipo `exemplo1` será a soma dos tamanhos de 1 `int`, 1 `char` e 1
`float`, ou seja, $4 + 1 + 4 = 9$ bytes.

Assim, e você cria uma variável `exemplo1 v[10]`, o compilador deve reservar um espaço de $10 × 9 = 90$ bytes.

Assim como nos referimos a variáveis dos tipos primitivos (inteiro, real, caractere) utilizando ponteiros, podemos também utilizar ponteiros para acessar uma variável do tipo `struct` e seus campos. Veja o exemplo para a estrutura declarada anteriormente.

```c
exemplo1 a = {-5, 'z', 0.89}, b;
exemplo1 *p;
p = &a;
cout << (*p).i << endl;
p = &b;
cin >> (*p).c;
```

Este trecho mostra na linha 1 a criação de duas variáveis do tipo `exemplo1` e na linha 2 a criação de uma variável do tipo ponteiro para `exemplo1`. As linhas 3 e 5 atualizando o ponteiro, fazendo com que referencie as variáveis `a` e `b`, respectivamente.
Desta maneira, a linha 4 irá imprimir o valor de `a.i`, enquanto a linha 6 irá ler a partir do teclado um valor para `b.c`.

Quando usamos ponteiros e estruturas, aparece o incoveniente de termos que digitar toda vez entre parênteses a variável do tipo ponteiro (`(*p).c`). Para simplificar a utilização de ponteiros no acesso a campos de uma estrutura, a linguagem C permite escrever esta mesma instrução de uma maneira mais fácil de digitar: `p->c`. O código anterior pode ser reescrito como:

```c
exemplo1 a = {-5, 'z', 0.89}, b;
exemplo1 *p;
p = &a;
cout << p->i << endl;
p = &b;
cin >> p->c;
```

Por fim, a passagem de estruturas por referência em funções auxiliares é feita da mesma forma que
vimos no capítulo anterior:

```c
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
```

A função auxiliar troca os valores de duas variáveis do tipo `exemplo1` passadas por referência. Após a invocação da função auxiliar a partir da `main` os valores iniciais das variáveis `a` e `b` serão trocados.

## Arranjos e Ponteiros
Até agora vimos vetores sem nenhuma relação com ponteiros. No fundo, quando criamos um vetor com a instrução `int a[10]`, estamos dizendo ao compilador para reservar na memória espaço para 10 inteiros (40 bytes) e armazenar o endereço em que começa o vetor na variável `a`. Em outras palavras, a variável `a` é um *ponteiro* para o primeiro elemento do vetor.

Por esta razão, a relação entre vetores e ponteiros é mais direta e mais fácil de utilizar.  Uma vez
que a variável que usamos contém o endereço do começo do vetor, um ponteiro pode receber diretamente
seu valor, sem necessidade do operador &. Considere o exemplo a seguir:

```c
float a[10];
float *p;
p = a;
cout << "Digite 10 numeros reais: ";
for(int i = 0; i < 10; i++)
  cin >> a[i];
cout << "Num. digitados: ";
for(int i = 0; i < 10; i++)
  cout << p[i];
```

Observe a linha 3 e perceba como a atualização da referência do ponteiro `p` para o vetor `a` não utilizou o &. Isto porque `a` também é um ponteiro. A diferença entre `p` e `a` é que a primeira pode ter sua referência atualizada, enquanto a segunda não. A partir da linha 3, o vetor pode ser acessado tanto pela variável `a` (linha 6) quanto pela variável `p` (linha 9).

É por este motivo que vetores sempre são passados por referência em funções auxiliares, sem a necessidade do & e do *.

### Percorrendo vetores com ponteiros

Já sabemos a relação entre ponteiros e vetores. Veremos a seguir algumas maneiras diferentes de acessar os elementos de um vetor utilizando ponteiros. Considere o trecho de um programa a seguir:

```c
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
```

Neste trecho utilizamos o ponteiro `s` como o vetor `str`, pois a partir da linha 3 ele "aponta" para o vetor. Este mesmo trecho pode ser reescrito:

```c
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
```

Observe a linha 9 de cada um dos dois trechos anteriores e veja a diferença na notação. Quando utilizamos ponteiro, podemos acessar um vetor pelo índice (colchetes) ou por um deslocamento sobre o valor do endereço inicial do vetor armazenado em `s`, ou seja, a notação `*(s+i)`, significa o caractere localizado `i` caracteres a partir do caractere na primeira posição do vetor.

O mesmo trecho pode ser reescrito  ainda de uma terceira forma:

```c
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
```

Qual a diferença entre esta versão e as versões anteriores? Qual a diferença entre `s++` e `(*s)++`? 
Qual o valor de `s[0]` em cada versão? 
E de `*s`? 
E de `str[0]`?

## Laboratório
!!! example "Laboratório"
    Crie uma estrutura com os campos nome, idade e salario dos tipos *string*, inteiro e real, respectivamente. 
    
    Em seguida, crie uma função que receba referências para duas variáveis de tal tipo e uma variável correspondente a uma porcentagem de aumento que deve ser aplicada sobre o campo salário de cada estrutura. 
    A função principal deve ler cada campo das duas variáveis e imprimir o novo salário.
    
    Finalmente, crie uma função que recebe duas variáveis de tal tipo e que troque os valores de todos os campos das duas estruturas. A função principal deve agora imprimir as estruturas antes e depois da troca.

!!! example "Laboratório"
    Execute as três versões do programa da seção e veja se há diferença no resultado. Responda às perguntas no final da seção.
