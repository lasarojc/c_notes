# Arquivos

Muitas vezes desejamos guardar o resultado de alguma computação para consulta posterior. Imagine, por exemplo, que você fez um programa que calcula a média final e situação de toda a turma. Se o resultado deste processamento não puder ser armazenado, toda vez que for necessário consultar a situação de algum aluno, o programa deverá ser executado e todos os dados inseridos novamente. 
Para solucionar este problema, o usuário pode salvar resultados de computação em uma estrutura persistente. Esta estrutura de dados manipulada fora do ambiente do programa (memória principal) é conhecida como **arquivo**.  

Um arquivo é armazenado em um dispositivo de memória secundária (CD, DVD, disco rígido, pendrive) e pode ser lido ou escrito por um programa. Em C, um arquivo pode representar diversas coisas, como documentos, uma impressora, um teclado, ou qualquer dispositivo de entrada ou saída.  Consideraremos apenas dados  em disco, iniciando por dados na forma textual.

## Arquivos de texto
Nesta seção estudaremos apenas arquivos texto, ou seja, arquivos que contêm apenas caracteres e podem ser visualizados em editores de textos como Notepad, Gedit, Vim, etc.

A linguagem C++ dá suporte à utilização de arquivos por meio da biblioteca `fstream`. Esta biblioteca fornece várias funções para manipulação de arquivos e define alguns tipos de dados para serem usados especificamente com arquivos.  O principal tipo definido nessa biblioteca que será usado é o tipo `fstream`.  Um variável do tipo `fstream` é capaz de identificar um arquivo no disco, direcionando-lhe todas as operações.  Essas variáveis são declaradas da seguinte
maneira:

`fstream arq;`

### Abertura e Fechamendo de Arquivos
Antes que o arquivo seja manipulado, é preciso abrí-lo, o que é feito via "função" `open` do arquivo. Uma vez aberto, o arquivo funciona como o `cin`  e `cout`, com os quais você já está acostumado a usar `<<` e `>>`, como no exemplo a seguir. Ao terminar o uso do arquivo, é importante fechá-lo, para garantir que tudo que, em teoria, está escrito no arquivo, realmente foi colocado no disco.

```c
#include <iostream>
#include <fstream>
using namespace std;

int main () {
  fstream arquivo;
  arquivo.open ("arquivo.txt");
  arquivo << "O que eu deveria escrever neste arquivo?" << endl;
  arquivo.close();
  return 0;
}
```

Nem sempre é possível abrir o arquivo como no exemplo, o que será explicado adiante. Para testar se o arquivo foi aberto ou não, use a função `is_open()`. É importante que você teste se o arquivo realmente está aberto, antes de tentar usá-lo.

```c
#include <iostream>
#include <fstream>
using namespace std;

int main () {
  fstream arquivo;
  arquivo.open("arquivo.txt");
  
  if(arquivo.is_open())
  {
     arquivo << "O que eu deveria escrever neste arquivo?" << endl;
     arquivo.close();
     cout << "tudo escrito";
  }
  else
     cout << "falhou";
     
  return 0;  
}
```

Se você tentou executar o código acima, percebeu que a mensagem "falhou" foi escrita na tela. O problema é que o código abre um arquivo e escreve no mesmo, mas somente se ele já existir, o que não é o caso. Por enquanto, vá até a pasta onde está o seu projeto e crie o arquivo manualmente. Na seção seguinte veremos como criar um arquivo "de dentro" do programa. Já no código a seguir, veja como os dados do arquivo podem ser lidos.

```c
#include <iostream>
#include <fstream>
using namespace std;

int main () {
  fstream arquivo;
  arquivo.open ("arquivo.txt");

  if(arquivo.is_open())
  {
    cout << "yeah";
    arquivo << "Sera que isso foi escrito?" << endl;
    arquivo.close();
    
    arquivo.open ("arquivo.txt");
    char str[1000];
    arquivo.getline(str,1000);
    arquivo.close();

    cout << str;  
  }
  else
    cout << "O arquivo nao foi aberto";

  return 0;
}
```

### Criação de Arquivos
Para abrir um arquivo que não existe, ou seja, criar o arquivo, é necessário passar um conjunto especial de instruções para a função de abertura. Infelizmente, o único jeito de passar estas instruções é bem mais complicado do que o que vimos até agora. Veja o seguinte código, em especial a linha que abre o arquivo.

```c
#include <iostream>
#include <fstream>
using namespace std;

int main () {
  fstream arquivo;
  arquivo.open ("arquivo.txt", ios::out | ios::in | ios::trunc);

  if(arquivo.is_open())
    cout << "yeah";
  else
    cout << "nope";

  arquivo << "O que eu deveria escrever neste arquivo?" << endl;
  arquivo.close();

  arquivo.open ("arquivo.txt");
  char str[1000];
  arquivo.getline(str,1000);
  arquivo.close();

  cout << str;

  return 0;
}
```

