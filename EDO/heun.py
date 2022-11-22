#Também conhecido como o método trapezoidal
import numpy as np
import matplotlib.pyplot as plt

# Tipos de estilos de gráficos: 
# ‘Solarize_Light2’, ‘_classic_test_patch’, ‘bmh’, ‘classic’, ‘dark_background’, ‘fast’, 
# ‘fivethirtyeight’, ‘ggplot’,’grayscale’,’seaborn’,’seaborn-bright’,’seaborn-colorblind’,
# ‘seaborn-dark’, ‘seaborn-dark-palette’, ‘seaborn-darkgrid’, ‘seaborn-deep’, ‘seaborn-muted’, 
# ‘seaborn-notebook’, ‘seaborn-paper’, ‘seaborn-pastel’, ‘seaborn-poster’,’seaborn-talk’,
# ’seaborn-ticks’,’seaborn-white’,’seaborn-whitegrid’,’tableau-colorblind10′
plt.style.use('Solarize_Light2')

def EDO_Heun(f,t0,tf,s0=0,n=100):
  h=(tf -t0)/n
  t = np.arange(t0, tf + h, h)
  s = np.zeros(len(t))
  s[0] = s0
  for i in range(0,len(t) -1):
    s[i + 1] = s[i] + h*f(t[i], s[i]) #primeira aproximação
    s[i+1] = s[i] + (h/2)*(f(t[i], s[i]) + f(t[i+1], s[i+1])) # Fórmula de Heun
  return [t,s]

f = lambda t, s: np.exp(-t)
[t,s] = EDO_Heun(f,0,1,-1,2)
# gráfico
plt.figure(figsize = (12, 8))
plt.plot(t, s, "y--", label="Aproximação")
plt.plot(t, -np.exp(-t), "g", label="Exato")
plt.title("Solução Exata e Aproximada de EDO")
plt.xlabel("t")
plt.ylabel("f(t)")
plt.grid()
plt.legend(loc="lower right")
plt.show()