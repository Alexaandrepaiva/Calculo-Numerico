# Cálculo Numérico

## Sobre
Esse repositório foi feito pelo aluno Alexandre de Paiva Almeida para ser usado na disciplina de Cálculo Numérico no quarto semestre do Ciclo Básico do Instituto Militar de Engenharia.

Autores: Alexandre Paiva e Camila Cardi

## Instalação
Se lhe convier usar esse repositório, é possível cloná-lo no Colab, basta seguir os seguintes passos:

1. Para clonar esse repositório no seu arquivo colab, copie e cole o código abaixo:

```
%rm -r CalculoNumerico/
!git clone https://github.com/Alexaandrepaiva/CalculoNumerico
```

2. Para importar arquivos, importe um ou mais arquivo da seguinte maneira:

```
from CalculoNumerico import zeros
from CalculoNumerico import linearSystem as ls
from CalculoNumerico import interpolacao as ip
from CalculoNumerico import autovalores as av
```

## Zeros de funções
As funções de zeros de funções se encontram no arquivo <strong>zeros.py</strong>.

#### Método gráfico
O método gráfico consiste em fazer um esboço do gráfico da $f(x)$, para ter uma ideia de em que intervalo se encontram as raízes de $f(x)$. Esse método pode ser realizado através da função `graph`.

#### Bisseção
O método da bisseção pode ser realizado através da função `bissection` e tem como objetivo reduzir a amplitude do intervalo que contém a raiz até atingir a precisão desejada.

#### Falsa posição
O método da falsa posição pode ser realizado através da função `falsePosition` e tem o mesmo objetivo do método da bisseção, no entanto, reduz o intervalo por meio da média ponderada.

#### Ponto fixo
O método do ponto fixo pode ser realizado através da função `fixedPoint` e consiste em transformar a equação $f(x)=0$ em uma equação equivalente $x=\phi (x)$. Uma função $\phi$ que satisfaz a condição acima é chamada de Função de Iteração para a equação $f(x)=0$.


<strong>TEOREMA DO MÉTODO DO PONTO FIXO</strong>

Seja $\epsilon$ uma raiz da equação $f(x)=0$, $I$ um intervalo centrado nessa raiz, $\phi$ uma função de iteração e $x_0$ o valor do chute inicial. O processe iterativo converge se:

- $\phi$ e $\phi '$ são contínuas em $I$;
- $|\phi '(x)|<1$  $\forall x \in I$;
- $x_0 \in I$


#### Newton-Raphson
O método de Newton-Raphson pode ser realizado através da função `newtonRaphson` e sua ideia é de tomar um valor de $x$ como primeira estimativa da raiz, calcular o valor da função para esse valor (que será diferente de zero), traçar a tangente à curva buscando o ponto em que essa tangente corta o eixo $x$. Esse novo valor de $x$ é uma melhor aproximação.

## Sistemas Lineares
As funções de sistemas lineares se encontram no arquivo <strong>linearSystem.py</strong>.

### Métodos diretos
Nesta classe de métodos a solução do sistema é obtida após um número finito de passos e são em geral baseados em métodos de eliminação onde se transforma o sistema a resolver em outro sistema de resolução mais fácil que o sistema original. Estes métodos são normalmente empregados na solução de sistemas de pequeno a médio porte em que a matriz de coeficientes é densa.

Teoricamente, a solução de uma sistema linear não singular es´ta perfeitamente assegurada. Entretanto, o método de Gauss pode gerar soluções falsas para sistemas lineares mal condicionados (sistemas cuja solução é muito sensível a pequenas mudanças nos coeficientes).

#### Eliminação de Gauss
A Eliminação de gauss pode ser realizada através da função `gaussElimination` e seu objetivo  é transformar um sistema linear $Ax = b$ em um outro sistema, que possui a mesma solução do primeiro, $Ux = c$ tal que a matriz $U$ seja triangular superior, `gaussElimination`. Esta transformação é feita através de combinações lineares das linhas do sistema. Caso julgue necessário, pode-se realizar esse método com pivoteamento com a função `gaussEliminationPivot`. O sistema linear triangular superior é resolvido por meio de substituições retroativas, através da função `substRetroativa`.

#### Decomposição $LU$
A decomposição $LU$ pode ser realizada através da função `decompositionLU` e, nela, decompõe-se a matriz $A$ em um produto de matrizes $L$ (triangular inferior) e $U$ (triangular superior). Pode-se ainda resolver o sistema linear por esse método através da função `solutionLU`, que resolverá por substituições retroativas, pela função `substRetroativa`, e por substituição sucessivas, pela função `substSucessiva`.

#### Decomposição de Choleski
A decomposição de Choleski pode ser realizada através da função `choleski` e é utilizada para decompor uma matriz simétrica definida positiva em $LL^T$ (produto de matrizes superior e inferior, em que uma é a transposta da outra). Pode-se resolver o sistema linear por esse método através da função `solutionCholeski`.

