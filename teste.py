import zeros
import numpy as np

def f(x):
  return 2*x**3 - 11.7*x**2 + 17.7*x - 5;

def phi(x):
    return 11.7/2 - 17.7/x/2 + 5/2*x**(-2);

def dfdx(x): 
    return 6*x**1 - 23.4*x + 17.7;

root_f = zeros.pontoFixo(f, phi, 3, 0.001, 3);
print('\nLetra B)')
print('A raiz de f pelo método do ponto fixo vale ' + str(root_f[-1]));