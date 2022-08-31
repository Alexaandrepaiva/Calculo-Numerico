# importar a biblioteca
import matplotlib.pyplot as plt;
import numpy as np;
import math;

# função do método secante
def secant(f, lowerLimit=-1e3, higherLimit=1e3,minValue = 1e-8, iterationNumber=10000):
    i = 0 
    c1 = lowerLimit
    c0 = higherLimit
    for i in range(iterationNumber):
        var = c1
        c1 = c1 - f(c1)*(c1-c0)/(f(c1)-f(c0))
        c0 = var

        if abs(f(c1)) < minValue:
            break

    return [c1,i]