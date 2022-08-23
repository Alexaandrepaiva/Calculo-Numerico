# Feito por Alexandre Paiva
# Biblioteca criada para disciplina de Cálculo Numérico
import numpy as np
import matplotlib.pyplot as plt


def graphically(xGraph, yGraph):
    plt.title('Questão 1a')
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    # Mostrar o gráfico
    plt.plot(xGraph, yGraph)
    plt.show()


def bissection(f, lowerLimit, higherLimit, tol, iterationNumber=100):
    err = higherLimit - lowerLimit
    i = 0

    while ((err > tol) and (i >= iterationNumber)):
        x = (lowerLimit + higherLimit)/2
        i = i + 1

        if(f(x) * f(lowerLimit) > 0):
            lowerLimit = x

        else:
            higherLimit = x
        err = np.abs(f(x))

    return [x, err, i]


def pontoFixo(f, phi, initialValue, tol, iterationNumber):
    x_k = [initialValue]
    i = 0

    while(abs(f(x_k[-1])) > tol and i < iterationNumber):
        x_next = phi(x_k[-1])
        x_k.append(x_next)
        i += 1

    err = x_next[-1] - x_next[-2]

    return [x_k, err, i]


def falsePositive(f, lowerLimit, higherLimit, tol, iterationNumber=100):
    a = lowerLimit
    b = higherLimit
    err = b - a
    i = 0

    while (err > tol):
        # calcula x como a média ponderada
        # de resto, idêntico à bisseção
        x = (a * abs(f(b)) + b * abs(f(a)))/(abs(f(a)) + abs(f(b)))
        i = i + 1

        if i >= iterationNumber:
            break

        if(f(x) * f(a) > 0):
            a = x

        else:
            b = x
        err = b - a

    return [x, err, i]


def newton_raphson(f, dfdx, initialValue, tol, iterationNumber):

    i = 0  # vai contar as iterações

    x_k = [initialValue]  # array com os valores testados de x
    y_k = [f(initialValue)]  # array com os correspondentes f(x)

    while(abs(f(x_k[-1])) > tol or i > iterationNumber):

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
