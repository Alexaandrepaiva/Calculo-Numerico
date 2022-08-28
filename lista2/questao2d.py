import numpy as np
import matplotlib.pyplot as plt

# função em questão que quero achar a raiz
def f(x):
    return 2*x**3 - 11.7*x**2 + 17.7*x - 5;

def secant(f, lowerLimit = -1e3, higherLimit=1e3, minValue=1e-8, iterationNumber=10000):
    i = 0
    while abs( f(lowerLimit) ) > minValue and i < iterationNumber:
        i = i + 1
        var = lowerLimit
        lowerLimit = lowerLimit - f(lowerLimit)*(lowerLimit-higherLimit)/(f(lowerLimit)-f(higherLimit))
        higherLimit = var
    return [lowerLimit, i]

raiz, iteracoes = secant(f, 1, 2, 0.001, 100)
print('A raiz de f pelo método d secante é {:.7f}  e com {} iteracoes.'.format(raiz, iteracoes))