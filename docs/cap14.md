# Funções Úteis I
## Funções Matemáticas
A biblioteca `math.h` fornece algumas funções aritméticas muito úteis no desenvolvimento de programas. A Tabela apresenta algumas destas funções.

  
  | Função | Descrição/Exemplo |
| --- | --- |
| abs | valor absoluto do argumento. Ex: `int x = abs(-9);` |
| sin | seno do argumento (em radianos). Ex: `double x = sin(3.14159);` |
| cos | cosseno do argumento (em radianos). Ex: `double x = cos(3.14159);` |
| tan | tangente do argumento (em radianos). Ex: `double x = tan(3.14159);` |
| asin | arco cujo seno é passado como argumento. Ex: `double x = asin(1);` |
| acos | arco cujo cosseno é passado como argumento. Ex: `double x = acos(1);` |
| atan | arco cuja tangente é passada como argumento. Ex: `double x = atan(sqrt(2)/2);` |
| floor | piso do valor passado como argumento. Ex: `double x = floor(3.2); //=3` |
| ceil | teto do valor passado como argumento. Ex: `double x = floor(3.2); //=4` |
| round | arredonda o argumento para o inteiro mais próximo. Ex: `double x = round(9.9); //=10` |
| pow | eleva o primeiro argumento ao expoente no segundo. Ex: `double x = pow(2,3); //=8` |
| sqrt | retorna a raiz quadrada do argumento. Ex: `double x = sqrt(169); //=13` |
| log | retorna logaritmo natural do argumento. |
| log10 | retorna log. do argumento na base 10. |
| log2 | retornar log do argumento na base 2 |
  *Algumas funções aritméticas.*

  

Além das funções em `math.h`, duas outras funções, da biblioteca `stdlib.h`, são particularmente interessantes na manipulação de números. Estas funções são apresentadas na Tabela.

  
  | Função | Descrição/Exemplo |
| --- | --- |
| rand | retorna um número aleatório (biblioteca `stdlib.h`) |
| srand | define a semente para a geração de números aleatórios por `rand` (biblioteca |
| `stdlib.h`) |  |
  *Funções para geração de números aleatórios.*

  

A função `rand()` é utiliza para gerar números aleatórios. Um número aleatório é gerado
internamente pelo computador aplicando-se operações aritméticas que o usuário desconhece a partir de
um valor inicial chamado de *semente*. O valor dessa semente é definido com a função
`srand()`. O exemplo a seguir imprime na tela 30 números "aleatórios".

```c
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
```

O codigo a seguir é para um jogo de adivinhação. O programa gera um número aleatório entre 1 e 10, e o usuário deve descobrir qual é este número (<http://www.cplusplus.com/reference/clibrary/cstdlib/rand/>).

```c
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
```

## Laboratório
!!! example "Laboratório"
    Faça um programa que leia os catetos de um triângulo e imprima o valor de sua
    hipotenusa. Utiliza as funções aritméticas.

!!! example "Laboratório"
    O valor de $\pi$ pode ser dado pela série:
    
    $\pi = \sum_{n=0}^{∞} (-1)^n\frac{4}{2n+1}$
    
    Faça uma função chamada `pi` que recebe o valor de `n` e retorna o valor calculado de
    acordo com a função informada. A função principal deve ler o valor de `n`, invocar a função
    `pi` e imprimir o resultado.

!!! example "Laboratório"
    Faça um programa que leia dois números $x$ e $y$ e calcule $log_y x$. O cálculo deve ser feito em uma função auxiliar.

!!! example "Laboratório"
    Faça uma função que receba como parâmetro o valor de um ângulo em graus e o número de iterações (n) e calcule o valor do cosseno hiperbólico desse ângulo usando sua respectiva série de Taylor:
    
    $cosh(x) = \sum_{n=1}^{∞} \frac{x^{2n}}{(2n)!}$
    
    , onde x é o valor do ângulo em *radianos*. Considerar pi = 3.141593.
