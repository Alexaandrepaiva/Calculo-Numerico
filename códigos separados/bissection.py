# importar a biblioteca
import matplotlib.pyplot as plt;
import numpy as np;
import math;

def bissection(f, lowerLimit, higherLimit, tol, iterationNumber=100):
    a = lowerLimit;
    b = higherLimit;
    err = b - a;
    i = 0;

    while (err > tol):
        x = (a + b)/2;
        i = i + 1;
        
        if i >= iterationNumber:
            break;

        if(f(x) * f(a) > 0):
            a = x;

        else:
            b = x;
        err = np.abs(f(x));

    return [x, err, i]

# função em questão que quero achar a raiz
def f(x):
    return 

root_f, error, iteration = bissection(f, 0.5, 2.5, 0.01,10)

print('A raiz de f vale ' + str(root_f) + ', com erro ' + str(error) + 'e com ' + str(iteration) + ' iteracoes.')