# Seleção Simples
Nossos programas até agora foram extremamente simples, contendo apenas algumas pequenas funções além da `main`. Isto acontece em parte por quê nossos programas são apenas sequências diretas de comandos, sem execução condicional. Isto é, até agora não aprendemos a dizer para o computador "Se for assim, então faça assado! Senão, faça cozido!". Esta deficiência será corrigida neste capítulo.

Como exemplo de programação mais interessante, implementemos uma função que calcule as raizes de uma equação de segundo grau. Para fazê-lo, relembremos a fórmula de Bhaskara:

$x = \frac{-b ± √{\Delta}}{2a}$, sendo $\Delta = b^2 -4ac$.

Comecemos então definindo uma função para o cálculo do $\Delta$.

```c
float delta(float a, float b, float c)
{
    return b*b - 4*a*c;
}
```

Para testar o cálculo do $\Delta$ precisamos da função `main`, juntamente com o restante do esqueleto de programa aprendido até agora.

```c
#include <iostream>

using namespace std;

float delta(float a, float b, float c)
{
    return b*b - 4*a*c;
}

int main()
{
    float a, b, c;

    cout << "Equacao do segundo grau: axx + bx + c = 0" << endl;
    cout << "Digite o valor de a: ";
    cin >> a;
    cout << "Digite o valor de b: ";
    cin >> b;
    cout << "Digite o valor de c: ";
    cin >> c;

    cout << "Delta: " << delta(a,b,c) << endl;
    return 0;
}
```

Agora, para cálculo das raízes! Comecemos por alterar o programa para imprimir *o número* de raízes da equação. O cálculo do número de raízes será feito na função `raizes`. A equação tem ou 0 raízes reais (se o $\Delta < 0$), ou duas raízes iguais (se $\Delta = 0$), ou duas raizes distintas (se $\Delta > 0$).

```c
#include <iostream>

using namespace std;

float delta(float a, float b, float c)
{
    return b*b - 4*a*c;
}

int raizes(float a, float b, float c)
{
    float d = delta(a,b,c);
    int qtd;

    se d menor que 0
    {
        qtd = 0;
    }
    senao e se d igual a 0
    {
        qtd = 1;
    }
    senao
    {
        qtd = 2;
    }

    return qtd;
}

int main()
{
    float a, b, c;

    cout << "Equacao do segundo grau: axx + bx + c = 0" << endl;
    cout << "Digite o valor de a: ";
    cin >> a;
    cout << "Digite o valor de b: ";
    cin >> b;
    cout << "Digite o valor de c: ";
    cin >> c;

    cout << "Delta: " << delta(a,b,c) << endl;
    cout << "A equacao tem " << raizes(a,b,c) << " raizes.";
    return 0;
}
```

Acontece que o computador não entende nem o `se` e nem o `menor que`. Mas então como faremos as verificações necessárias para determinar a quantidade raizes? A resposta tem duas partes.

## Operadores Relacionais
As linguagens de programação provêem sempre formas de se comparar dados. Em C(++) os operadores relacionais, usados para comparar, são os seguintes:

| `==` | igual a |
| --- | --- |
| `!=` | diferente de |
| `>` | maior que |
| `<` | menor que |
| `>=` | maior ou igual a |
| `<=` | menor ou igual a |

Observe que o primeiro operador tem *dois* sinais de igual. Isto é para diferenciar este operador do operador de atribuição `=`, visto anteriormente. O segundo operador tem um sinal de exclamação (`!`) que, em linguagem C, significa *negação*. Logo, `!=` significa não igual ou, simplesmente, diferente. Os demais operadores devem ter significados óbvios.

Usando estes operadores, podemos re-escrever a função raizes do nosso programa assim: 

```c
int raizes(float a, float b, float c)
{
    float d = delta(a,b,c);
    int qtd;

    se d < 0
    {
        qtd = 0;
    }
    senao e se d == 0
    {
        qtd = 1;
    }
    senao
    {
        qtd = 2;
    }

    return qtd;
}
```

Melhorou, mas ainda não pode ser executado pelo computador. Vamos então ao *se*.

## `if-else`
Em C, testes simples (tudo o que você realmente precisa) podem ser feitos com a estrutura `if`, que tem uma das seguintes sintaxes:

- `if(` expressão lógica `)` bloco de comandos 1

- `if(` expressão lógica `)` bloco de comandos 1 `else` bloco de comandos 2

Uma *expressão lógica* é uma expressão cuja avaliação resulte em *verdadeiro* ou *falso* como, por exemplo, as expressões que usam os operadores relacionais apenas apresentados.

Um *bloco de comandos* é ou uma instrução ou um conjunto de instruções dentro de `{` `}`.

Quando a expressão lógica é avaliada, se seu resultado for *verdadeiro*, então o bloco de comandos 1 será executado. Se o resultado for *falso*, o bloco de comandos 1 não será executado e o bloco 2, se existir, será executado em seu lugar.

Observe que o segundo bloco pode ser, por sua vez, outro `if`. Por exemplo, nosso programa pode ser reescrito assim:

