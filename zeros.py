# Feito por Alexandre Paiva
# Biblioteca de zero de funções criada para disciplina de Cálculo Numérico
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
            erro_absoluto = higherLimit - x
            erro_relativo = (higherLimit - x)/higherLimit
        else:
            higherLimit = x
            erro_absoluto = x - lowerLimit
            erro_relativo = (higherLimit - x)/higherLimit
    return [x, erro_absoluto, erro_relativo, i]
#raiz, erro_absoluto, erro_relativo, iteracoes = zeros.bissection(f, 0.5, 2.5, 0.01, 10)
#print('A raiz de f pelo método da bisseção vale {:.7f} , com erro absoluto {:.5f}, erro relativo {:.5f}e com {} iteracoes.'.format(raiz, erro_absoluto, erro_relativo, iteracoes))


#Definir f(x)
def falsePosition(f, lowerLimit= -1e5, higherLimit = 1e5, tolerance = 1e-5, iterationNumber = 1e5):
    i = 0
    while (higherLimit - lowerLimit) > tolerance and i < iterationNumber:
        x = (lowerLimit * abs(f(higherLimit)) + higherLimit * abs(f(lowerLimit)))/(abs(f(lowerLimit)) + abs(f(higherLimit)))
        i = i + 1
        if f(x) * f(lowerLimit) > 0:
            lowerLimit = x
            erro_absoluto = higherLimit - x
            erro_relativo = abs(higherLimit - x)/higherLimit
        else:
            higherLimit = x
            erro_absoluto = x - lowerLimit
            erro_relativo = abs(lowerLimit - x)/higherLimit
    return [x, erro_absoluto, erro_relativo, i]
#raiz, erro_absoluto, erro_relativo, iteracoes = zeros.falsePosition(f, 0.5, 2.5, 0.01, 10)
#print('A raiz de f pelo método do falsovale {:.7f} , com erro absoluto {:.5f}, erro relativo {:.5f} e com {} iteracoes.'.format(raiz, erro_absoluto, erro_relativo, iteracoes))


#Definir f(x)
#Definidir phi(x)
def fixedPoint(f, phi, initialValue = 0, tolerance = 1e-5, iterationNumber = 1e5):
    i = 0
    x = phi(initialValue)
    while abs(initialValue - x) > tolerance and i < iterationNumber:
        i += 1
        initialValue = x
        x = phi(x)
    return [x, i]
#raiz, iteracoes = zeros.fixedPoint(f, phi, -1, 0.001, 10)
#print('A raiz de f pelo método da iteração de ponto fixo é {:.7f} e com {} iteracoes.'.format(raiz, iteracoes))

# declaração da função dada
# declaração da função de iteração
def fixedPointBra(f, phi, x0, tol = 1e-5, maxIter = 1e5):
    x_k = [x0]
    k = 0
    while(abs(f(x_k[-1])) > tol and k < maxIter):
        x_next = phi(x_k[-1])
        x_k.append(x_next)
        k += 1
    return x_k[-1]
# root = fixedPointBra(f, phi, -1, 0.0001, 10);
# print('Método do ponto fixo: a raiz vale ' + str(root));

#Definir f(x)
#Definir dfdx(x)
def newtonRaphson(f, dfdx, initialValue = 0, tolerance = 1e-5, iterationNumber = 1e5):
    i = 0
    x_k = [initialValue]
    y_k = [f(initialValue)]
    while abs( f(x_k[-1]) ) > tolerance and i < iterationNumber:
        i = i + 1
        old_x = x_k[-1]
        next_x = x_k[-1] - f(x_k[-1])/dfdx(x_k[-1])
        erro_absoluto = abs(old_x - next_x)
        erro_relativo = abs(old_x - next_x)/old_x
        x_k.append(next_x)
        y_k.append(f(next_x))
    return [x_k[-1], erro_absoluto, erro_relativo, i]
#raiz, erro_absoluto, erro_relativo, iteracoes = zeros.newtonRaphson(f, dfdx, 2, 0.001, 10)
#print('A raiz de f pelo método de Newton-Raphson é {:.7f}, com erro absoluto {}, erro relativo {} e com {} iteracoes.'.format(raiz, erro_absoluto, erro_relativo, iteracoes))


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
#print('A raiz de f pelo método da secante é {:.7f}  e com {} iteracoes.'.format(raiz, iteracoes))
