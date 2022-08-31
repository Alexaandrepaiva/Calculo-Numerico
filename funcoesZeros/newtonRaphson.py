# importar a biblioteca
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return

def dfdx(x):
    return

def newtonRaphson(f, dfdx, initialValue, tolerance, iterationNumber):
    i = 0
    x_k = [initialValue]
    y_k = [f(initialValue)]
    while abs( f(x_k[-1]) ) > tolerance and i < iterationNumber:
        i = i + 1
        next_x = x_k[-1] - f(x_k[-1])/dfdx(x_k[-1])
        x_k.append(next_x)
        y_k.append(f(next_x))
    return [x_k[-1],i]

raiz, iteracoes = newtonRaphson(f, dfdx, 2, 0.001, 10)
print('A raiz de f pelo método do ponto fixo é {:.7f}  e com {} iteracoes.'.format(raiz, iteracoes))