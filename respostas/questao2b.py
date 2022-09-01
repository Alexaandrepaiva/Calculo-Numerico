# importar a biblioteca
import matplotlib.pyplot as plt;
import numpy as np;
import math;

# função em questão que quero achar a raiz
def f(x):
    return 2*x**3 - 11.7*x**2 + 17.7*x - 5;

#função phi convergente
def phi(x):
    return 11.7/2 - 17.7/x/2 + 5/2*x**(-2);

# função do método do ponto fixo
def pontoFixo(f, phi, initialValue, tol, iterationNumber):

    x_k = [initialValue]; 
    k = 0; 

    while(abs(f(x_k[-1])) > tol and k < iterationNumber):

        x_next = phi(x_k[-1]);
        x_k.append(x_next);
        k += 1;
        
    return x_k;

root_f = pontoFixo(f, phi, 3, 0.001, 3);
print('A raiz de f vale ' + str(root_f[-1]));