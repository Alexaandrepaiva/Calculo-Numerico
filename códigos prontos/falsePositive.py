# importar a biblioteca
import matplotlib.pyplot as plt;
import numpy as np;
import math;

# função do método da falsa posição

def falsePositive(f, lowerLimit, higherLimit, tol, iterationNumber=100):
    a = lowerLimit;
    b = higherLimit;
    err = b - a;
    i = 0;

    while (err > tol):
        # calcula x como a média ponderada
        # de resto, idêntico à bisseção
        x = (a * abs(f(b)) + b * abs(f(a)))/(abs(f(a)) + abs(f(b)));
        i = i + 1;
        
        if i >= iterationNumber:
            break;

        if(f(x) * f(a) > 0):
            a = x;

        else:
            b = x;
        err = b - a;

    return [x, err, i]

# função em questão que quero achar a raiz
def f(x): 
    return 

root_f, error, iteration = falsePositive(f, 0.1, 2.5, 0.01,10)

print('A raiz de f vale ' + str(root_f) + ', com erro ' + str(error) + 'e com ' + str(iteration) + ' iteracoes.')