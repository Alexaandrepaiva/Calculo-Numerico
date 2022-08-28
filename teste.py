import zeros
import numpy as np
import matplotlib.pyplot as plt
import zeros as root


def f(x):
    A = 27*x**3 + 27/2*x**4 + 9*x**5/4 + (x**6)/8
    B = 3+x
    Q = 20
    g = 9.81
    return (B)*Q**2 - g*(A)


raiz, erro, iteracoes = root.bissection(f, 0.5, 2.5, 0.0001, 10)
print('A raiz de f vale {:.7f} , com erro {:.5f} e com {} iteracoes.'.format(raiz, erro, iteracoes))
