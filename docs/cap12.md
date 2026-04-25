# Bits, bytes e bases numéricas

Até agora temos trabalhado essencialmente com os tipos numéricos, inteiros e reais, e booleanos. Para que possamos usar outros tipos, é essencial que antes entendamos como os dados são representados na memória do computador.

## Bit & Byte
Como dito anteriormente, a memória do computador pode ser entendida como uma grande planilha eletrônica, podendo cada célula ser endereçada (atribuída, lida, nomeada) individualmente. Na memória do computador não existem números ou caracteres, mas várias "lampâdas" que podem estar ligadas ou desligadas. Nós humanos atribuímos significado a tais estados como sendo 0's e 1's. Cada posição da memória, que pode armazenar 0 ou 1, é denominado um *bit*. Por serem mínimos, normalmente trabalhamos com conjuntos de 8 bits por vez, o que denominamos *bytes*.

### Base Binária
Os bits de um byte podem assumir todas as combinações de ligado e desligado (0 e 1). Dado um contexto, cada combinação corresponde a um certo valor. Por exemplo, se estiver usando um byte para representar números inteiros, então provavelmente a correspondência na Tabela se aplica.

*Exemplos de valores em binário e decimal correspondente.*

| bits | Número |
| --- | --- |
| 00000000 | 0 |
| 00000001 | 1 |
| 00000010 | 2 |
| 00000011 | 3 |
| 00000100 | 4 |
| 00000101 | 5 |
| 00000110 | 6 |
| 00000111 | 7 |
| 00001000 | 8 |
| 00001001 | 9 |
| 00001010 | 10 |
| ... |  |
| 11111101 | 253 |
| 11111110 | 254 |
| 11111111 | 255 |
| 00000000 | 0 |
| ... |  |

Talvez isso seja novidade para você, mas você representa números na base decimal usando 10 dígitos (de 0 a 9). 
Contudo, outras bases existem. Como os bits só possuem dois estados, é natural na computação usar a base binária, que usa 2 dígitos (0 e 1). Os valores à esquerda na tabela podem ser entendidos como números nesta base. (sempre que não for colocada a base, considera-se a base 10, mais natural aos seres de vida baseada em carbono do nosso planeta, A.K.A., você.)

Para conseguir converter números de uma base para a outra, basta entender o que exatamente significa a representação de um número em uma base genérica X. Nesta base, $ABCD_X$ significa $A*X^3 + B*X^2 + C*X^1 + D*X^0$. O número $1234_{10}$, por exemplo, significa $1*X^3 + 2*X^2 + 3*X^1 + 4*X^0 = 1*1000 + 2 * 100 + 3*10 + 4*1$ que é igual a, tá dá, $1234_{10}$.
Para um exemplo mais interessante, o número $10101010_2 = 1*2^7 + 0*2^6 + 1*2^5 + 0*2^4 + 1*2^3 + 0*2^2 + 1*2^1 + 0*2^0 = 128+0+32+8+2 = 170$.

Observe que, pela tabela, o maior número que se pode representar com 8 bits é $11111111_2 = 255_{10}$. Via de regra, com X bits pode se representar $2^X$ na base binária, de 0 a $2^X-1$.

### Base Hexadecimal
Embora se possa usar qualquer base numérica, as que fazem mais sentido no mundo computacional são as binária e hexadecimal.
A base hexadecimal usa 16 dígitos em cada posição representando valores de 0 a 15. Para isto, usa os valores de 0 a 9 iguais aos da base decimal e também as letras de A a F representado os valores de 10 a 15.
Por exemplo, o número 1A2F$_{16}$ equivale a $1*16^3 + 10*16^2 + 2*16^1 + 15*16^0 = 4096 + 2560 + 32 + 15 = 6703$.

## Conversão entre bases numéricas
Enquanto nós trabalhamos com base decimal, o computador armazena informação e realiza operações na base binária. Por isso, a todo momento ocorre a conversão entre um decimal que informamos como entrada em um programa, por exemplo, para a base binária (para efetuar o cálculo), bem como da base binária (resultado do cálculo) para a base decimal exibida na tela.

