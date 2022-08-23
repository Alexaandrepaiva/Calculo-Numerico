# importar a biblioteca
import matplotlib.pyplot as plt;
import numpy as np;
import math;

# função do método do ponto fixo
def pontoFixo(f, phi, initialValue, tol, iterationNumber):

    x_k = [initialValue]; 
    k = 0; 

    while(abs(f(x_k[-1])) > tol and k < iterationNumber):

        x_next = phi(x_k[-1]);
        x_k.append(x_next);
        k += 1;
        
    return x_k;

def f(x):
    return 

def phi(x):
    return (-1) * math.sqrt((math.e) ** x);

root_f = pontoFixo(f, phi, -1, 0.001, 20);
print('A raiz de f vale ' + str(root_f[-1]));