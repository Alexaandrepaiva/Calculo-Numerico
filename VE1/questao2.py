import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.7,0.85,100)

def f(x):
    g=9.8
    return g*(np.sinh(x) - np.sin(x)) - 2*x

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
            erro_absoluto = higherLimit - x
            erro_relativo = (higherLimit - x)/higherLimit
        else:
            higherLimit = x
            erro_absoluto = x - lowerLimit
            erro_relativo = (higherLimit - x)/higherLimit
    return [x, erro_absoluto, erro_relativo, i]

print(graph(x, f(x))) #Gráfico para estimar a raiz: raiz estimada = 0.781

x, erro_1, erro_2, iteracoes = bissection(f,0.7, 0.85, 1e-5, 1e10)
print('A raiz do problema é {} com {} iterações'.format(x,iteracoes))
