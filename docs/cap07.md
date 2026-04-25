# Switch
Em diversas situações em programação, é necessário testar se uma determinada variável tem um dentre diversos possíveis valores. Nesta situação, embora seja possível usar vários `if`, outra solução nos é dada em linguagem C: o uso de `switch`.

## `switch-case-default`
Considere o problema de transformar o mês de uma representação numérica de uma data em sua representação textual. Isto é, transformar, por exemplo, 25/12/2012 em 25 de Dezembro de 2012. Uma possível solução para este problema, em C(++), é o seguinte.

```c
#include <iostream>

using namespace std;

int main()
{
    int dia, mes, ano;

    cout << "Dia? " <<endl;
    cin >> dia;

    cout << "Mes? " <<endl;
    cin >> mes;

    cout << "Ano? " <<endl;
    cin >> ano;

    cout << dia << " de ";

    if(mes == 1)
        cout << "Janeiro";
    else if(mes == 2)
        cout << "Fevereiro";
    else if(mes == 3)
        cout << "Marco";
    else if(mes == 4)
        cout << "Abril";
    else if(mes == 5)
        cout << "Maio";
    else if(mes == 6)
        cout << "Junho";
    else if(mes == 7)
        cout << "Julho";
    else if(mes == 8)
        cout << "Agosto";
    else if(mes == 9)
        cout << "Setembro";
    else if(mes == 10)
        cout << "Outubro";
    else if(mes == 11)
        cout << "Novembro";
    else if(mes == 12)
        cout << "Dezembro";
	else
		cout << "Hein?-zembro";
    cout << " de " << ano << endl;
    return 0;
}
```

Em vez de usar vários `if` e `else-if`, uma solução melhor seria usar `switch`, criado exatamente para tratar estas situações. A sintaxe do uso do `switch` é a seguinte.
`switch` (identificador)
{
`case` valor1: bloco_comandos1
`case` valor2: bloco_comandos2
...
`case` valorN: bloco_comandosN
`default`: bloco_comandos_default
}

- identificador: Identificador da variável a ser testada

- valor1: primeiro caso a ser testado

- bloco_comandos1: bloco de comandos a ser executado caso a variável tenha valor igual a valor1

- valor2: segundo caso a ser testado

- bloco_comandos2: bloco de comandos a ser executado caso a variável tenha valor igual a valor2

- ... outros casos a serem testados

- valor n: último caso a ser testado

- bloco_comandosN: bloco de comandos a ser executado caso a variável tenha valor igual a valorN

- default: um valor especial, que sempre "casa" com o valor da variável

- bloco_comandos_default: bloco de comandos a ser executado caso a variável "case" com default.

Usando `switch-case-default`, o exemplo acima pode ser reescrito assim.

```c
#include <iostream>

using namespace std;

int main()
{
    int dia, mes, ano;

    cout << "Dia? " <<endl;
    cin >> dia;

    cout << "Mes? " <<endl;
    cin >> mes;

    cout << "Ano? " <<endl;
    cin >> ano;

    cout << dia << " de ";

    switch(mes)
    {
    case 1:
        cout << "Janeiro";
    case 2:
        cout << "Fevereiro";
    case 3:
        cout << "Marco";
    case 4:
        cout << "Abril";
    case 5:
        cout << "Maio";
    case 6:
        cout << "Junho";
    case 7:
...
    case 11:
        cout << "Novembro";
    case 12:
        cout << "Dezembro";
    default:
        cout << "Hein?-zembro";
    }
    cout  << " de " << ano << endl;
    return 0;
}
```

Execute este código e digite, por exemplo, a data 1/1/2012 para ver que ele funciona "quase" corretamente. O problema, você deve ter observado, é que além de imprimir o nome do mês correto, o programa imprime também o nome de todos os meses subsequentes e o valor `default`.  Isso ocorre por que, na verdade, o `switch` começa a executar o bloco correspondente ao `case` com o valor da variável mas, a partir daí, executa todos os blocos a não ser que seja instruído a fazer diferente, o que é feito via a instrução `break`.

