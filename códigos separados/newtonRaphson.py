# importar a biblioteca
import matplotlib.pyplot as plt;
import numpy as np;
import math;

# função do método de Newton-Raphson

# esse método se aproxima da raiz ao ver onde a reta tangente a um ponto inicial de chute cruza as abcissas
# usamos y - y0 = m(x - x0) => y - f(x0) = dfdx(x0) * (x - x0) => fazemos y = 0, para ver onde cruza =>
# -f(x0) = dfdx(x0) * x - dfdx(x0) * x0 => x = x0 - f(x0)/dfdx(x0)

# recebe a função original (f), sua derivada (dfdx), o chute inicial (x0), a tolerância (tol) e
# a quantidade máxima de iterações (iterationNumber)

def newton_raphson(f, dfdx, initialValue, tol, iterationNumber):

    i = 0; # vai contar as iterações

    x_k = [initialValue]; # array com os valores testados de x
    y_k = [f(initialValue)]; # array com os correspondentes f(x)

    while(abs(f(x_k[-1])) > tol or i > iterationNumber):

        # método para calcular o próximo valor de x
        # é onde a reta tangente em initialValue cruza as abcissas
        next_x = x_k[-1] - f(x_k[-1])/dfdx(x_k[-1]);
        
        x_k.append(next_x);
        y_k.append(f(next_x));

    print(x_k);
    print(y_k);    

    return x_k[-1];

def f(x):
    return 2*x**3 - 11.7*x**2 + 17.7*x - 5;

def dfdx(x): 
    return 6*x**1 - 23.4*x + 17.7;

root_f = newton_raphson(f, dfdx, 2, 0.001, 1000);

print('A raiz de f vale ' + str(root_f));