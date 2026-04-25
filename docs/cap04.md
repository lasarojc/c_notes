# Variáveis (II)
## Escopo de Variáveis
No capítulo anterior estudamos como declarar e utilizar variáveis em nossos programas. Fizemos, por exemplo, um programa como o seguinte, que pede ao usuário que entre com as medidas da base e altura de um retângulo e então imprime na tela do computador a área deste retângulo.

```c
float area_retangulo(float altura, float base)
{
    //Calcula e retorna a area do retangulo.
    return altura * base;
}

int main()
{
    float area,
          b,
          a;
    cout << "Qual a altura do retangulo?" << endl;
    cin >> a;
    
    cout << "Qual a base do retangulo?" << endl;
    cin >> b;
            
    area = area_retangulo(b, a);
    cout << "A area do retangulo de base " << b << " e altura " 
          << a << " eh " << area << endl;
    
    return 0;
}
```

O que aconteceria se em vez de chamarmos as variáveis na função `main`  de `a`  e `b` as tivéssemos chamado de `base` e `altura`? Veja que estes são exatamente os nomes dos parâmetros da função `area_retangulo`. Melhor ainda, e se a função tivesse alterado os valores dos parâmetros? 

Para descobrir as respostas a estas perguntas, faça o seguinte experimento:
- digite o programa tal qual acima em seu computador e *execute-o*.

- modifique somente a função `main` do seu programa para que fique assim
```c
int main()
{
    float area,
          base,
          altura;
    cout << "Qual a altura do retangulo?" << endl;
    cin >> altura;
    
    cout << "Qual a base do retangulo?" << endl;
    cin >> base;
            
    area = area_retangulo(base, altura);
    cout << "A area do retangulo de base " << base << " e altura " 
         << altura << " eh " << area << endl;
    
    return 0;
}
```
e execute-o.

- Note quais as diferenças na execução.

- Finalmente, altere a função `area_retangulo` para que fique assim
```c
float area_retangulo(float altura, float base)
{
    //Calcula e retorna a area do retangulo.
    altura *= base;
    return altura;
}
```
e execute novamente o programa.

- Note se houve alguma alteração do valor da variável `altura`.

Como se pôde notar, estas mudanças não afetaram a execução do programa. Isto acontece por quê as variáveis tem escopos bem definidos em C. A variável `altura` da função `main` não é a mesma variável/parâmetro `altura` da função `area_retangulo`; cada uma só existe dentro do corpo da função em que foi declarada. Quando a função `area_retangulo` é invocada passando-se como parâmetro a variável `altura` da função `main`, o valor desta variável é *copiado* para o parâmetro `altura` da função invocada. Sendo assim, quaisquer alterações ao valor do parâmetro dentro da função afetam apenas a cópia, não o valor da variável de onde foi copiado.

A variáveis definidas até agora possuem o que chamamos *escopo local*. Isto é, elas são visiveis somente localmente à função em que foram definidas. Outro tipo de escopo presente possível em C é o *escopo global*. Uma variável tem escopo global se for definida fora de qualquer função. Uma variáel com escopo global poderá ser acessada de (quase) qualquer parte do seu código. Para um exemplo de variável de escopo global, veja o código a seguir. 

```c
float PI = 3.1416;

float resposta = 0;

float area_retangulo(float altura, float base)
{
    //Calcula e retorna a area do retangulo.
    resposta = base * altura;
    return resposta;
}

float area_circulo(float raio)
{
    //Calcula e retorna a area do circulo.
    resposta = PI * raio * raio; 
    return resposta;
}

int main()
{
    float area,
          base,
          altura,
          raio;
    
    cout << "Qual a altura do retangulo?" << endl;
    cin >> altura;
    
    cout << "Qual a base do retangulo?" << endl;
    cin >> base;
            
    area = area_retangulo(base, altura);
    cout << "A area do retangulo de base " << base << " e altura " 
          << altura << " eh " << area << endl;
    
    cout << "Resposta da chamada de funcao " << resposta << endl; 

    cout << "Qual o raio do circulo?" << endl;
    cin >> raio;

    area = area_circlo(raio);
    cout << "A area do circulo de raio " << raio 
    << " e PI arredondado para " << PI <<" eh " << area << endl;
     
    cout << "Resposta da chamada de funcao " << resposta << endl; 
    return 0;
}
```

Observe a variável `PI`. Esta variável foi declarada fora de qualquer função e, sendo assim, é visível em qualquer delas, como demonstrado pelo seu uso na função `main` e `area_circulo`.

Observe também que a mesma variável `area` foi utilizada mais de uma vez. Isto é comum em programação pois, com a quantidade limitada de recursos, pode não fazer sentido criar uma variável para cada novo uso. Observe que a variável `resposta` foi alterada dentro das duas funções de cálculo de área e que estas mudanças foram visíveis à função `main`.

Verifique de forma experimental (copiando e executando) que o programa acima funciona como esperado.

## Faixas de Valores
Você já aprendeu que variáveis são espaços (células) da memória do computador para o qual damos nomes. Estes espaços, por serem limitados, podem armazenar uma quantidade limitada de valores. Pense, por exemplo, em quais os números, positivos e negativos, se pode representar com três dígitos: $-99, -98, ..., 0, 1, 2, ..., 998,999$.

Tentemos descobrir qual a faixa de valores que "cabem" em uma variável `int`. Escreva um programa que declare uma variável do tipo `int`, inicie esta variável com um número (digamos, 10000), e imprima este número na tela do computador. Veja que o número é impresso na tela como deveria: `10000`. 

Agora altere seu programa para que imprima 20000 e execute-o. Refaça este passo (adicionando 10000 a cada passo) até que a impressão fuja do que você esperava. Neste ponto, trabalhe com incrementos menores até determinar qual o maior número que é impresso como esperado. Fepita o processo para identificar qual o menor número que cabe em um `int`. Quais são estes valores?

Finalmente, tente identificar a faixa de valores que cabem em um `float`. Dica: os incrementos iniciais deveriam ser na faixa de milhões e não dezenas de milhares.

## Exercícios
<!-- TODO: Colocar -->

## Laboratório
<!-- TODO: Colocar -->
