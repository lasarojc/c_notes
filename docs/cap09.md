# Repetição (II)
Você deve ter percebido que no uso de `do-while` e  `while` quase sempre seguimos os mesmos passos:
- declarar uma variável que sirva de controle para a iteração;

- iniciar a variável de controle (e possivelmente outras);

- verificar a condição para iteração

- executar iteração

- executar incremento/decremento (mudança da variável de controle)

A linguagem C tem um comando iteração que agrega todos estes passos, chamado `for`.

## `for`
Sua forma geral do comando `for` é a seguinte:
```c
for(DI; C; I)
{
	\\bloco de comandos a ser repetido
}
```

O comando `for` tem três partes em sua declaração, além dos comandos a serem repetidos.
- DI -- em DI variáveis podem ser **D**eclaradas e **I**niciadas. Variáveis já existentes também podem ter seus valores ajustados em DI;

- C -- C define a **C**ondição necessária à execução do bloco de comandos. *Enquanto* a condição for verdadeira, o bloco será executado.

- I -- comandos de modificação de variáveis, como **I**ncremento e decremento, são colocados diretamente na declaração do `for`. O comando é executado ao final de cada iteração.

A execução do `for` segue os seguintes passos:
1. Iniciação (execução de DI)

2. Avaliação (teste da condição em C)

3. Execução do bloco de comandos

4. Incremento

5. De volta ao passo 2

Considere o exemplo do capítulo anterior em que deseja-se somar todos os números pares entre 1 e 999. O código pode ser escrito, como vimos, usando `while`.

```c
...
int n = 2, // primeiro par maior do que 1
    soma = 0; // soma inicialmente zerada
while (n < 999)
{
	soma = soma + n;
	n += 2;
}
cout << "O valor da soma eh " << soma << endl;
...
```

O código equivalente, usando `for` é essencialmente o mesmo.

```c
...
int n, // primeiro par maior do que 1
    soma = 0; // soma inicialmente zerada
for (n = 2; n < 999; n += 2)
{
	soma = soma + n;
}
cout << "O valor da soma eh " << soma << endl;
...
```

O código, contudo, pode ser simplificado colocando-se a declaração da variável de controle no próprio `for`.

```c
...
int soma = 0; // soma inicialmente zerada
for (int n = 2; n < 999; n += 2)
{
	soma = soma + n;
}
cout << "O valor da soma eh " << soma << endl;
...
```

É possível declarar e iniciar mais de uma variável no DI, mas não é possível definir novas variáveis e iniciar outras já definidas. No exemplo abaixo, errado, a variável soma sendo iniciada no `for` é diferente da variável definida antes do comando, apesar do nome ser igual.

```c
...
int soma = 0; // soma inicialmente zerada
for (int n = 2, soma = 0; n < 999; n += 2)
{
	soma = soma + n;
}
cout << "O valor da soma eh " << soma << endl;
...
```

## Mais Exemplos
Também do capítulo anterior, imagine o exemplo em que se deseja obter o maior entre 10 números inteiros lidos. Utilizando o `for`, uma possível solução seria:

```c
...
int i, // contador da qtde de numeros lidos
    maior,
    n; 

cout << "Entre um numero: ";
cin >> n;
maior = n;

for(i = 0; i < 9; i++)
{
	cout << "Entre um numero: ";
	cin >> n;
	if(n > maior) // atualizo o maior
	{
		maior = n;
	}
}
...
```

Observe que a primeira leitura aconteceu fora do `for`.

## Declarações especiais
Em certas situações pode ser desejável omitir partes da declaração do `for`. Por exemplo, se as variáveis de controle já tiverem sido iniciadas ou, simplesmente, se não existirem, ou se não houver incremento a ser feito, então estas partes da declaração podem ser deixadas em branco. Por exemplo,

```c
int menu()
{
    int opcao = 0;
    
    for( ; opcao < 1 || opcao > 4 ; )
    {
        cout << "1 Soma" << endl 
             << "2 Media" << endl 
             << "3 Menor" << endl 
             << "4 Maior" << endl;

        cout << "Qual sua opcao? ";

	    cin >> opcao;
    }
    return opcao;
}
```

Observe que embora neste exemplo tanto DI quanto I estão vazias, isso não é necessário. Isto é, qualquer das partes da declaração podem estar vazias independentemente, inclusive a segunda parte.

## Alterando a repetição com o `break` e `continue`
Caso a segunda parte do comando esteja vazia, a repetição será executada *ad infinitum* ou até que seja interrompida. A interrupção de uma iteração pode ser feita usando-se o comando `break`. Veja o exemplo anterior reescrito para usar tal comando.

```c
int menu()
{
    int opcao;
    
    for(;;)
    {
        cout << "1 Soma" << endl 
             << "2 Media" << endl 
             << "3 Menor" << endl 
             << "4 Maior" << endl;

        cout << "Qual sua opcao? ";

	    cin >> opcao;
	    
	    if(opcao > 0 && opcao < 5)
	        break;
	    else
	    	cout << "Opcao invalida" << endl << endl;
    }

    return opcao;
}
```

Outra forma de se alterar o fluxo é via o comando `continue`, que faz com que a o restante do bloco de comandos seja ignorado e, conseqüentemente, incremento e condição sejam reavaliados. Por exemplo, reescrevendo o código acima para o usar o `continue`.

```c
int menu()
{
    int opcao;
    
    for(;;)
    {
        cout << "1 Soma" << endl 
             << "2 Media" << endl 
             << "3 Menor" << endl 
             << "4 Maior" << endl;

        cout << "Qual sua opcao? ";

	    cin >> opcao;
	    
	    if(opcao < 1 || opcao > 4)
	        continue;
	    
	    cout << "A opcao escolhida foi " << opcao;
	    break;
    }

    return opcao;
}
```

## Exercícios
!!! question "Exercício"
    Refaça os execícios do capítulo anterior usando `for`.

## Laboratório
!!! example "Laboratório"
    Refaça o laboratório do capítulo anterior usando `for`.

!!! example "Laboratório"
    Escreva uma função que receba dois parâmetros inteiros, X e Y, e imprima X linhas na tela, cada uma com Y ".".
    Por exemplo, se sua função for invocada com X igual 3 e Y igual 2, o resultado deveria ser o seguinte
    ```
    ..
    ..
    ..
    ```
!!! example "Laboratório"
    Escreva uma função que receba dois parâmetros inteiros, X e Y, e imprima de forma decrescente os números de X*Y até 1, em X linhas de Y números.
    Por exemplo, se sua função for invocada com X igual 4 e Y igual 3, o resultado deveria ser o seguinte
    ```
    12 11 10
    9 8 7
    6 5 4
    3 2 1
    ```
