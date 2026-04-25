# Repetição (I)

Em certas situações é necessária a repetição de um conjunto de comandos. Em situações como esta, temos duas opções: ou copiamos e colamos todo o trecho que desejamos repetir, fazendo os ajustes necessários; ou utilizamos uma saída mais inteligente por meio de comandos especiais que permitem automatizar a repetição. Neste capítulo veremos o comando de repetição `while` e alguns exemplos de seu uso.

## Motivação
Suponha de você deseja fazer um programa para ler duas notas, calcular e imprimir a média de dez alunos da disciplina. A maneira menos prática de fazer isso seria:

```c
...
float nota1, nota2, media;
cout << "Entre nota 1 e nota 2 do aluno 1: " << endl;
cin >> nota1 >> nota2;
media = (nota1 + nota2) / 2;
cout << "A media das notas eh " << media << endl;
cout << "Entre nota 1 e nota 2 do aluno 2: " << endl;
cin >> nota1 >> nota2;
media = (nota1 + nota2) / 2;
cout << "A media das notas eh " << media << endl;
cout << "Entre nota 1 e nota 2 do aluno 3: " << endl;
cin >> nota1 >> nota2;
media = (nota1 + nota2) / 2;
cout << "A media das notas eh " << media << endl;
cout << "Entre nota 1 e nota 2 do aluno 4: " << endl;
cin >> nota1 >> nota2;
media = (nota1 + nota2) / 2;
cout << "A media das notas eh " << media << endl;
cout << "Entre nota 1 e nota 2 do aluno 5: " << endl;
cin >> nota1 >> nota2;
media = (nota1 + nota2) / 2;
cout << "A media das notas eh " << media << endl;
cout << "Entre nota 1 e nota 2 do aluno 6: " << endl;
cin >> nota1 >> nota2;
media = (nota1 + nota2) / 2;
cout << "A media das notas eh " << media << endl;
cout << "Entre nota 1 e nota 2 do aluno 7: " << endl;
cin >> nota1 >> nota2;
media = (nota1 + nota2) / 2;
cout << "A media das notas eh " << media << endl;
cout << "Entre nota 1 e nota 2 do aluno 8: " << endl;
cin >> nota1 >> nota2;
media = (nota1 + nota2) / 2;
cout << "A media das notas eh " << media << endl;
cout << "Entre nota 1 e nota 2 do aluno 9: " << endl;
cin >> nota1 >> nota2;
media = (nota1 + nota2) / 2;
cout << "A media das notas eh " << media << endl;
cout << "Entre nota 1 e nota 2 do aluno 10: " << endl;
cin >> nota1 >> nota2;
media = (nota1 + nota2) / 2;
cout << "A media das notas eh " << media << endl;
...
```

Este código tem vários problemas. Primeiro, ele é mais propenso a erros; se, por exemplo, você resolve renomear a variável `nota2` para `notab`, você terá que fazê-lo em diversos pontos do programa, aumentando a possibilidade de esquecer algum.
Em segundo lugar, o código exigiu grande retrabalho, isto é, a repetição de uma mesma tarefa por parte do programador.
Finalmente, se você precisar aumentar a quantidade de repetições para, digamos, 100 alunos, terá que estender o código por páginas e páginas.

Para evitar tais problemas, para estas situações a linguagem C(++) fornece estruturas de repetições, as quais permitem repetir um determinado conjunto de comandos.

## O comando `while`
Um destes comandos é o comando `while` (enquanto, em português). Sua forma geral é muito simples:

```c
while (<condicao>)
{
	// bloco de comandos a ser repetido
}
```

O bloco de comandos entre as chaves será repetido **enquanto a condição dentro dos parênteses for verdadeira**.

Utilizando o `while`, o exemplo anterior pode ser reescrito de maneira bem mais prática:

```c
...
float nota1, nota2, media;
int i = 1;  // valor inicial do identificador do aluno

while (i <= 10)
{
	cout << "Entre nota 1 e nota 2 do aluno: " << endl;
	cin << nota1 << nota2;
	media = (nota1 + nota2) / 2;
	cout << "A media das notas eh " << media << endl;
	i = i +1; // aumentamos o valor de i no final de cada calculo da media
}
...
```

Observe as seguintes modificações:
- Uma nova variável, `i`, foi criada para contabilizar o número de alunos.

- Esta variável é inicializada com o valor 1, representando o primeiro aluno.

- A condição dentro do comando de repetição será verdadeira enquanto o valor de `i` for menor ou igual a 10.

