#Feito por Alexandre Paiva
import matplotlib.pyplot as plt;
import numpy as np;

def bissection(f, lower_limit = -1e5, higher_limit = 1e5, tolerance = 1e-5, iteration_number = 1e3):
    i = 0
    for i in range(iteration_number):
        mid_point = (lower_limit + higher_limit)/2
        if f(lower_limit)*f(higher_limit) > 0:
            return "Intervalo não apresenta apenas uma raiz"
        elif f(lower_limit)*f(mid_point) < 0:
            higher_limit = mid_point
            erro = (mid_point - lower_limit )/2
        else:
            lower_limit = mid_point
            erro = (higher_limit - mid_point)/2
            
        if abs(f(mid_point)) < tolerance:
            break
        
    return [mid_point, erro, iteration_number]
        
            