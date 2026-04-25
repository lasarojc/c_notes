# Alocação Dinâmica
Por mais interessante que seja poder criar ponteiros para variáveis já existentes e passar
parâmetros por referência, o poder dos ponteiros só fica mesmo evidente quando se trabalha com
alocação dinâmica de memória.

Alocação dinâmica é a habilidade de se criar novas variáveis durante a execução do programa, sem que
elas tenham sido declaradas antes. Justamente por não terem sido declaradas antes da compilação,
estas variáveis alocadas dinamicamente não têm nomes e, assim, só podem ser acessadas por meio de
referências.

## Alocação Dinâmica de Tipos Simples
Existem várias formas de se alocar memória dinamicamente, todas elas via funções que retornam como
resultado uma referência para o começo da memória alocada, na forma de uma referência genérica.

A função mais simples para alocação de memória é a `malloc`. Esta função recebe como único
parâmetro o tamanho da memória a ser alocada, em bytes. Observe o seguinte código para alguns
exemplos.

```c
char *s1;
int *i1;
float *f1;

s1 = (char *) malloc(1);
i1 = (int *) malloc(4);
f1 = (float *) malloc(4);
```

No exemplo acima você percebe que antes de cada `malloc` há, entre parênteses, o tipo da
variável que guardará a referência. Isso é o que chamamos de *casting*, e serve para
transformar a referência genérica retornada pela função para o tipo de referência da variável.
**Este *casting* é obrigatório em seu código**.

Você também percebe que cada alocação especifica exatamente o tamanho do tipo para o qual estamos
alocando a memória. Isto é, 1 para caracteres e 4 para inteiros e números reais. Estes tamanhos,
contudo, podem variar de uma máquina/sistema operacional para outra, o que tornaria complicado
especificar tais tamanhos em cada invocação à `malloc`. É por isso que a linguagem C(++)
especifica o construto `sizeof`, que "descobre" o tamanho do tipo para você, conforme o
seguinte exemplo.

```c
char *s1;
int *i1;
float *f1;
double *d1;

s1 = (char *) malloc(sizeof(char));
i1 = (int *) malloc(sizeof(int));
f1 = (float *) malloc(sizeof(float));
d1 = (double *) malloc(sizeof(double));
```

## Alocação Dinâmica de Vetores
Como visto nos capítulos anteriores, a diferença entre referências para tipos simples e vetores é...
**nenhuma**! Isso quer dizer que podemos alocar vetores usando um código similar ao anterior,
alterando apenas a quantidade de memória alocada, como no seguinte exemplo.

```c
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
```

## Liberação de memória
Todos os exemplos mostrados até agora neste capítulo são incompletos. Isso por quê nenhum programa
que faça alocação dinâmica em C(++) pode ser completo sem que se faça a liberação da memória
alocada. Liberar ou "desalocar" a memória consiste simplesmente na invocação da função
`free`, passando-se como parâmetro a referência a ser desalocada. O uso de
`free` será exemplificado na próxima seção.

## Alocação Dinâmica de Estruturas
Assim como declarar uma referência para uma estrutura é tão simples quanto declarar uma referência
para um tipo primitivo(simples), alocar um vetor de estruturas dinamicamente é tão simples quanto
alocar um vetor de tipos primitivos dinamicamente. O exemplo a seguir mostra exatamente como alocar
um vetor com 10 estruturas do tipo definido.

```c
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
```

## Exercícios
### 
Escreva um programa que leia um numero inteiro N, aloque dinamicamente um vetor de N inteiros, leia cada um dos N inteiros, e imprima os N inteiros na tela.

### 
Escreva um programa que repita o seguinte procedimento X vezes: leia um numero inteiro N, aloque dinamicamente um vetor de N carateres, leia uma palavra de N caracteres, transforme todas as maiúsculas em minúsculas e vice-versa na palara e imprima o resultado na tela. X deve ser lido no início da execução do programa.

## Laboratório
### {} Implemente os exercícios acima.

### 
Escreva um programa que aloque um vetor de 100000 float e imprima os 10 primeiros e os 10 últimos (o lixo que estiver na memória).  (Se tudo funcionar, aumente o vetor para 1000000 e assim por diante. O objetivo neste laboratório é mostrar que a quantidade de memória disponível para seu programa é limitada, e que se extrapolada, seu programa incorrerá em um erro.)
