# Seleção Simples (II)

Uma vez apresentado a estrutura condicional *if-else*, veremos agora como realizar testes mais complexos utilizando operadores lógicos.

## `if-else` e Operadores Lógicos
Até o ponto atual fizemos apenas testes simples dentro da condição dos nossos `if`, por exemplo:
```c
...
/* 
 * esta funcao retorna verdadeiro se a pessoa de sexo 
 * (1=Masculino, 2=Feminino) e idade passados como argumentos
 * for maior que idade ou falso, caso contrario
 */
bool ehMaior(int sexo, int idade)
{
	if(sexo == 1)        // masculino
	{
		if(idade >= 18) 
		{
			return true;
		}
		else 
		{
			return false;
		}
	}
	else if(sexo == 2)  // feminino
	{
		if(idade >= 21)
		{
			return true;
		else
		{
			return false;
		}
	} 
	else             // sexo informado errado
	{
		return false;
	}
}
```

Observe que na função `ehMaior` temos `if` *aninhados*, ou seja, `if` dentro de `if`. 
Isto porque um pessoa deve ser do sexo masculino *E* possuir idade maior ou igual a 18 anos para ser considerada maior de idade. *OU* ainda, ela pode ser do sexo feminino *E* possuir idade igual ou maior a 21 anos.

Quando esta situação ocorre, as condições podem ser combinadas em um único `if` utilizando-se operadores lógicos. Os operadores lógicos que usaremos são o E, o OU e a NÃO (negação).

Na linguagem C, eles são representados pelos símbolos a seguir:

*Operadores lógicos e seus símbolos na linguagem C.*

| Operador Lógico | Símbolo | Símbolo novo (Disponível somente em compiladores C++ ISO98) |
| --- | --- | --- |
| E | && | and |
| OU | \|\| | or |
| NÃO | ! | not |

Os operadores lógicos podem ser resumidos nas tabelas a seguir:

 

*NÃO lógico.*

| **A** | **!A** |
| --- | --- |
| V | F |
| F | V |

*E lógico.*

| **A** | **B** | **A && B** |
| --- | --- | --- |
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | F |

*OU lógico.*

| **A** | **B** | **A \|\| B** |
| --- | --- | --- |
| V | V | V |
| V | F | V |
| F | V | V |
| F | F | F |

Voltando ao nosso exemplo, a função anterior pode ser reescrita da seguinte forma:

```c
...
/* 
 * esta funcao retorna verdadeiro se a pessoa de sexo 
 * (1=Masculino, 2=Feminino) e idade passados como argumentos
 * for maior de idade ou falso, caso contrario
 */
bool ehMaior(int sexo, int idade)
{
	if((sexo == 1 && idade >=18) || (sexo == 2 && not(idade < 21))
	{
		return true;
	}
	else             // sexo errado ou idade errada
	{
		return false;
	}
}
```

Perceba que em apenas um `if` colocamos a condição completa, ou seja, "se sexo igual a 1 E idade maior ou igual a 18 OU sexo igual a 2 e idade NÃO menor do que 21 então é maior de idade".

## Prioridade dos Operadores
Quando mais de um operador lógico aparece em uma expressão, a precedência pode ser expressa da seguinte maneira: primeiro o NÃO, depois o E, por último o OU. Quando houver parênteses, primeiro avalia-se o que estiver dentro dos mesmos.

Em diversas expressões e testes, diversos operadores dos vários tipos podem aparecer. A avaliação dessa expressão deve obedecer à seguinte ordem de prioridade em relação aos operadores:
1. Parênteses, incremento e decremento (`++`, `--`)

2. `not` (!)

3. Multiplicação, divisão e módulo (o que aparecer primeiro);

4. Soma e subtração;

5. Operadores relacionais (<, <=, >, >=)

6. Operadores relacionais (==, !=)

7. `and` (&&)

8. `or` (||)

9. Atribuição (=, +=, -=, *=, /=, %=)

Embora os operadores lógicos façam sentido somente para operandos `bool`, é importante relembrar que, para o computador, verdadeiro e falso são apenas formas de interpretar números na memória. Na linguagem C, qualquer número diferente de 0 é tratado como `true` e 0 é tratado como `false`. Sendo assim, é possível aplicar operadores lógicos também à números. Contudo, sempre que requisitado a representar o valor `true` como número, o computador usará o valor 1, o que faz com que nem todas as computações tenham resultados óbvios. Por exemplo, o código `cout<<(2||0);` imprime, na tela, o valor 1. Isto por quê 2 é tratado como verdadeiro e 0 como falso, e o resultado de verdadeiro OU falso é verdadeiro, que é então convertido para 1.

Da mesma forma, `!!3` é 1, pois `!3` é falso e sua negação é verdadeiro, que é 1.

## Exercícios
!!! question "Exercício"
    Avalie o resultado de cada expressão a seguir (verdadeiro ou falso):
    - `2 < 5 && 15/3 == 5`
    
    - `pow(3,2) - 5 > 0 && 5/2 == 3 - 4`
    
    - `F || 20 == 18/3 != 21/3 / 2`
    
    - `!V || 3*3/3 < 15 - 35%7`
    
    - `!(5 != 10/2) || V && 2 - 5 > 5 - 2 || V`
    
    - `pow(2,4) != 4 + 2 || 2 + 3 * 5/3%5 < 0`
    
    - `!1+1` %1
    
    - `!2+1` %1
    
    - `!0+1` %2

!!! question "Exercício"
    Faça um programa que:
    1. contenha uma função que retorna verdadeiro se um número for divisível por 3 ou 5, mas não simultaneamente pelos dois, e;
    
    2. na função principal sejam lidos dois números inteiros, que deverão ser passados para a função criada, tendo seu resultado impresso.

!!! question "Exercício"
    Faça uma função que receba 3 números reais (`float`) correspondentes aos lados de um triângulo e retorne `true` caso esse triângulo seja retângulo ou `false` caso não o seja. A função principal deve ler os valores dos lados do triângulo, verificar se realmente formam um triângulo e imprimir "sim" se é ou "não", caso não seja triângulo retângulo; se não formar um triângulo, imprimir "não forma".

## Laboratório
!!! example "Laboratório"
    Escreva um programa que implemente uma calculadora com as quatro operações +,-,* e /.
    
    Sua calculadora deve ler um número real X, seguido de um inteiro representando um dos operadores definidos (1 para -, 2 para +, 3 para * e 4 para /), seguido de outro número real Y.
    
    Finalmente, seu programa deve escrever o resultado da operação desejada.

<!-- TODO: Revisado até aqui -->
