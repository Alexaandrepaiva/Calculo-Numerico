# importar a biblioteca
import matplotlib.pyplot as plt;
import numpy as np;
import math;

# função em questão que quero achar a raiz
def f(x):
    return 2*x**3 - 11.7*x**2 + 17.7*x - 5;

# derivada da função em questão que quero achar a raiz
def dfdx(x): 
    return 6*x**1 - 23.4*x + 17.7;

# função do método de Newton-Raphson
def newton_raphson(f, dfdx, initialValue, tol, iterationNumber):
    i = 0;
    x_k = [initialValue]; 
    y_k = [f(initialValue)]; 

    while(abs(f(x_k[-1])) > tol or i > iterationNumber):

        next_x = x_k[-1] - f(x_k[-1])/dfdx(x_k[-1]);
        
        x_k.append(next_x);
        y_k.append(f(next_x)); 
    
    return x_k[-1];

root_f = newton_raphson(f, dfdx, 3, 0.001, 3);

print('A raiz de f vale ' + str(root_f));