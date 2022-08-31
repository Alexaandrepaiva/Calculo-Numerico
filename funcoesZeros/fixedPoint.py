# importar a biblioteca
import matplotlib.pyplot as plt;
import numpy as np;
import math;

# função do método do ponto fixo

def f(x):
    return 

def phi(x):
    return (-1) * math.sqrt((math.e) ** x)

def fixedPoint(f, phi, initialValue = 0, tolerance = 1e-5, iterationNumber = 1e5):
    i = 0
    x = phi(initialValue)
    while abs(initialValue - x) > tolerance and i < iterationNumber:
        i += 1
        initialValue = x
        x = phi(x)
    return [x, i]

raiz, iteracoes = fixedPoint(f, phi, -1, 0.001, 10)
print('A raiz de f pelo método da iteração de ponto fixo é {:.7f} e com {} iteracoes.'.format(raiz, iteracoes))