#### Outros tipos de sistemas
- Matriz tridiagonal

    Pode-se resolver o sistema linear em que $A$ é uma matriz tridiagonal pela função `tridiagonal`.

- Matriz pentadiagonal

    Pode-se resolver o sistema linear em que $A$ é uma matriz pentadiagonal pela função `pentadiagonal`.

### Métodos iterativos
Nos métodos iterativos, para a resolução do sistema linear $Ax = b$, dado na forma matricial, tranformamos esse sitema linear na forma equivalente $x = Cx + g$.
#### Método Gauss-Jacobi
O método de Gauss-Jacobi pode ser realizado através da função `solutionJacobi`.
#### Método Gauss-Seidel
O método de Gauss-Seidel pode ser realizado através da função `solutionGaussSeidel`.

## Autovalores e Autovetores
As funções de autovalores e autovetores se encontram no arquivo <strong>autovalores.py</strong>.
#### Método de Leverrier
O método de Leverrier fornece o polinômio característico de uma matriz $A$, $nxn$ e pode ser realizado através da função `leverrier`.
#### Método de Leverrier-Faddeev
O método de Leverrier-Faddeev consiste em uma simplificação do método de Leverrier para o cálculo dos autovalores da matriz $A$ e também permite calcular seus autovetores. Os autovetores de uma matriz podem ser encontrados através da função `autovetor`.

O método de Leverrier-Faddev para obter os autovalores possui um pouco de instablidade e ainda precisamos encontrar as raízes de um polinômio caractéristico.
#### Método $LR$
O método $LR$ pode ser realizado através da função `methodLR` e tem o objetivo de encontrar os coeficientes do polinômio característico por meio de um processo iterativo iniciando com a decomposição $LU$ da matriz $A$, nesse arquivo executada pela função `decompositionLR`.
#### Método $QR$
O método $QR$ pode ser realizado através da função `methodQR` e tem o objetivo de encontrar os coeficientes do polinômio característico por meio da decomposição da matriz $A$ em $QR$, em que $Q$ é uma matriz ortogonal $(Q^TQ=I)$ e $R$ é uma matriz triângular superior. Os autovalores podem ser encontrados por esse método com a função `autovaloresQR`.

## Interpolação Polinomial
Existe e é unico o polinômio $p_n(x)$ de grau $<=n$ que se aproxima a $f(x)$ em $n+1$ pontos distintos tal que: $f(x_k)=p_n(x_k), k=0,1,2,...,n$. 

#### Formas de Interpolação
Sejam $x_0, x_1, ..., x_n$, $n+1$ pontos distintos e $y_i=f(x_i), i=0, 1, ..., n$. Podemos representar $p_n(x)$ na forma $p_n(x)=y_0L_0(X) + y_1L_1(X) + ... + y_nL_n(X)$, em que $L_n(x)$ são os polinômios de grau $<=n$. Para cada $i$, deve-se satisfazer a equação de que $p_n(x_i)=y_i$. Obtem-se:
$p_n(x)= sum of ...$


As funções de interpolação polinomial se encontram no arquivo <strong>interpolation.py</strong>.

## Ajustes de curvas
As funções de interpolação polinomial se encontram no arquivo <strong>ajuste.py</strong>.

## Integral
As funções de integral se encontram no arquivo <strong>integral.py</strong>.

## Equação Diferencial Ordinária
As funções de E.D.O. se encontram no arquivo <strong>edo.py</strong> e os arquivos da pasta <strong>EDO</strong> apresentam alguns exemplos.

