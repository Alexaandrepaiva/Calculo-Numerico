# importar a biblioteca
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return

def dfdx(x):
    return

def newtonRaphson(f, dfdx, initialValue = 0, tolerance = 1e-5, iterationNumber = 1e5):
    i = 0
    x_k = [initialValue]
    y_k = [f(initialValue)]
    while abs( f(x_k[-1]) ) > tolerance and i < iterationNumber:
        i = i + 1
        old_x = x_k[-1]
        next_x = x_k[-1] - f(x_k[-1])/dfdx(x_k[-1])
        erro_absoluto = abs(old_x - next_x)
        erro_relativo = abs(old_x - next_x)/old_x
        x_k.append(next_x)
        y_k.append(f(next_x))
    return [x_k[-1], erro_absoluto, erro_relativo, i]

raiz, erro_absoluto, erro_relativo, iteracoes = newtonRaphson(f, dfdx, 2, 0.001, 10)
print('A raiz de f pelo método de Newton-Raphson é {:.7f}, com erro absoluto {}, erro relativo {} e com {} iteracoes.'.format(raiz, erro_absoluto, erro_relativo, iteracoes))
