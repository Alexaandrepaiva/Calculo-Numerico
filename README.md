# Cálculo Numérico

## Sobre
Esse repositório foi feito pelo aluno Alexandre de Paiva Almeida para ser usado na disciplina de Cálculo Numérico no quarto semestre do Ciclo Básico do Instituto Militar de Engenharia.

## Instalação
Caso você também queira usar esse repositório e queira cloná-lo no seu colab, basta seguir os seguintes passos:

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
## Sistemas Lineares

### Métodos diretos
Nesta classe de métodos a solução do sistema é obtida após um número finito de passos e são em geral baseados em métodos de eliminação onde se transforma o sistema a resolver em outro sistema de resolução mais fácil que o sistema original. Estes métodos são normalmente empregados na solução de sistemas de pequeno a médio porte em que a matriz de coeficientes é densa.

Teoricamente, a solução de uma sistema linear não singular es´ta perfeitamente assegurada. Entretanto, o método de Gauss pode gerar soluções falsas para sistemas lineares mal condicionados (sistemas cuja solução é muito sensível a pequenas mudanças nos coeficientes).

#### Eliminação de Gauss
A Eliminação de gauss pode ser realizada através da função `gaussElimination` e seu objetivo  é transformar um sistema linear $Ax = b$ em um outro sistema, que possui a mesma solução do primeiro, $Ux = c$ tal que a matriz $U$ seja triangular superior, `gaussElimination`. Esta transformação é feita através de combinações lineares das linhas do sistema. Caso julgue necessário, pode-se realizar esse método com pivoteamento com a função `gaussEliminationPivot` O sistema linear triangular superior é resolvido por meio de substituições retroativas, através da função `substRetroativa`.

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
## Interpolação Polinomial