# Estruturas Não-Homogêneas

## Introdução
Imagine que você deseje armazenar informações sobre um funcionário de uma empresa. Entre estas informações podemos ter, por exemplo, nome, endereço, telefone, sexo, estado civil, cargo, setor e salário. 
Em um programa, isto seria representado por oito variáveis apenas para um funcionário. Se
você desejar incluir mais informações, isto implicará em mais variáveis, aumentando a complexidade do programa. 

Por esta razão, em muitas aplicações, é importante a capacidade de se tratar todas as
informações de uma entidade (uma pessoa, por exemplo), como sendo uma única unidade de
armazenamento, ou seja, uma única variável. 
Por outro lado, deve ser possível, que esta única variável permita acesso a cada informação em separado.
Outros exemplos de informação com esta característica é o endereço, que pode ser decomposto em:
logradouro, número, complemento, CEP, cidade, estado, país.

Neste tipo de informação é possível observar que, diferentemente de variáveis indexadas (vetores e matrizes), não há homogeneidade quanto ao tipo de dados tratado.  Por isso, deve haver um mecanismo para trabalhar com variáveis estruturadas heterogêneas, também conhecidas simplesmente como *estruturas* ou *structs*.

## Declaração
Na linguagem C, a palavra reservada `struct` é destinada à declaração de variáveis não-homogêneas, e seu uso segue a seguinte sintaxe:

```
struct identificador{
	tipo_campo_1 nome_campo_1;
	...
	tipo_campo_n nome_campo_n;
};
```

Em primeiro lugar, cada estrututura tem um identificador, usado na declaração de variáveis do tipo desta estrutura. Em seguida, são declarados os campos da estrutura, especificadas entre as chaves. Os campos podem ter qualquer tipo, inclusive ser outra estrutura. O exemplo a seguir declara uma estrutura para o armazenamento de endereços e várias variáveis deste tipo.

```c
struct endereco {
  char logradouro[15];
  int numero;
  char complemento[6], bairro[10];
  char cidade[10], estado[3], pais[10];
};
...
struct endereco e1, e2, e3;
```

O uso da palavra reservada `struct` é obrigatório na declaração de variáveis, pois ela faz parte do tipo da variável. O uso repetido desta palavra reservada pode "poluir" o código, e por essa razão recomenda-se a definição de novos tipos baseados na estrutura.

### `typedef`
A palavra chave `typedef` permite que se defina novos tipos de dados a partir de tipos já existentes. Por exemplo, é possível definir um tipo "numero_real" ou um tipo "caractere". A sintaxe para o uso `typedef` é a seguinte:

```
typedef tipo_antigo tipo_novo;
```

Os exemplos apenas dados são implementados assim:
```c
typedef float numero_real;
typedef char caractere;
```

Mais importante, é possível definir um tipo basedo na estrutura. Neste caso, há duas formas de fazê-lo. O exemplo a seguir mostra a mais verborrágica.

```c
struct end{
  char logradouro[15];
  int numero;
  char complemento[6], bairro[10];
  char cidade[10], estado[3], pais[10];
};
...
typedef end endereco;

endereco e1, e2, e3;
```

Embora mais explícita, esta forma não é usada normalmente, em função forma mais compacta a seguir.

```c
typedef struct{
  char logradouro[15];
  int numero;
  char complemento[6], bairro[10];
  char cidade[10], estado[3], pais[10];
} endereco;
...
endereco e1, e2, e3;
```

## Acesso aos Campos de Uma Estrutura
Embora as estruturas agreguem vários campos, com raras exceções, o manuseio da mesma deve ser feito campo a campo, como variáveis normais.
Para acessar um dos campos de uma estrutura, usa-se o operador '.' (ponto). Diferentemente de variáveis indexadas, variáveis do tipo estrutura podem receber o valor de outra do mesmo tipo (desde que nenhum dos campos seja vetor). Por exemplo:
```c
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
```

## Exemplo
Considere a estrutura `complexo`, a qual representa um número imaginário na forma $a + b × i$, em que o valor de $a$ é armazenado na variável `real` e o valor de $b$ é armazenado na variável `imag`. O exemplo a seguir apresenta uma matriz de $3 × 3$ em que cada elemento é do tipo `complexo`.

```c
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
```

## Exercícios
### 
Faça um programa que leia informações sobre 15 pessoas. Essa informação deve ficar em um vetor de variáveis do tipo estruturado `pessoa`, o qual deve conter as seguintes informações:
- Nome: string de tamanho 30;

- Sexo: tipo enumerativo com os valores `masc`, `fem`;

- Idade: valor inteiro;

- Estado Civil: tipo enumerativo com os valores `solteiro`, `casado`, `separado`, `viúvo`.

- Salário: valor real.
Em seguida, imprima o número de homens, número de mulheres e informações da pessoa com maior salário.

### 
Faça um programa que leia o nome, duas notas e número de faltas de 10 alunos. As informações desses alunos devem ser armazenadas em um vetor de variáveis do tipo estruturado `aluno`, o qual deve conter as seguintes informações de cada aluno:
      - Nome: string de tamanho 30;

- Média: número real resultado da média das duas notas lidas;

- Situação: caractere representando situação, isto é, 'A' (Aprovado), se média maior ou igual a 6 e número de faltas menor que 10, e 'R' (Reprovado), caso contrário.

- Faltas: número de faltas (valor inteiro).
      Por fim, devem ser impressas as informações de cada aluno.

## Laboratório
Primeiramente, implemente sua solução para o exercício anterior. Em seguida, implemente duas funções, que ordenem os dados das pessoas por Nome e Idade, e imprimam todos os dados na tela. Finalmente, demonstre o uso destas funções.

## Estruturas e funções
Estruturas são utilizadas em funções da mesma forma que os tipos básicos que vimos 
(`int, float, char`, ...). Veja o exemplo a seguir:
```c
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
```

De maneira análoga, vetores de estruturas devem ser utilizados da mesma forma que vetores dos tipos
básicos:

```c
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
```

## Laboratório
!!! example "Laboratório"
    Considerando a estrutura:
    ```c
    struct Ponto {
      int x;
      int y;
    };
    ```
    para representar um ponto em uma grade 2D, implemente uma função que indique se
    um ponto `p` está localizado dentro ou fora de um retângulo. O retângulo é definido
    por seus vértices inferior esquerdo `v1` e superior direito `v2`. A função deve retornar 1
    caso o ponto esteja localizado dentro do retângulo e 0 caso contrário.

!!! example "Laboratório"
    Faça um função que recebe um valor em segundos e retorna o valor equivalente para o tipo horário,
      o qual é composto por hora, minuto e segundos. Em seguida imprima os campos da estrutura
      retornada.

!!! example "Laboratório"
    Crie a estrutura baralho, baseado em um “baralho tradicional” (cada carta tem seu naipe e seu
      valor). Implemente uma função que faça parte de distribuição (sorteio) de cartas para 2 jogadores,
      considerando que cada jogador irá receber 5 cartas. Exiba na tela as cartas que cada um dos
      jogadores recebeu.

!!! example "Laboratório"
    Faça um programa que controla o consumo de energia dos eletrodomésticos de uma casa. Leia um
      inteiro `n` e, utilizando funções auxiliares:
      - Crie e leia `n` eletrodomésticos que contém nome (máximo 15 letras), potencia (real, em kW)
          e tempo ativo por dia (real, em horas).
    
    - Leia um tempo `t` (em dias), calcule e mostre o consumo total na casa e o consumo relativo
          de cada eletrodoméstico (consumo/consumo total) nesse período de tempo. Apresente este último
          dado em porcentagem.