#### Método de Euler
A resolução de E.D.O. pelo método de Euler pode ser realizada através da função `ODE_Euler`.
Seja: 
$$\dfrac{ds(t)}{dt}=F(t,s(t))$$ 
Uma aproximação linear de $s(t)$ em torno de $t_j$ e $t_{j+1}$ é: 
$$s(t_{j+1}=s(t_j)+(t_{j+1}-t_j)\dfrac{ds(t_j)}{dt}$$
ou ainda:
$$s(t_{j+1}=s(t_j)+h\cdot F(t_j,s(t_j))$$
Essa última equação é conhecida como a forma explícita de Euler e o código da função de Euler está no arquivo <strong>euler.py</strong>

#### Método de Heun
A resolução de E.D.O. pelo método de Heun pode ser realizada através da função `ODE_Heun`.
Seja: 
$$\dfrac{ds(t)}{dt}=F(t,s(t))$$
$$s(t)\vert_{t_j}^{t_{j+1}} = s(t_{j+1}) - s(t_{j}) = \int_{t_j}^{t_{j+1}}F(t,s(t)dt $$
$$ s(t_{j+1})  = s(t_{j}) + \int_{t_j}^{t_{j+1}}F(t,s(t)dt $$
com $s(t_0) = s_0$
Formula Trapezoidal
$$ s(t_{j+1}) = s(t_j) + \dfrac{h}{2}(F(t_j,s(t_{j})+ F(t_{j+1},s(t_{j+1})) $$
$$s(t_{j+1}) \approx s(t_j) + h(F(t_j,s(t_{j})$$
$$ s(t_{j+1}) = s(t_j) + \dfrac{h}{2}(F(t_j,s(t_{j})+ F(t_{j+1},s(t_{j+1}) + h(F(t_j,s(t_{j})) $$

#### Método de Runge-Kutta
O método Runge-Kutta (RK4) de quarta ordem com um erro de truncamento de $O (h^4)$ é um dos métodos mais amplamente usados para resolver equações diferenciais. A resolução de E.D.O. pelo método de Runge-Kutta de quarta ordem pode ser realizada através da função `ODE_RK4`.
$$ s(t_{j+1}) = s(t_j) + \dfrac{h}{6}(f_1 + 2f_2 + 2f_3 + f_4) $$
Em que:
$$ f_1 = F(t_j,s(t_{j}))$$
$$f_2 = F(t_{j} + \dfrac{h}{2},s(t_j) + f_1 \dfrac{h}{2} )$$
$$f_3 = F(t_{j} + \dfrac{h}{2},s(t_j) + f_2 \dfrac{h}{2} )$$
$$f_4 = F(t_{j} + h,s(t_j) + f_3h )$$

#### Método de Adams
São métodos lineares de passo múltiplo, onde um métode de passo $k$ pode ser dado por: 
$$ \alpha_{k}s_{i+k} + \alpha_{k-1}s_{i+k-1} + \cdots + \alpha_{-1}s_{i-1} + \alpha_{0}s_{i} = h(\beta_{k}F_{i+k} + \cdots +\beta_{0}F_{i})$$
onde $\alpha$ e $\beta$ é para cada método particular, sujeitas a s condições $\alpha_{k}=1$ e $\vert \alpha_0 \vert + \vert \beta_0 \vert \ne 0$ , sendo $F_i =F(t_i, s(t_i))$
Saõ definidos uma família de métodos de Adams, onde podem serem classicados de Explícitos, chamados de Adams-Bashforth, e de métodos Implícitos, chamados com Adams-Moulton. Quando $\beta_k= 0 $, o método é dito explícito e para $\beta_k \ne 0 $ é dito implícito.
Os métodos são obtidos por integração do PVI e para uma EDO de 1ª ordem é dada por:
$$ s_{i+1}= s_i + \int_{t_i}^{t_{i+1}}F(t,s(t)dt$$
A técnica para obter os coefientes é de aproximar $F(t,s(t) $ com uma aproximação de um polinômio inteporlador, usando  o método de lagrange o polinômio será $l(t)$.
$$ s_{i+1}= s_i + \int_{t_i}^{t_{i+1}}l(t)dt$$


#### Método de Shooting
O método Shooting (tiro) foi desenvolvido com o objetivo de transformar um PVC em um PVI equivalente para que possamos resolvê-lo usando os métodos anteriores.
$$\begin{cases}\dfrac{d^2s(t)}{dt^2}= F(t,s(t),s'(t)) \\ s(t_0) = s_0 \;\;\;\;\;\;\;\; s'(t_0)=v_0
\end{cases}$$

Uma maneira de proceder na resolução  é adivinhar $s'(t_0)$ e, em seguida, realizar a solução do problema de valor inicial resultante até $t_f$, e verificar se a solução calculada seja
$s_f$, ou seja, $s(t_f)=s_f$. 

Se isso não acontecer (o que é bastante provável), podemos voltar e mudar
nossa estimativa para $s'(t_0)$.

Repetir este procedimento até atingirmos o alvo $s_f$.
 
Pode ser um bom método, se pudermos aprender algo com as várias tentativas. Existem maneiras sistemáticas de utilizar esta informação, e o método resultante é conhecido pelo apelido de tiro.

Observamos que o valor final $s(t_f)=s_f$ da solução do nosso problema de valor inicial depende
na suposição feita para $s'(t_0)$. Todo o resto permanece corrigido neste problema. Assim, a equação diferencial $\dfrac{d^2s(t)}{dt^2}= F(t,s(t),s'(t))$ e o primeiro valor inicial, $s(t_0) = s_0$ , não mudam.

Se atribuirmos um valor real $z$ à condição inicial ausente,
$s'(t_0) =z $ então, o problema do valor inicial pode ser resolvido numericamente. O valor de $s$ em $t_f$ agora é um função de $z$, que denotamos por $\phi(z)$. Em outras palavras, para cada escolha de $z$, obtemos um novo valor para $s(t_f)$, e $\phi$ é o nome da função com este comportamento. 

Nós sabemos muito pouco sobre $\phi(z)$, mas podemos computá-lo ou avaliá-lo. 

É, no entanto, uma função cara para
avaliar porque cada valor de $\phi(z)$ é obtido somente após resolver um problema de valor inicial.

Deve ser enfatizado que o método de tiro combina qualquer algoritmo para o problema de valor inicial com qualquer algoritmo para encontrar o zero de uma função. A escolha de esses dois algoritmos devem refletir a natureza do problema a ser resolvido.

## Equação Diferencial Dependente
As funções de E.D.P. se encontram no arquivo <strong>edp.py</strong>.
