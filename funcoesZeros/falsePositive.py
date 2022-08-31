# importar a biblioteca
import matplotlib.pyplot as plt;
import numpy as np;
import math;

def f(x):
    return

def falsePositive(f, lowerLimit= -1e5, higherLimit = 1e5, tolerance = 1e-5, iterationNumber = 1e5):
    i = 0
    while (higherLimit - lowerLimit) > tolerance and i < iterationNumber:
        x = (lowerLimit * abs(f(higherLimit)) + higherLimit * abs(f(lowerLimit)))/(abs(f(lowerLimit)) + abs(f(higherLimit)))
        i = i + 1
        if f(x) * f(lowerLimit) > 0:
            lowerLimit = x
            erro = (higherLimit - x)/2
        else:
            higherLimit = x
            erro = (x - lowerLimit)/2
    return [x, erro, i]

raiz, erro, iteracoes = falsePositive(f, 0.5, 2.5, 0.01, 10)
print('A raiz de f pelo método do falsovale {:.7f} , com erro {:.5f} e com {} iteracoes.'.format(raiz, erro, iteracoes))