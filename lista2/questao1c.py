import math;
import numpy as np;
import matplotlib.pyplot as plt;

def falsePositive(f, lowerLimit, higherLimit, tol, iterationNumber=100):
    a = lowerLimit;
    b = higherLimit;
    err = b - a;
    i = 0;

    while (err > tol):
        x = (a * abs(f(b)) + b * abs(f(a)))/(abs(f(a)) + abs(f(b)));
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
    A = 27*x**3 + 27/2*x**4 + 9*x**5/4 + (x**6)/8
    B = 3+x
    Q = 20
    g = 9.81
    return (B)*Q**2 - g*(A)

root_f, error, iteration = falsePositive(f, 0.1, 2.5, 0.01,10)

# str(number) só transforma um número em string
print('A raiz de f vale ' + str(root_f) + ', com erro ' + str(error) + 'e com ' + str(iteration) + ' iteracoes.')