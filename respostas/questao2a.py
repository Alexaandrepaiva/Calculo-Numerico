import matplotlib.pyplot as plt;
import numpy as np;
import math;

#Definir variáveis

x = np.arange(-2, 5, 0.01);

#Definir funções

y = 2*x**3 - 11.7*x**2 + 17.7*x - 5;

#Personalisar eixos
plt.title('Gráfico da questão X')
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