Na frente do parâmetro com o nome do arquivo, na função `open`, foram passadas três opções para o modo de abertura do arquivo, que especifica o tipo de operações que se intende fazer no arquivo (o caractere `|` combina as opções passadas). Algumas das opções possíveis são:

- ios::in		--	 Operações de escrita.

- ios::out 	--	 Operações de leitura.

- ios::app	--	 Posiciona no fim do arquivo. Não pode ser reposicionado. Não pode ser usado com ios::in.

- ios::trunc	--	 Posiciona no início do arquivo. Se o arquivo já existe, então seu conteúdo anterior é perdido.

As opções para leitura e escrita do arquivo, e somente estas, são implícitas, quando nenhuma opção é especificada. Se você quiser, pode usar apenas uma destas por questões de segurança (o arquivo pode ser lido mas não escrito, ou o arquivo pode ser aumentado mas não lido). Usando somente as opções de leitura e escrita, contudo, o arquivo não é criado caso não exista. Para que seja criado, é necessário que se especifique ou `ios::trunc`  ou `ios::app`, que farão com que o arquivo seja ou truncado ou que toda modificação seja adicionada ao fim do arquivo (*append*).

### Cuidados com a Formatação dos Dados
Quando se escreve um dado em um arquivo de texto, precisa-se entender que o dado ocupa somente o espaço que você especificar. Isto é, se você escrever a sequência de caracteres "C(++) é bom!!!", 14 caracteres serão escritos, e pronto. Se escrever algo na linha seguinte depois resolver mudar a string acima para "C(++) não é bom!!!", então a divisão entre as linhas (o `endl`) terá sido sobrescrito e as duas linhas se tornarão uma. Estes cuidados não precisam ser tomados agora, com os exemplos simples com os quais estamos lidando, mas nos próximos capitulos você terá que tomá-los. Assim, melhor que você já saiba sobre estes problemas desde agora.

```c
#include <iostream>
#include <fstream>
using namespace std;

int main () {
  fstream arquivo;
  arquivo.open ("arquivo.txt", ios::out | ios::in | ios::trunc);
  char str[1000];

  if(arquivo.is_open())
  {
        cout << "O arquivo foi aberto!";
        arquivo << "Escrevendo um numero pequeno:" << endl;
        arquivo << 10 <<endl;
        arquivo << "Numero pequeno escrito." << endl;

        cout << "Fechando o arquivo.";
        arquivo.close();

        cout << "Reabrindo o arquivo.";

        arquivo.open ("arquivo.txt");

        arquivo << "Escrevendo um numero pequeno:" << endl;
        arquivo << 10000 <<endl;

        cout << "Fechando o arquivo.";
        arquivo.close();

        cout << "Reabrindo o arquivo.";
        arquivo.open ("arquivo.txt");

        arquivo.getline(str,1000);
        cout << str;
        arquivo.getline(str,1000);
        cout << str;
        arquivo.getline(str,1000);
        cout << str;

        arquivo.close();
  }

  else
    cout << "nope";

  return 0;
}
```

## Laboratório
!!! example "Laboratório"
    Faça um programa que leia o nome e sobrenome de 30 alunos e armazene em um arquivo, de tal forma que o arquivo tenha um aluno por linha. Abra o arquivo usando um editor de textos qualquer, como o Notepad.

!!! example "Laboratório"
    Faça um programa que tente abrir um arquivo e, caso não consiga, tente criá-lo e abrí-lo. Com arquivo aberto, leia um vetor A de inteiros de tamanho 20 e guarde seus valores em um arquivo, um por linha. Em seguida, reabra o arquivo e leia os elementos para o vetor B, verificando se os valores foram gravados corretamente.

!!! example "Laboratório"
    Faça um programa em Linguagem C que receba do usuário um arquivo, e mostre na tela quantas linhas esse arquivo possui.
 
!!! example "Laboratório"
    Faça um programa que receba dois arquivos do usuário, e crie um terceiro arquivo com o conteúdo dos dois primeiros juntos (o conteúdo do primeiro seguido do conteúdo do segundo).
 
!!! example "Laboratório"
    Desenvolver um programa em C que lê o conteúdo de um arquivo e cria um arquivo com o mesmo conteúdo, mas com todas as letras minúsculas convertidas para maiúsculas. Os nomes dos arquivos serão fornecidos, via teclado, pelo usuário. A função que converte minúscula para maiúscula é o toupper(). Ela é aplicada em cada caractere da string.
 
!!! example "Laboratório"
    Faça um programa no qual o usuário informa o nome do arquivo, e uma palavra, e retorne o número de vezes que aquela palavra aparece no arquivo.
