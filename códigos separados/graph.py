# importar a biblioteca
import matplotlib.pyplot as plt;
import numpy as np;
import math;

x = np.arange(0, 3, 0.01)
y = 2*x

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
    
print('O gráfico da função em questão no intervalo dado é:')
graph(x, y)