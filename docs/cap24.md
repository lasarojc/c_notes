# Navegação dentro do arquivo
Embora seja possível trabalhar com arquivos usando apenas as ferramentas apresentadas até agora,
alguns problemas são de difícil resolução, a não ser que extendamos nosso conhecimento.

Suponha por exemplo que você tenha o seguinte arquivo:

```
O rato roeu a roupa do
rei de Roma e a rainha
Ruinha resolveu rir-se
pois o rei que remente
suas roídas roupagens.
```

Observe que todas as linhas tem o mesmo tamanho (22 caracteres) e que a palavra "remende" está
escrita de forma incorreta. Para corrigir esta palavra, podemos reescrever toda a frase, ou
posicionar o cursor do arquivo exatamente sobre o caractere errado e corrigi-lo. Há várias formas de
se fazer isso, como veremos agora.

## Posicionamento no arquivo
Como visto no capítulo anterior, operações de leitura e escrita no arquivo vão mudando a posição em
que as próximas operações serão executadas. Isto é, se considerarmos que há um cursor dentro do
arquivo, na posição em escreveremos, caso uma escrita seja feita, ou leremos, caso uma leitura seja
executada, então se lermos ou escrevermos 3 caracteres, então o cursor "andará" 3 caracteres. Se
quisermos colocar o cursor no fim do arquivo, podemos reabrí-lo usando `ios::app`. Caso
queiramos colocar o cursor no começo do arquivo, podemos simplesmente reabri-lo sem especificar
qualquer opção ou usando `ios::trunc` (e com isso também zerarmos nosso arquivo). 

Caso precisemos posicionar o cursor no meio do arquivo, podemos usar a função `seekg`, que
pode ser usada duas formas:

```
seekg(nova posição [em bytes])

seekg(diferença [em bytes] em relação ao marco, marco)
```

Na primeira forma você pode especificar onde o cursor deve ser posicionado em relação ao início do
arquivo, em número de bytes. Por exemplo, `arq.seekg(10)` posiciona o cursor no décimo
byte do arquivo `arq`. Já pela segunda forma, você especifica onde posicionar o cursor em
relação a um marco no arquivo, que pode ser seu início (`ios_base::beg`), fim
(`ios_base::end`), ou posição atual (`ios_base::cur`). A diferença em relação ao
marco é especificada como um inteiro com sinal. Por exemplo,
`arq.seekg(-10,ios_base::end)` posiciona o cursor no décimo caractere *antes do fim*
do arquivo `arq`.

Para resolver o problema apresentado acima, podemos então usar as seguintes soluções.

```c
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
```

## Arquivos formatados
Para que se possa movimentar o cursor dentro de um arquivo, é importante que se conheça a estrutura
do mesmo, principalmente se pretender sobrescrevê-lo sem destruí-lo. Por exemplo, considere o
seguinte problema.

Escrever um programa que leia matrícula e nome de alunos do curso de Engenharia Química e armazene
estas informações em um arquivo. Em seguida, seu programa deve escrever todas as informações na
tela, precedidas por um número identificando cada aluno. Finalmente, o programa deve ler números
correspondentes a alunos e sobrescrever os dados do aluno com novas informações.

```c
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
```

Este código possui duas particularidades. Primeiro, ele usa a função `arq.clear()`, ainda
não mencionada e, segundo, ele está errado.

Toda vez que o arquivo é lido até o seu fim, seu estado interno é mudado para identificar o fato.
Isto é verificável pela função `arq.eof()`, que testa se o arquivo chegou ao *end of
file*. Quando isso é verdade, as funções de reposicionamento não funcionarão, a não ser que este
status seja reiniciado, o que é feito com a função `clear()`. No código simplesmente
usamos esta função sempre que formos fazer um *seek*, por simplicidade.

Sobre o código não funcionar como esperado, execute-o e insira um aluno apenas, com matrícula
"aaaaaaaaaa" e nome "bbbbbbbbbb". Em seguida, altere os dados da linha 1 e insira matrícula "cc" e
nome "dd". Ao final, os dados impressos serão os seguintes:

```
Dados atuais
1 - cc dd
2 - aaaa bbbbbbbbbb
```

## Exercícios
### 
Corrija o programa exemplo mostrado acima para que escreva sempre linhas de um mesmo tamanho e que,
portanto, não tenha o problema de fragmentação de registros.

| ios::ate | Posiciona no fim do arquivo. Se não for usado, é posicionado no início. |
| --- | --- |

## Arquivos binários
| ios::binary | Modo não formatado. (Próximo capítulo) |
| --- | --- |

O argumento `nome_do_arquivo` é o caminho do arquivo que se deseja abrir, e
`modo_de_abertura` representa como o arquivo será aberto, de acordo com a tabela a seguir:

  
    | **Modo** | **Descrição** |
| --- | --- |
| r | Abre arquivo texto somente para leitura |
| w | Cria arquivo texto somente para escrita |
| a | Anexa dados a um arquivo texto |
| r+ | Abre arquivo texto para leitura e escrita |
| w+ | Cria arquivo onde poderão ser realizadas leituras e escritas |
| a+ | Anexa dados a um arquivo texto ou cria um para leitura e escrita |
  *Modos de abertura de arquivo texto em C.*

  

      
#### Fechamento de Arquivo
Um arquivo aberto sempre deve ser fechado antes do fim do programa. A função que realiza essa tarefa
é `fclose`. Seu protótipo é:

`int fclose(FILE *arq);`

O argumento `arq` é a variável que representa o arquivo aberto (com `fopen`)
O retorno dessa função é zero em caso de sucesso. Qualquer valor diferente de zero, significa erro.

#### Leitura e Escrita de Arquivo
A função `fputc` escreve um caractere em um arquivo. Seu protótipo é:
      `int fputc(char ch, FILE *arq);`

A função `fputs` escreve um cadeia de caracteres em um arquivo. Seu protótipo é:
      `char *fputs(char *cadeia, FILE *arq);`

A função `fgetc` lê um caractere em um arquivo. Seu protótipo é:
      `int fgetc(FILE *arq);`

A função `fgets` lê um cadeia de caracteres em um arquivo. Seu protótipo é:
      `char *fgets(char *cadeia, int tam, FILE *arq);`, onde `tam` define o tamanho
      da cadeia que será lida: tam-1 ou fim de linha, o que ocorrer primeiro.

A função `fprintf` permite escrever em um arquivo da mesma forma que escrevemos na tela
com o `printf`. Seu protótipo é:
      `int fprintf(FILE *arq, char *formato, ...);`

A função `fscanf` lê informações de um arquivo da mesma forma que lemos do teclado com o
`scanf`. Seu protótipo é:
      `int fscanf(FILE *arq, char *formato, ...);`

#### Exemplos
 ```c
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
```

```c
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
```

# Part: Avançado: Estruturas de dados
