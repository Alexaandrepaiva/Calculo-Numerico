# importar a biblioteca
import matplotlib.pyplot as plt;
import numpy as np;
import math;

#Definir variáveis
x = np.arange(0, 3, 0.01);

#Definir funções
y = 2*2**2 - 4*4;

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