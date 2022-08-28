# Feito por Alexandre Paiva
# Biblioteca criada para disciplina de Cálculo Numérico
import matplotlib.pyplot as plt
import numpy as np

#Definir x        Exemplo: x = np.arange(0, 3, 0.01)
#Definir y
def graph(x, y):
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    plt.plot(x, y)
    plt.show()
#print('O gráfico da função em questão no intervalo dado é:')
#zeros.graph(x, y)


#Definir f(x)      
def bissection(f, lowerLimit = -1e5, higherLimit = 1e5, tolerance = 1e-5, iterationNumber = 1e5):
    i = 0
    while (higherLimit - lowerLimit) > tolerance and i < iterationNumber:
        x = (lowerLimit + higherLimit)/2
        i = i + 1
        if f(x) * f(lowerLimit) > 0:
            lowerLimit = x
            erro = (higherLimit - x)/2
        else:
            higherLimit = x
            erro = (x - lowerLimit)/2
    return [x, erro, i]
#raiz, erro, iteracoes = zeros.bissection(f, 0.5, 2.5, 0.01, 10)
#print('A raiz de f pelo método da bisseção vale {:.7f} , com erro {:.5f} e com {} iteracoes.'.format(raiz, erro, iteracoes))


#Definir f(x)
def falsePositive(f, lowerLimit= -1e5, higherLimit = 1e5, tolerance = 1e-5, iterationNumber = 1e5):
    i = 0
    while (higherLimit - lowerLimit) > tolerance and i < iterationNumber:
        x = (lowerLimit * abs(f(higherLimit)) + higherLimit * abs(f(lowerLimit)))/(abs(f(lowerLimit)) + abs(f(higherLimit)))
        i = i + 1
        if f(x) * f(lowerLimit) > 0:
            lowerLimit = x
            erro = (higherLimit - x)/2
        else:
            higherLimit = x
            erro = (x - lowerLimit)/2
    return [x, erro, i]
#raiz, erro, iteracoes = zeros.falsePositive(f, 0.5, 2.5, 0.01, 10)
#print('A raiz de f pelo método do falsovale {:.7f} , com erro {:.5f} e com {} iteracoes.'.format(raiz, erro, iteracoes))


#Definir f(x)
#Definidir phi(x)
def fixedPoint(f, phi, initialValue, tolerance, iterationNumber):
    x_k = [initialValue]
    x_next = []
    i = 0
    while(abs(f(x_k[-1])) > tolerance and i < iterationNumber):
        x_next.append(phi(x_k[-1]))
        x_k.append(x_next[-1])
        i += 1
    erro = x_next[-1] - x_next[-2]
    return [x_k, erro, i]
#raiz, erro, iteracoes = zeros.fixedPoint(f, phi, -1, 0.001, 10)
#print('A raiz de f pelo método do ponto fixo é {:.7f} , com erro {:.5f} e com {} iteracoes.'.format(raiz, erro, iteracoes))


#Definir f(x)
#Definir dfdx(x)
def newtonRaphson(f, dfdx, initialValue, tolerance, iterationNumber):
    i = 0
    x_k = [initialValue]
    y_k = [f(initialValue)]
    while abs( f(x_k[-1]) ) > tolerance and i < iterationNumber:
        i = i + 1
        next_x = x_k[-1] - f(x_k[-1])/dfdx(x_k[-1])
        x_k.append(next_x)
        y_k.append(f(next_x))
    return [x_k[-1],i]
#raiz, iteracoes = zeros.newtonRaphson(f, dfdx, 2, 0.001, 10)
#print('A raiz de f pelo método do ponto fixo é {:.7f}  e com {} iteracoes.'.format(raiz, iteracoes))


#Definir f(x)
def secant(f, lowerLimit = -1e3, higherLimit=1e3, minValue=1e-8, iterationNumber=10000):
    i = 0
    while abs( f(lowerLimit) ) > minValue and i < iterationNumber:
        i = i + 1
        var = lowerLimit
        lowerLimit = lowerLimit - f(lowerLimit)*(lowerLimit-higherLimit)/(f(lowerLimit)-f(higherLimit))
        higherLimit = var
    return [lowerLimit, i]
#raiz, iteracoes = zeros.secant(f, 1, 2, 0.001, 100)
#print('A raiz de f pelo método d secante é {:.7f}  e com {} iteracoes.'.format(raiz, iteracoes))