- Por este motivo, devemos incrementar o valor de `i` ao fim de cada ciclo.

Normalmente, a variável que conta a quantidade de iterações executadas, `i` no exemplo dado, é chamada de contadora. No exemplo, a variável contadora foi usada apenas para este fim, contar, e não aparece no bloco de comandos sendo repetido. Isto nem sempre é o caso, como veremos em outros exemplos. Antes, porém, vejamos uma variação do `while`.

## O comando `do-while`
Se por acaso a condição verificada no `while` for inicialmente falsa, o bloco não será repetido nem mesmo uma vez. Para situações em que é preciso executar o bloco pelo menos uma vez, uma variação do comando `while` é fornecida pela linguagem C. Trata-se do comando `do-while` (faça-enquanto ou repita-enquanto, em português). Sua forma geral é dada por:
```c
do
{
	\\ bloco de comandos
	\\ a ser repetido
}
while (<condicao>);
```

O mesmo exemplo anterior pode ser reescrito utilizando este comando:

```c
do {
	cout << "Entre nota 1 e nota 2 do aluno : " << endl;
	cin >> nota1 >> nota2;
	i = 1+1; // aumentamos o valor de i no final de cada calculo da media
	media = (nota1 + nota2) / 2; 
	cout << "A media das notas eh " << media << endl;
}
while (i <= 10);
```

Em comparação ao comando `while`, a única diferença existente é o fato do teste da condição ser feito após a execução do bloco de comandos que se deseja repetir. Uma implicação disto é que, em casos em que a condição é falsa logo no primeiro teste, o bloco de comandos é executado com `do-while`, mas não é executado com `while`. Isto aconteceria para a variável `i` com valor inicial de 11, por exemplo.

## Mais exemplos
Considere que deseja-se somar todos os números pares entre 1 e 999. Ou fazemos uma soma com todos os valores em uma linha enorme, ou utlizamos o que apresendemos sobre comandos de repetição. Utilizando o `while`, teríamos:

```c
...
int n = 2, // primeiro par maior do que 1
    soma = 0; // soma inicialmente zerada
while (n < 999)
{
	soma = soma + n;
	n = n + 2;
}
cout << "O valor da soma eh " << soma << endl;
...
```

Observe que a cada iteração o valor de soma é acrescido do próximo número par, o qual é obtido somando-se 2 ao valor de `n`.

Imagine que se deseja obter o maior entre 10 números inteiros lidos. Utilizando o `do-while`, uma possível solução seria:

```c
...
int i = 0, // contador da qtde de numeros lidos
    maior,
    n; 
do
{
	cout << "Entre um numero: ";
	cin >> n;
	if (i == 0) // se for o primeiro numero lido
	{           // ele sera o menor
		maior = n;
	}
	else        // a partir do segundo
	{
		if(n > maior) // atualizo o maior
		{
			maior = n;
		}
	}
    i = i + 1;
}
while (i < 10);
...
```

Neste exemplo temos uma situação especial em que, no primeiro caso (`i = 0`), o maior valor é o único valor lido. A partir do segundo número, se o número lido for maior do que o valor armazenado na variável `maior`, esta será atualizada.

Em outro exemplo, imagine que queira ler números até que leia um número maior que 100. Neste caso, o seguinte programa resolveria nosso problema.

```c
...
int num; 
do
{
	cout << "Entre um numero: ";
	cin >> num;
}
while (! num > 100);
...
```

Neste exemplo utilizamos `do-while` pois é necessário ler pelo menos um número. Reescreva o código utilizando `while` e veja como fica, necessariamente, mais complexo.

### Operadores de incremento e outras construções especiais
Nos exemplos apresentados, a variável contadora foi manipulada em todas as repetições de uma forma bem comum, sendo incrementada de 1 em 1 ou de 2 em 2. Repetições tem esta característica, embora as operações aplicadas aos contadores não sejam sempre simples incrementos e decrementos. Com a finalidade de agilizar o desenvolvimento e simplificar algumas operações aritméticas mais comuns, a linguagem C(++) permite algumas construções especiais envolvendo operadores. Considere o seguinte trecho de código:
```c
int a, b;
...
a = a + b;
b = b * 2;
a = a / 7;
```

Observe que nas três atribuições (indicadas pelo sinal de igualdade), as variáveis que são atualizadas também aparecem como primeiro elemento da operação aritmética à esquerda. Nestas situações, podemos reescrever as atribuições assim:
```c
int a, b;
...
a += b;
b *= 2;
a /= 7;
```

