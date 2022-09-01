import matplotlib.pyplot as plt
import numpy as np
import math

R = 3
V = 30

x = np.linspace(0,3,1000)

def f(x):
  return (-1) * np.pi * x**3 + 3 * np.pi * R * x**2 - 3*V

def dfdx(x):
  return (-3)*np.pi*x**2 + 6*np.pi*R*x

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
        print(f'O {i} erro relativo é: {erro_relativo}')
        x_k.append(next_x)
        y_k.append(f(next_x))
    return [x_k[-1], erro_absoluto, erro_relativo, i]

graph(x,f(x))

raiz, erro_absoluto, erro_relativo, iteracoes = newtonRaphson(f, dfdx, 2.5, 1e-7, 3)
print('A raiz de f pelo método de Newton-Raphson é {:.7f} com {} iteracoes.'.format(raiz, iteracoes))