### Conversão de Binário para Decimal
A conversão de binário (e qualquer outra base) para decimal pode ser feita facilmente usando a notação da base genérica apresentada acima. Isto é, para realizar a conversão basta multiplicar o valor de cada posição pelo seu peso (base elevada à posição). 
Por exemplo, o número $1111011_2$ equivale a $1*2^6 + 1*2^5 + 1*2^4 + 1*2^3 + 0*2^2 + 1*2^1 + 1*2^0 = 64 + 32 + 16 + 8 + 0 + 2 + 1 = 123_{10}$.

### Conversão de Decimal para Binário
A conversão de decimal para binário é feita realizando-se divisões sucessivas pela base de interesse (2, no nosso caso) até que o resultado seja zero. Os restos das divisões, na ordem inversa, correspondem ao número convertido.

Por exemplo, considere a conversão do número 169 para a base binária. O processo de conversão é o seguinte:
$169 / 2 = 84, Resto = 1$
$84 / 2 = 42, Resto = 0$
$42 / 2 = 21, Resto = 0$
$21 / 2 = 10, Resto = 1$
$10 / 2 = 5, Resto = 0$
$5 / 2 = 2, Resto = 1$
$2 / 2 = 1, Resto = 0$
$1 / 2 = 0, Resto = 1$
O número binário equivalente é, portanto, $10101001_2$.

### Conversão entre Binário e Hexadecimal
Sabendo-se que com 4 bits é possível representar até 16 números (de 0 a 15) e que a base hexadecimal tem exatamente 16 dígitos, concluímos que é possível representar cada dígito hexadecimal com 4 dígitos binários. Sendo assim, a conversão binário/hexadecimal pode ser feita facilmente substituindo conjuntos de 4 bits binários por um dígito hexadecimal e vice-versa.

Por exemplo, para convertermos $11101010_2$ convertemos $1110_2$ para E$_{16}$ e $1010_2$ para A$_{16}$, obtendo o número EA$_{16}$. Na direção inversa, para convertermos o número 7B$_{16}$ para binário convertemos 7$_{16}$ para $0111_2$ e B$_{16}$ para $1011_2$, obtendo o número $01111011_2$.

*Exemplos de valores em binário, decimal e hexadecimal correspondentes.*

| Binário | Decimal | Hexadecimal |
| --- | --- | --- |
| 00000000 | 0 | 0 |
| 00000001 | 1 | 1 |
| 00000010 | 2 | 2 |
| 00000011 | 3 | 3 |
| 00000100 | 4 | 4 |
| 00000101 | 5 | 5 |
| 00000110 | 6 | 6 |
| 00000111 | 7 | 7 |
| 00001000 | 8 | 8 |
| 00001001 | 9 | 9 |
| 00001010 | 10 | A |
| 00001011 | 11 | B |
| 00001100 | 12 | C |
| 00001101 | 13 | D |
| 00001110 | 14 | E |
| 00001111 | 15 | F |
| 00010000 | 16 | 10 |
| ... |  |  |
| 11111101 | 253 | FD |
| 11111110 | 254 | FE |
| 11111111 | 255 | FF |
| 00000000 | 0 | 0 |
| ... |  |  |

## Tipos Numéricos Inteiros
Na linguagem C, os principais tipos, a quantidade de bits utilizada para sua representação e o intervalo de valores aceitos são resumidos na tabela a seguir:  (A quantidade de bits pode variar de acordo com o compilador e a arquitetura do sistema)

*Intervalo de representação dos tipos numéricos inteiros.*

| Tipo | Quantidade de Bits | Intervalo |
| --- | --- | --- |
| char | 8 | -128 a 127 |
| unsigned char | 8 | 0 a 255 |
| int | 16 | -32.768 a 32.767 |
| unsigned int | 16 | 0 a 65.535 |
| long | 32 | -2.147.483.648 a 2.147.483.647 |
| unsignet long | 32 | 0 a 4.294.967.295 |

