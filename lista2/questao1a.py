import matplotlib.pyplot as plt
import numpy as np
import math

#Definir variáveis
x = np.arange(0, 2, 0.01);
Q=20;
g=9.81;

#Definir funções
A = 27*x**3 + 27/2*x**4 + 9*x**5/4 + (x**6)/8;
B = 3+x;
y = B*Q**2 - g*A;

#Personalisar eixos
plt.title('Questão 1a')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

#Mostrar o gráfico
plt.plot(x,y)
plt.show()