## `break`
A instrução `break` diz ao computador que pare de executar o `switch` no ponto em que é invocada. (Mais tarde veremos outros blocos no qual o `break` pode ser utilizado.) Sendo assim, podemos reescrever o programa mais uma vez para obter exatamente o comportamento da versão usando `if`.

```c
#include <iostream>

using namespace std;

int main()
{
    int dia, mes, ano;

    cout << "Dia? " <<endl;
    cin >> dia;

    cout << "Mes? " <<endl;
    cin >> mes;

    cout << "Ano? " <<endl;
    cin >> ano;

    cout << dia << " de ";

    switch(mes)
    {
    case 1:
        cout << "Janeiro";
        break;
    case 2:
        cout << "Fevereiro";
        break;
    case 3:
        cout << "Marco";
        break;
    case 4:
        cout << "Abril";
        break;
    case 5:
        cout << "Maio";
        break;
    case 6:
        cout << "Junho";
        break;
    case 7:
        cout << "Julho";
        break;
    case 8:
        cout << "Agosto";
        break;
    case 9:
        cout << "Setembro";
        break;
    case 10:
        cout << "Outubro";
        break;
    case 11:
        cout << "Novembro";
        break;
    case 12:
        cout << "Dezembro";
        break;
    default:
        cout << "Hein?-zembro";
        break;
    }

    cout << " de " << ano << endl;
    return 0;
}
```

## Exercícios
!!! question "Exercício"
    
    Implemente uma função chamada `menu` que imprima o seguinte menu na tela:
    1. Soma
    
    2. Média
    
    3. Menor
    
    4. Maior
    Leia e que retorne o número da opção escolhida.
    
    Implemente a função `main` de forma a ler três números e, então, invocar a função definida acima para decidir o que fazer. O resultado da função deve ser armazenando em uma variável e seu conteúdo testado com `switch`. Cada opção deve invocar a função respectiva, que calculará e retornará o que se pede. A função `main` imprimirá então o resultado.
    
    ```c
    #include <iostream>
    #include <stdio.h>
    #include <math.h>
    using namespace std;

    int menu()
    {
        int opcao;
        cout << "1 Soma" << endl << "2 Media" << endl << "3 Menor" << endl << "4 Maior" << endl;
        cout << "Qual sua opcao? ";

        cin >> opcao;
        return opcao;
    }

    int menor(int x, int y, int z)
    {
        if(x <= y && x <= z)
            return x;

        if(y <= x && y <= z)
            return y;

        return z;
    }

    int maior(int x, int y, int z)
    {
        if(x >= y && x >= z)
            return x;
        else if(y >= x && y<= z)
            return y;
        else
            return z;
    }

    int soma(int x, int y, int z)
    {
        return x+y+z;
    }

    float media(int x, int y, int z)
    {
        float somatorio = soma(x,y,z);
        return somatorio / 3.0;
    }

    int main()
    {
        int a, b, c;
        int opcao;

        cout << "digite tres numero inteiros" <<endl;

        cin >> a >> b >> c;

        opcao = menu();

        switch(opcao)
        {
            case 1:
                cout << "A soma dos tres numeros eh " << soma(a,b,c);
                break;
            case 2:
                cout << "A media dos tres numeros eh " << media(a,b,c);
                break;
            case 3:
                cout << "O menor dentre os tres numeros eh " << menor(a,b,c);
                break;
            case 4:
                cout << "O maior dentre os tres numeros eh " << maior(a,b,c);
                break;
            default:
                cout << "Opcao invalida. Execute o programa novamente e leia direito as opcoes.";
        }

        return 0;
    }
    ```
!!! question "Exercício"
    Escreva um programa com uma função que receba um inteiro entre 1 e 7, inclusive, e escreva o dia correspondente da semana (1 para domingo e 7 para sábado).

!!! question "Exercício"
    
    Escreva um programa com uma função que receba um inteiro de 1 a 12 e retorne a quantidade de dias no mês correspondente (assuma que o ano não é bisexto).
    
    Para este exercício, a solução mais simples envolve não colocar `break` em alguns dos `case`.

## Laboratório
Implemente os exercícios de a.