Observe que o tipo caractere também é armazenado internamente como um número inteiro de 8 bits.
Com 8 bits podemos representar $2^8$ números. Se considerarmos números sem sinal (*unsigned*) teremos de 0 a 255; se considerarmos números com sinal, teremos metade para positivos e metade para negativos, ou seja, de -128 a 127. O mesmo raciocínio se aplica para os outros tipos de dados da tabela.

A partir desta tabela podemos observar a importância da escolha adequada do tipo correto de acordo com sua aplicação. Se utilizarmos um inteiro para somarmos 20.000 e 50.000, por exemplo, o resultado será inesperado, uma vez que o maior valor que um inteiro aceita é 32.767. Quando isto ocorre, dizemos que houve um *overflow*.

### Números Binários Negativos
Os exemplos que vimos até agora de conversão não contemplam números negativos. Na base decimal, o sinal de menos (-) antes do valor do número tem a finalidade de representar números negativos.

Como a memória do computador armazena apenas 0's e 1's, uma possível estratégia é "desperdiçar" um dos bits do número para o sinal. Adota-se, por padrão, o zero para representar um número positivo e o um para negativo. O bit do sinal é armazenado na posição mais à esquerda.

Para representar o valor de um número negativo há duas principais abordagens: **sinal-magnitude** e **complemento de 2**.

Na representação **sinal-magnitude**, o número negativo tem seu valor absoluto (magnitude) representado da mesma forma que um número positivo e o bit mais significativo, que representa o sinal, será igual a um. A tabela a seguir mostra alguns exemplos de números na base decimal e na representação sinal-magnitude.

*Exemplos de valores na representação sinal-magnitude.*

| Decimal | Binário Sinal-Magnitude |
| --- | --- |
| +20 | **0**0010100 |
| -20 | **1**0010100 |
| +115 | **0**1110011 |
| -115 | **1**1110011 |

Com 8 bits, temos, então números de $11111111_2$ a $01111111_2$ (-127 a +127). Um problema que aparece com esta representação é o zero. Qual a representação correta, $00000000$ ou $10000000$? E por que precisaríamos de duas representações?

A representação **complemento de 2** utiliza uma maneira um pouco diferente de representar números negativos. Para expressá-los devemos inverter cada bit do número positivo e somar 1 ao resultado. Por exemplo, o número -15 é representado em complemento de 2 com 5 bits como 10001, ou seja, calcula-se o valor de +15 = $01111_2$, e, em seguida invertemos e somamos 1: $10000_2 + 1_2 = 10001_2$. Se a representação usar 8 bits, então $15_{10} = 00001111_{2}$ e $-15_{10} = 11110001_{2}$.

## Aritmética Inteira Binária
Aritmética binária é tão simples como $1 + 1 = 10$. Sério, é assim que se faz: $0 + 0 = 0, 0+1 = 1+0 = 1, 1 + 1 = 10_2$. Logo, em sistemas computacionais as somas e subtrações geralmente são realizadas aos pares, da mesma forma que na base binária.

### Números positivos
A **adição** de números positivos é muito simples. Para fazê-la, basta somar os valores na mesma posição, do menos significativo para o mais significativo. O "vai-um" funciona da mesma forma como fazemos na base decimal. Por exemplo, para somarmos 5 e 9, fazemos:
```
  1
0101 +
1001
----
1110
```
Como a quantidade de bits para determinado tipo de dados é limitado, durante uma soma pode ocorrer de o resultado ultrapassar o maior valor permitido para aquela quantidade de bits, quando isto ocorre, temos um *overflow* (derramamento). Considere a soma de 7 e 9, ambos com 4 bits.
```
1 111
  0111 +
  1001
  ----
1 0000  <-- overflow!
```

Houve um "vai-um" além do bit mais significativo, caracterizando um *overflow*. Neste caso, o resultado da operação está errado.

