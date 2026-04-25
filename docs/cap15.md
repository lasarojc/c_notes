# Arranjos Multidimensionais

Embora os arranjos unidimensionais sejam úteis em várias situações, eles não são suficientes para resolver todos os problemas relacionados a arranjos. Em certas situações, várias dimensões precisam ser representadas. Um exemplo simples é o problema de multiplicação de matrizes. (A bem da verdade, é possível representar qualquer matriz finita como um arranjo unidimensional, mas a complexidade é muito maior em relação ao uso de arranjos multidimensionais.)

## Declaração e Iniciação
Como já visto, a declaração de arranjos tem a seguinte sintaxe,
```
tipo identificador[tamanho];
```

A declaração de uma variável do tipo matriz tem uma forma semelhante, apenas aumentando uma segunda dimensão ao arranjo, como a seguir.
```
tipo identificador[tamanho1][tamanho2];
```

Assim, uma declaração como
```c
int matriz[10][20];
```
declara uma matriz de 10 linhas por 10 colunas, cujas células são números inteiros.

A matriz pode ser iniciada como em arranjos unidimensionais, colocando-se os valores do elemento dentro de chaves após a declaração da matriz. Os valores para cada linha devem ficar dentro de chaves próprias e são
separados por vírgula:

```c
{int matriz[2][3] = {{1, 2, 3}, {4, 5, 6}};
```

A matriz criada pode ser visualizada da seguinte maneira:

  | 1 | 2 | 3 |
| --- | --- | --- |
| 4 | 5 | 6 |

### Acesso aos elementos
O acesso às células é feito também como em arranjos unidimensionais, exceto que ambas as coordenadas devem ser especificadas. O exemplo a seguir mostra a criação, iniciação, e impressão dos elementos de uma matriz bidimensional.

```c
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
```

Observe que tanto na leitura como impressão da matriz, o laço mais externo percorre as linhas. Para cada valor da variável `i`, a variável `j`, dentro do laço interno percorre os valores de 0 a $N-1$. Desta maneira, a matriz é lida e impressa linha a linha. 

Observe a impressão. Para que serve o comando `cout<<endl;`?

## Mais Dimensões
Agora você já deve ter deduzido que para adicionar mais dimensões aos seus arranjos, basta colocar esta dimensão na declaração dos mesmos. Por exemplo, o seguinte trecho de código declara um arranjo com três dimensões, em que cada célula é um inteiro. 
```c
char matriz[100][100][100];
```

Outra forma de ver tal arranjo é como um livro com várias "páginas", em que cada uma é uma matriz bidimensional.

## Multiplicação de Matrizes
Agora que você viu alguns exemplos de declarações de arranjos multidimensionais, vejamos alguns usos reais, como a já mencionada multiplicação de matrizes.

Sejam duas matrizes $A$ e $B$, tal que $A$ tem dimensões $m × n$ e $B, n × o$; então, a matriz $AB$ tem dimensões  $m× o$, e $C_i,j = \sum_{k = 1}^{m}A_{m,n}B_{n,o}$. 

Observe que na matemática os índices começam, normalmente, em 1. Na computação, contudo, os arranjos tem seu menor índice igual a zero. Logo, o código para multiplicar as duas matrizes fica assim.

```c
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
```

Observe que fizemos nosso código de manipulação da matriz dentro da função `main`. Fizemos isso por que usar matrizes como parâmetro é bem mais complicado do que vetores unidimensionais. Contudo, não se aflija, pois veremos isso logo a seguir.

## Passagem de matriz como parâmetro em funções
Vimos que, ao passar vetores para uma função, não era necessário especificar o número de elementos
no vetor. Em matrizes bidimensionais, não é necessário especificar o número de linhas na matriz,
apenas o número de colunas. O programa a seguir usa a função `exibeMatriz` para exibir o conteúdo
de matrizes bidimensionais:
```c
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
```

Via de regra, não é necessário especificar a primeira dimensão da matriz. Isto é, em vetores, você não passava qualquer dimensão. Em matrizes bidimensionais, não precisa especificar a quantidade de linhas. Em uma matriz tridimensional, não precisaria especificar a quantidade de "páginas", e assim por diante.

Lembre-se, semelhante ao que acontece com vetores, matrizes alteradas em funções auxiliares implicam em alteração na matriz original.

## Matrizes de Caracteres
Da mesma forma que vetores de caracteres podem ser manipuladas de forma especial no C(++), também podem as matrizes de caractere. Na verdade, se um vetor de caracteres é o que chama-se de uma string, então uma matriz bidimensional de caracteres é, na verdade, um vetor de strings. Por exemplo,

```c
char nomes[10][20];
```
pode ser visto como um vetor de 10 strings, cada uma com 20 caracteres, e cada string pode ser manipulada como tal, como no exemplo a seguir.

```c
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
```

## Exercicios
!!! example "Laboratório"
    Escreva um programa com uma função que receba como parâmetro uma matriz bidimensional e suas dimensões, e que incremente cada elemento da matriz em 10%.

!!! example "Laboratório"
    Escreva um programa que leia e [some](http://pt.wikipedia.org/wiki/Adição_de_matrizes) duas matrizes, imprimindo o resultado. Utilize funções auxiliares para leitura, impressão e soma.

!!! example "Laboratório"
    Escreva um programa que leia uma matriz e diga se ela é a matriz [identidade](http://pt.wikipedia.org/wiki/Matriz_identidade) ou não.

!!! example "Laboratório"
    Escreva um programa que leia uma matriz e imprima sua 
    [transposta](http://pt.wikipedia.org/wiki/Matriz_transposta).
