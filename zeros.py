# Feito por Alexandre Paiva
# Biblioteca criada para disciplina de Cálculo Numérico
import matplotlib.pyplot as plt
import numpy as np

def graph(x, y):
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    plt.plot(x, y)
    plt.show()


def bissection(f, lowerLimit = -1e5, higherLimit = 1e5, tolerance = 1e-5, iterationNumber = 1e5):
    i = 0
    while (higherLimit - lowerLimit) > tolerance and i < iterationNumber:
        x = (lowerLimit + higherLimit)/2
        i = i + 1
        if f(x) * f(lowerLimit) > 0:
            lowerLimit = x
            erro = (higherLimit - x)/2
        else:
            higherLimit = x
            erro = (x - lowerLimit)/2
    return [x, erro, i]
#raiz, erro, iteracoes = zeros.bissection(f, 0.5, 2.5, 0.01, 10)
#print('A raiz de f pelo método da bisseção vale {:.7f} , com erro {:.5f} e com {} iteracoes.'.format(raiz, erro, iteracoes))

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
#raiz, erro, iteracoes = zeros.falsePositive(f, 0.5, 2.5, 0.01, 10)
#print('A raiz de f pelo método do falsovale {:.7f} , com erro {:.5f} e com {} iteracoes.'.format(raiz, erro, iteracoes))

def fixedPoint(f, phi, initialValue, tolerance, iterationNumber):
    x_k = [initialValue]
    i = 0
    while(abs(f(x_k[-1])) > tolerance and i < iterationNumber):
        x_next = phi(x_k[-1])
        x_k.append(x_next)
        i += 1
    erro = x_next[-1] - x_next[-2]
    return [x_k, erro, i]


def newton_raphson(f, dfdx, initialValue, tolerance, iterationNumber):

    i = 0  # vai contar as iterações

    x_k = [initialValue]  # array com os valores testados de x
    y_k = [f(initialValue)]  # array com os correspondentes f(x)

    while(abs(f(x_k[-1])) > tolerance or i > iterationNumber):

        # método para calcular o próximo valor de x
        # é onde a reta tangente em initialValue cruza as abcissas
        next_x = x_k[-1] - f(x_k[-1])/dfdx(x_k[-1])

        x_k.append(next_x)
        y_k.append(f(next_x))

    print(x_k)
    print(y_k)

    return x_k[-1]


def secant(f, lowerLimit=-1e3, higherLimit=1e3, minValue=1e-8, iterationNumber=10000):
    i = 0
    c1 = lowerLimit
    c0 = higherLimit
    for i in range(iterationNumber):
        var = c1
        c1 = c1 - f(c1)*(c1-c0)/(f(c1)-f(c0))
        c0 = var

        if abs(f(c1)) < minValue:
            break

    return [c1, i]