```c
#include <iostream>

using namespace std;

float delta(float a, float b, float c)
{
    return b*b - 4*a*c;
}

int raizes(float a, float b, float c)
{
    float d = delta(a,b,c);
    int qtd;

    if(d < 0)
    {
        qtd = 0;
    }
    else if(d == 0)
    {
        qtd = 1;
    }
    else
    {
        qtd = 2;
    }

    return qtd;
}

int main()
{
    float a, b, c;

    cout << "Equacao do segundo grau: axx + bx + c = 0" << endl;
    cout << "Digite o valor de a: ";
    cin >> a;
    cout << "Digite o valor de b: ";
    cin >> b;
    cout << "Digite o valor de c: ";
    cin >> c;

    cout << "Delta: " << delta(a,b,c) << endl;
    cout << "A equacao tem " << raizes(a,b,c) << " raizes.";
    return 0;
}
```

O último passo no desenvolvimento do nosso programa é imprimir na tela as raizes da equação, o que faremos em uma nova função: `imprime_raizes`.

```c
#include <iostream>
#include <math.h>

using namespace std;

float delta(float a, float b, float c)
{
    return pow(b,2) - 4*a*c;
}

int raizes(float a, float b, float c)
{
    float d = delta(a,b,c);
    int qtd;

    if(d < 0)
    {
        qtd = 0;
    }
    else if(d == 0)
    {
        qtd = 1;
    }
    else
    {
        qtd = 2;
    }

    return qtd;
}

int imprime_raizes(float a, float b, float c)
{
    float d = delta(a,b,c);
    int qtd;

    if(d < 0)
    {
        cout << "A equacao tem zero raizes reais." << endl;
    }
    else if(d == 0)
    {
        cout << "A equacao tem duas raizes iguais a " << -b/(2*a);
    }
    else
    {
        cout << "A equacao tem duas raizes iguais distintas " << endl <<
        "x' = " << (-b + sqrt(d))/(2*a) << endl <<
        "x'' = " << (-b - sqrt(d))/(2*a) << endl;
    }

    return qtd;
}

int main()
{
    float a, b, c;

    cout << "Equacao do segundo grau: axx + bx + c = 0" << endl;
    cout << "Digite o valor de a: ";
    cin >> a;
    cout << "Digite o valor de b: ";
    cin >> b;
    cout << "Digite o valor de c: ";
    cin >> c;

    cout << "Delta: " << delta(a,b,c) << endl;
    cout << "A equacao tem " << raizes(a,b,c) << " raizes." << endl;
    imprime_raizes(a,b,c);
    return 0;
}
```

Note que a nova função usa a função `sqrt` para calcular a raíz de $\Delta$. Esta função é uma das muitas disponíveis na linguagem C. Para usar esta função é preciso dizer ao computador sua intenção. No nosso programa, isto é feito na linha 2, isto é,
 `#include <math.h>`
 em que dizemos ao computador que queremos usar as funções da biblioteca matemática da linguagem. Aproveitando a inclusão desta biblioteca também alteramos a linha 8 para usar a função  `pow` para o cálculo do $b^2$. Várias outras funções estão disponíveis e podem ser consultadas em <http://www.cplusplus.com/reference/clibrary/cmath/>.

<!-- TODO: A seção seguinte deveria virar um capítulo e a parte if else vistos até agora se juntar ao próximo capítulo -->

## Funções e Procedimentos
A função `imprime_raizes`, definida na seção anterior, tem por objetivo imprimir na tela as raizes da equação de segundo grau, se existirem. Esta função não tem, pela nossa definição, o objetivo de calcular a quantidade de raízes (que era o objetivo da função `raizes`). Em `imprime_raizes` não faz sentido, então, a função ter um *resultado*. Funções sem resultado são denominadas *procedimentos* e, em C, são declaradas como qualquer outra função, apenas com uma particularidade: o tipo do resultado é `void`. Antes de vermos alguns exemplos, precisamos ver a sintaxe de funções em geral, que estivemos usando nas seções e capítulos anteriores mas não havíamos definido formalmente.

tipo_resultado 
identificador_função(tipo_parâmetro 1 identificador_do_parâmetro 1, ...)
bloco_de_comandos

- tipo_resultado -- o tipo do valor que a função está calculando.

- identificador_função -- o nome usado para invocar a função.

- tipo_parâmetro 1 -- tipo do primeiro parâmetro da função.

- identificador_parâmetro 1 -- identificador do primeiro parâmetro da função.

- ... -- tipo e identificador dos demais parâmetros.

- bloco_de_comandos -- instruções que compõem o corpo da função.

Como mencionado, procedimentos são funções sem um resultado e, em C, são declarados como tendo resultado do tipo `void`. Em funções normais, o resultado é dado pela instrução `return`; em procedimentos, que não tem resultado, `return` não é utilizado. Além disso, o resultado de procedimentos não podem ser usados em atribuições.

Além de funções sem resultado, C permite a definição de funções sem parâmetros. Um exemplo deste tipo de função seria uma que lesse algum dado do usuário.
```c
int ler_idade()
{
	int id;
	cout << "Qual sua idade? " <<endl;
	cin >> id;
	return id;
}
```

