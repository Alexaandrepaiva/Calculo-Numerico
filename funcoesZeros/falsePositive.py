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
            erro_absoluto = higherLimit - x
            erro_relativo = abs(higherLimit - x)/higherLimit
        else:
            higherLimit = x
            erro_absoluto = x - lowerLimit
            erro_relativo = abs(lowerLimit - x)/higherLimit
    return [x, erro_absoluto, erro_relativo, i]
raiz, erro_absoluto, erro_relativo, iteracoes = falsePositive(f, 0.5, 2.5, 0.01, 10)
print('A raiz de f pelo método do falsovale {:.7f} , com erro absoluto {:.5f}, erro relativo {:.5f} e com {} iteracoes.'.format(raiz, erro_absoluto, erro_relativo, iteracoes))