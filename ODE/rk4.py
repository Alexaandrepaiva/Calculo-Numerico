import numpy as np
import matplotlib.pyplot as plt

# Tipos de estilos de gráficos: 
# ‘Solarize_Light2’, ‘_classic_test_patch’, ‘bmh’, ‘classic’, ‘dark_background’, ‘fast’, 
# ‘fivethirtyeight’, ‘ggplot’,’grayscale’,’seaborn’,’seaborn-bright’,’seaborn-colorblind’,
# ‘seaborn-dark’, ‘seaborn-dark-palette’, ‘seaborn-darkgrid’, ‘seaborn-deep’, ‘seaborn-muted’, 
# ‘seaborn-notebook’, ‘seaborn-paper’, ‘seaborn-pastel’, ‘seaborn-poster’,’seaborn-talk’,
# ’seaborn-ticks’,’seaborn-white’,’seaborn-whitegrid’,’tableau-colorblind10′
plt.style.use('bmh')

def ODE_RK4(f,t0,tf,s0=0,n=100):
  h=(tf -t0)/n
  t = np.arange(t0, tf + h, h)
  s = np.zeros(len(t))
  s[0] = s0
  for i in range(0,len(t) -1):
    f1= h*f(t[i], s[i]) 
    f2= h*f(t[i]+ h/2, s[i] + f1/2)
    f3= h*f(t[i]+ h/2, s[i] + f2/2)
    f4= h*f(t[i]+ h, s[i] + f3)
    s[i+1] = s[i] + (f1 + 2*(f2+f3) + f4)/6
  return [t,s]

f = lambda t, s: np.exp(-t)
[t,s] = ODE_RK4(f,0,1,-1,2)
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