### Números em Complemento de 2
Como vimos anteriormente, o computador usa duas principais representações para números negativos. A representação complemento de 2 é a mais utilizada porque permite que a soma de números negativos seja feita da mesma maneira que a soma de números positivos. Por exemplo considere as soma de -2 + 5 e -1+(-1), em complemento de 2:
```
    1 1
(-2)  1110 +
(+5)  0101
      ----
    1 0011  <-- Não é overflow! Esse "vai-um" deve ser desprezado!
    
    1 111
(-1)  1111 +
(-1)  1111
      ----
    1 1110  <-- Não é overflow! Esse "vai-um" deve ser desprezado!
```
Observe que nestes exemplos tivemos um "vai-um" além do bit mais significativo. Em soma de números em complemento de 2 isto não é suficiente para caracterizar um *overflow*. Um *overflow* apenas ocorrerá quando, ao somarmos dois números de mesmo sinal, obtivermos um número de sinal diferente. Desta maneira, no exemplo apresentado, este "vai-um" a mais deve simplesmente ser ignorado.

Já os exemplos a seguir mostram operações problemáticas.
```
      111
(+7)  0111 +
(+7)  0111
      ----
      1110  <-- O resultado começa com 1, logo é negativo. Absurdo!

    1 
(-3)  1101 +
(-6)  1010
      ----
    1 0111  <-- O resultado começa com 0, logo é positivo. Absurdo!
```

### E a subtração?
Na verdade, a maioria dos computadores não sabe fazer subtração. O que eles fazem é utilizar um truque para transformar uma subtração em uma soma.

Por exemplo, a operação $7 - 5$ pode ser reescrita como $7 + (-5)$, ou seja, para realizar a subtração basta inverter o segundo número (em complemento de 2) e somá-lo ao primeiro da maneira usual.

## Tipos Numéricos Reais
Para representarmos números reais no computador, definimos que uma quantidade de bits do número será usada para representar a mantissa e o restante o expoente do número. Por exemplo, se dispusermos de 8 bits, podemos definir que os quatro primeiros bits serão a mantissa e os quatro últimos serão o expoente, em notação científica. Assim, $10101010_2 = 1,0*10^{11}$ e $10111010_2 = 1,1*10^{11}$.

Antes que você saia dizendo por aí que o ideal é usar tais números pois podemos representar números tão grandes como $11111111_2 = 15*10^{15}$, que é muito mais que os $2^{16}-1$ da notação binária  convencional, pense em como representaria o número 161$_{10}$, já que a maior mantissa representável é 1,5. Além disso, como representar 1,1111, já que só dispomos de 4 dígitos na mantissa?

Além disso, se representações de números reais pecam em sua precisão, também pecam na velocidade de processamento. A aritmética de números binários é muito mais simples que a de números reais (ou de ponto flutuante, como costumamos dizer na computação). Para manipular números reais, computadores normalmente precisam de componentes dedicados a este fim e que tem alto tempo de execução.

Para saber mais sobre representações de números em pontos flutuantes visite a URL <http://en.wikipedia.org/wiki/Floating_point>

## Exercícios e laboratório
### 
Quantos números se pode representar, na base binária, com 1, 8, 16, 32 e 64 bits?

### 
Escreva os seguintes números nas bases binária e hexadecimal:
1. 16

2. 45

3. 129

4. 23

5. 1290

### 
Converta os números a seguir para a base decimal:
1. $16_{16}$

2. D5$_{16}$

3. $1100101101_2$

4. 2C04$_{16}$

5. $11101_2$

### 
Escreva os números a seguir nas representações sinal-magnitude e complemento de 2 com 8 bits:
1. -19

2. +47

3. -29

4. -37

5. -105

### 
Realize as seguintes operações aritméticas em complemento de 2 com números de 8 bits:
1. 16 - 9

2. -45 - 7

3. -12 + 12

### 
!!! example "Laboratório"
    Faça um programa para descobrir quantos bits tem uma variável do tipo `int`? E um `unsigned int`?

!!! example "Laboratório"
    Escreva um programa que leia um número de 2 dígitos na base decimal e imprima o mesmo número na base binária.

!!! example "Laboratório"
    Escreva um programa que leia um número binário de até 10 bits e imprima o mesmo número na base decimal.