As operações de incremento (aumento de uma unidade) e o decremento (diminuição de uma unidade) de uma variável são muito comuns em programação. Sendo assim, a linguagem C define dois operadores para as mesmas: `++` e `--`, respectivamente. Veja o exemplo.

```c
int a = 0;
a = a + 1;
cout << "a = " << a << endl;
a += 1;
cout << "a = " << a << endl; 
a++;
cout << "a = " << a << endl; 
a--;
cout << "a = " << a << endl;
```

O trecho acima deve imprimir os valores de `a`, ou seja, 1, 2, 3 e 2.

## Exercícios
!!! question "Exercício"
    Diga o que será escrito na tela durante a execução do
    seguinte trecho de código:
    ```c
    int a, b = 0, c = 0;
    a = ++b + ++c;
    cout << a << ", " << b << ", " << c << endl;
    a = b++ + c++;
    cout << a << ", " << b << ", " << c << endl;
    a = ++b + c++;
    cout << a << ", " << b << ", " << c << endl;
    a = b-- + --c;
    cout << a << ", " << b << ", " << c << endl;
    ```
<!-- TODO: Incluir exercícios mais simples como os da lista 1 do Prof. Anilton. -->

Faça os exercícios a seguir à mão.

!!! question "Exercício"
    Faça uma função que recebe um número inteiro positivo e retorna o fatorial deste número. A função principal deve ler o número do qual se deseja calcular o fatorial e imprimir o resultado.

!!! question "Exercício"
    Faça uma função que recebe um número inteiro positivo e retorna `true` se o número for primo ou `false`, caso contrário. A função principal (`main`) deve ler o número e imprimir o resultado.

!!! question "Exercício"
    Modifique o programa anterior para imprimir todos os números primos abaixo de dois milhões.

!!! question "Exercício"
    Faça um programa que leia um número inteiro positivo e imprima esse número de trás pra frente.
    A impressão deve ser feita pela função auxiliar `inverteNumero`.

## Laboratório
!!! example "Laboratório"
    Implemente os exercícios acima no Code::Blocks.

!!! example "Laboratório"
    Escreva uma função que receba dois parâmetros inteiros, $x$ e $y$, $x < y$ e que imprima $y$ pontos na tela e que a cada $x$ pontos, imprima um acento circunflexo.

!!! example "Laboratório"
    
    O exercício pedia que você escrevesse uma função que gerasse um menu na tela. A função que você escreveu tinha um problema: ela aceitava qualquer valor, mesmo algum não correspondendo a nenhuma opção do menu.
    
    Usando `do-while`, altere sua função para que continue exibindo o menu e lendo uma opção até que uma opção válida seja digitada pelo usuário.

!!! example "Laboratório"
    Implemente uma função chamada `pot` que receba um número real e um inteiro, respectivamente `base` e `expoente`, como parâmetros e que calcule {$`base`^`expoente`$}. 
    
    A função `pot`, que você implementará, deve usar multiplicações sucessivas para calcular seu resultado (isto é, é proibido o uso da função `pow`).

!!! example "Laboratório"
    Execute o seguinte programa em seu computador e observe o que acontece.
    
    ```c
    ...
    int num = 10; 
    do
    {
    	cout << num;
    	num *= 2;
    }
    while (1);
    ...
    ```
    À propósito, para terminar um programa basta digitar a combinação de teclas `ctrl+c`.

!!! example "Laboratório"
    Escreva um programa que leia um numero inteiro positivo `n` e em seguida imprima `n` linhas do chamado Triângulo de Floyd:
    ```
     1
     2  3
     4  5  6
     7  8  9 10
    11 12 13 14 15
    16 17 18 19 20 21
    ```
!!! example "Laboratório"
    Faça um programa que gera um número inteiro aleatório de 1 a 1000 em uma função denominada `geraNumero`. Na função principal, o usuário deve tentar acertar qual o número foi gerado. A cada tentativa o programa deverá informar se o chute é menor ou maior que o número gerado. O programa acaba quando o usuário acerta o número gerado. O programa deve informar em quantas tentativas o número foi descoberto.

!!! example "Laboratório"
    Escreva um programa que receba como entrada o valor do saque realizado pelo cliente de um banco e retorne quantas notas de cada valor serão necessárias para atender ao saque com a menor quantidade de notas possível. Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 reais. O cálculo e impressão do resultado deve ser efetuado por uma função auxiliar denominada `imprimeNotas`.
