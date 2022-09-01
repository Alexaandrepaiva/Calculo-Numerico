import numpy as np

A = [[1, 1/2, 1/3, 1/4],
     [1/2, 1/3, 1/4, 1/5],
     [1/3, 1/4, 1/5, 1/6],
     [1/4, 1/5, 1/6, 1/7]]

b = [[77/12], [37/10], [53/20], [218/105]]

C = np.concatenate((A, b), axis = 1)

def substRetroativa(matrix_U, matrix_b):
    n = matrix_b.size
    x_s = np.zeros(n)
    for i in reversed(range(n)):
        x_s[i] = (matrix_b[i] - matrix_U[i, i+1:]@x_s[i+1:])/matrix_U[i, i]
    return x_s

def gaussElimination(matrix_A, matrix_b):
  a = np.copy(matrix_A)
  bs = np.copy(matrix_b)
  n = bs.size
  for j in range(n-1):
    for i in range(j+1,n):
        m = a[i,j] / a[j,j]
        a[i,j:] -= m*a[j,j:]
        bs[i] -= m*bs[j]
  matrix_x = substRetroativa(a,bs)
  return matrix_x

print('A solução do sistema é: {}'.format(gaussElimination(A, b)))