import numpy as np
import matplotlib.pyplot as plt

def EDO_Euler(f,t0,tf,s0=0,n=100):
  h=(tf -t0)/n
  t = np.arange(t0, tf + h, h)
  s = np.zeros(len(t))
  s[0] = s0
  for i in range(0,len(t) -1):
    s[i + 1] = s[i] + h*f(t[i], s[i])
  return [t,s]

def EDO_Heun(f,t0,tf,s0=0,n=100):
  h=(tf -t0)/n
  t = np.arange(t0, tf + h, h)
  s = np.zeros(len(t))
  s[0] = s0
  for i in range(0,len(t) -1):
    s[i + 1] = s[i] + h*f(t[i], s[i]) #primeira aproximação
    s[i+1] = s[i] + (h/2)*(f(t[i], s[i]) + f(t[i+1], s[i+1])) # Fórmula de Heun
  return [t,s]