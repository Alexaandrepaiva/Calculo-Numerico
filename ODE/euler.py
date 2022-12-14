import numpy as np
import matplotlib.pyplot as plt

# Tipos de estilos de gráficos: 
# ‘Solarize_Light2’, ‘_classic_test_patch’, ‘bmh’, ‘classic’, ‘dark_background’, ‘fast’, 
# ‘fivethirtyeight’, ‘ggplot’,’grayscale’,’seaborn’,’seaborn-bright’,’seaborn-colorblind’,
# ‘seaborn-dark’, ‘seaborn-dark-palette’, ‘seaborn-darkgrid’, ‘seaborn-deep’, ‘seaborn-muted’, 
# ‘seaborn-notebook’, ‘seaborn-paper’, ‘seaborn-pastel’, ‘seaborn-poster’,’seaborn-talk’,
# ’seaborn-ticks’,’seaborn-white’,’seaborn-whitegrid’,’tableau-colorblind10′
plt.style.use('seaborn-notebook')


# Definir os parâmetros
# EDO
f = lambda t, s: np.exp(-t)
#Tamanho do espaçamento
h = 0.1
# Tempo discretizado
t = np.arange(0, 1 + h, h)
# Condição inicial
s0=-1
# Método Explicito de Euler
s = np.zeros(len(t))
s[0] = s0

for i in range(0,len(t) -1):
  s[i + 1] = s[i] + h*f(t[i], s[i])

# gráfico
plt.figure(figsize = (12, 8))
plt.plot(t, s, "r--", label="Aproximação")
plt.plot(t, -np.exp(-t), "g", label="Exato")
plt.title("Solução Exata e Aproximada de EDO")
plt.xlabel("t")
plt.ylabel("f(t)")
plt.grid()
plt.legend(loc="lower right")
plt.show()