Finalmente, é importante relembrar que as funções precisam ser definidas *antes* de serem usadas. Sendo assim, você deve incluir a definição das funções antes da definição da função `main` em seu código.  (É possível escrever o código de suas funções após a função `main` ou mesmo em outros arquivos. Fazer isso, contudo, requer conhecer um pouco mais do funcionamento dos compiladores do que o escopo deste livro.). Ainda, relembrando a primeira aula, sobre a função `main`: 
1. A função `main` tem um resultado do tipo inteiro e seu resultado é sempre 0 (`return 0;` ) (Pelo menos nos programas simples que faremos.).

2. Função `main` é como um *highlander*: só pode haver uma! Isto é, cada programa só pode conter a definição de uma função com este nome.

3. Finalmente, todas as funções devem ser declaradas antes da serem usadas, pois quando o computador tenta executá-la, já deve saber de sua existência.

## O Tipo Primitivo `bool`
Como vimos neste capítulo, o `if` avalia uma expressão lógica para decidir-se por executar ou não um bloco de comandos. Expressões lógicas, como também já visto, são aquelas que são avaliadas em verdadeiro ou falso. Na linguagem C(++), quaisquer números inteiros podem também ser avaliados como verdadeiro ou falso, seguindo a seguinte regra:
- 0 corresponde a falso.

- qualquer outro número corresponde a verdadeiro.

Em C++, também é possível utilizar os valores `true` e `false`, que correspondem, respectivamente, a 1 e 0. Estes dois valores compõem o conjuntos dos booleanos, ou melhor, o tipo primitivo `bool`. Isto é, `true` e `false` estão para `bool` assim como -100, 10, 12, ... estão para `int`.

## Exercícios
!!! question "Exercício"
    Muitas pessoas acreditam que um ano é bissexto se for múltiplo de 4. Contudo, a regra é um pouco mais complexa do que esta: 
    - Um ano é bissexto se for múltiplo de 4 mas não de 100, ou
    
    - se for múltiplo de 100, então for múltiplo de 400.
    
    Escreva um programa que leia um ano, chame uma função para calcular se o ano é bissexto e imprima sim ou não de acordo.
    
    ```c
    #include <iostream>

    using namespace std;

    bool bissexto(int ano)
    {
        if(ano % 4 == 0)
        {
            if(ano % 100 == 0)
            {
               if (ano % 400 == 0)
               {
                   return true;
               }
               else
               {
                   return false;
               }
            }
            else
            {
                return true;
            }
        }
        else
        {
            return false;
        }
    }

    int main()
    {
        int ano;

        cout << "Digite o ano que deseja verificar se e bissexto: ";
        cin >> ano;

        cout << "O ano " << ano;

        if(bissexto(ano))
            cout << " e bissexto" << endl;
        else
            cout << " nao e bissexto" << endl;

        return 0;
    }
    ```
!!! question "Exercício"
    Este exercício é dividido em várias partes:
    
    1. Escreva uma função que receba 3 números reais e retorne a média dos três números.
    
    2. Escreva uma função que receba 3 números reais e retorne o menor dentre eles.
    
    3. Escreva uma função que receba 3 números reais e retorne o maior dentre eles.
    
    4. Escreva a função `main` de forma a ler três números reais, calcular a média dos mesmos e, caso a média seja menor que 0, imprima o menor dentre os três, ou, caso a média seja maior ou igual a zero, imprima o maior dentre os três. Sua função `main` deve usar as funções escritas nos itens anteriores para cálculo da média e impressão dos números.

!!! question "Exercício"
    Escreva um programa que contenha
    1. Uma função `celsius_fahrenheit` que receba uma temperatura em graus celsius e converta para fahrenheit.
    
    2. Uma função `fahrenheit_celsius` que receba uma temperatura em fahrenheit e converta para graus celsius.
    
    3. Função `main` que leia uma temperatura do teclado, pergunte ao usuário se a temperatura é em celsius ou fahrenheit, e imprima a temperatura convertida para a outra medida.

!!! question "Exercício"
    Faça uma função denominada *ehPar* que receba um número inteiro como argumento e retorne verdadeiro se este número for par ou falso, caso contrário. A função `main` deve ler o número e imprimir o valor retornado pela função auxiliar.

!!! question "Exercício"
    Elabore um programa com as seguinte descrição:
    - Uma função que retorna verdadeiro se três números reais recebidos como argumentos formam um triângulo ou falso, caso contrário.
    
    - Uma função que recebe três números reais como argumento representado os lados de um triângulo e retorna 0 caso os números formem um triângulo equilátero, 1 caso formem um triângulo isósceles, ou 2 caso sejam os lados de um triângulo escaleno.
    
    - Por fim, a função `main` deve ler os 3  números que representam os lados, e caso formem um triângulo, imprimir se o triângulo formado é equilatero, isósceles ou escaleno.

## Laboratório
Refaça no computador os exercícios propostos acima.
