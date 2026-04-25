# Arranjos Unidimensionais
Tente resolver o seguinte problema: 
1. ler um conjunto de 6 números inteiros

2. calcular sua média

3. imprimir todos os números maiores que a média na tela do computador
Fácil, certo? Basta declarar 6 variáveis do tipo `int`, ler seus valores, somar seus valores e dividir por 6, calculando a média. Finalmente, basta escolher aquelas variáveis com números maiores que a média e imprimí-las.

Mas e se alterássemos o problema para que, em vez de 6, precisasse ler 10 números, ou 100? Ainda assim se poderia usar o mesmo algoritmo, com 10 ou 100 variáveis em vez de 6. Mas ter muitas variáveis distintas com a mesma finalidade não é viável por duas razões:
- difícil de manter: se você precisar renomear uma variável, terá que fazê-lo em todas as variáveis;
	se precisar aumentar ou diminuir o número de variáveis, terá que apagar/copiar e renomear.

- evita reuso de código: se uma mesma operação precisa ser aplicada a cada variável, o mesmo código deve ser reescrito para cada variável, dificultado o reuso de código.

A solução para esta situação é o uso de vetores (ou variáveis indexadas, ou arranjo, ou *array*).

## Vetores
Continuando com nossa analogia da memória do computador como uma planilha eletrônica, um vetor é uma variável que nomeia diversas células contíguas da memória do computador. Isto é, de certa forma, enquanto uma variável `int` corresponde a uma área da memória que cabe 1 inteiro, um vetor de 10 `int` é uma variável que cabe 10 inteiros.

A sintaxe para a declaração estática de vetores é bem simples (em capítulos futuros veremos como declarar vetores dinâmicos, isto é, que podem variar seus tamanhos).

```
tipo identificador[tamanho];
```

Onde
- tipo -- é o tipo do dado a ser armazenado em cada posição do vetor;

- identificador -- é o nome do vetor;

- tamanho -- é a quantidade de células no vetor;

O acesso a uma célula, para leitura ou atribuição, é feito usando-se o identificador seguido pela posição a ser acessada, entre colchetes (`[]`). Por exemplo, `x[3] = 0` atribui o valor 0 à posição de índice 3 do vetor `x`. Algo importante a ser observado aqui é que a primeira posição de um vetor de tamanho $n$ tem índice 0 e a última tem índice $n-1$.

O exemplo a seguir resolve o problema apresentado na seção anterior usando vetores.

```c
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
```

Observe a definição e o uso da palavra `TAMANHO` no programa. Uma vez definido que `TAMANHO` tem o valor 10, o computador substituirá toda ocorrência desta palavra no programa pelo valor correspondente, *antes* da compilação.

Uma variação interessante do problema calcula a média apenas de números positivos e a entrada de um número negativo serve para finalizar o fim da entrada. O código seguinte resolve o problema.
```c
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
```
Observe como a variável `contador` é usada para contar a quantidade de números válidos lidos e como ela é usada como limitante da varredura do vetor no segundo `for`. Observe também como o `break` é utilizado para interromper o `for`.

## Exercícios
!!! question "Exercício"
    Escreva um programa que leia 10 números e imprima o menor e o maior entre eles (não é necessário usar vetores aqui).

!!! question "Exercício"
    Escreva um programa que leia 10 números e calcule e imprima a média e desvio padrão dos mesmos. Lembre-se que o desvio padrão é definido como a raiz quadrada dos quadrados das diferenças dos valores para a média dos valores.

!!! question "Exercício"
    Escreva um programa que leia 11 números reais e imprima os valores dos 10 primeiros multiplicados pelo 11-ésimo. 
    Por exemplo, se os valores digitados foram 1, 2, 3 ,4 ,5 ,6, 7, 8, 9, 10 e 1.1, então seu programa deve imprimir 1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9 e 11.0.

## Laboratório
!!! example "Laboratório"
    Escreva um programa que leia um número inteiro `n` e então leia `n` números reais. Em seguida, seu programa deve imprimir a média e desvio padrão dos números lidos. Seu programa deve **ignorar** números negativos.

!!! example "Laboratório"
    Escreva um programa que leia `n` números reais e imprima seus valores na tela. Em seguida, leia mais um número real `x` e imprima o valor dos `n` números multiplicados `x`.

!!! example "Laboratório"
    Escreva um programa que leia `n` booleanos e imprima seus valores na tela. Em seguida, imprima todos os booleanos invertidos, na linha seguinte.
