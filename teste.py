import zeros

def f(x):
    A = 27*x**3 + 27/2*x**4 + 9*x**5/4 + (x**6)/8
    B = 3+x
    Q = 20
    g = 9.81
    return (B)*Q**2 - g*(A)

zeros.bissection(f, 0.5, 2.5, 0.01,10)

root_f, error, iteration = zeros.bissection(f, 0.5, 2.5, 0.01,10)

print('A raiz de f vale ' + str(root_f) + ', com erro ' + str(error) + 'e com ' + str(iteration) + ' iteracoes.')