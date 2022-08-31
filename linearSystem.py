# Feito por Alexandre Paiva
# Biblioteca de sistemas lineares criada para disciplina de Cálculo Numérico

import numpy as np

def det(matrix):
    matrix_np = np.array(matrix)
    row_number = len(matrix_np)
    
    for i in range(row_number):
        if matrix_np[i][i] != 0:
            pivot = matrix_np[i][i]
        else:
            for j in range(i+1,row_number):
                if matrix_np[j][i]:
                    ans = list(matrix_np[i])
                    matrix_np[i] = -matrix_np[j]
                    matrix_np[j] = np.array(ans)
                    pivot = matrix_np[i][i]
                    break

        for j in range(i+1,row_number):
            if not matrix_np[j][i]:
                continue
            else:
                matrix_np[j] = matrix_np[j]*pivot - matrix_np[j][i]*matrix_np[i]

    return matrix_np[row_number-1][row_number-1]

# Substituicao retroativa - Resolve U*x = b_s. 
# Recebe U (triangular superior), B e retona x
def retroactiveReplacement(matrixU, b_s):
    n = b_s.size
    x_s = np.zeros(n)
    for i in reversed(range(n)):
        x_s[i] = (b_s[i] - matrixU[i, i+1:]@x_s[i+1:])/matrixU[i, i]
    return x_s

# Eliminacao de Gauss com pivotamento.- Resolve A*x = B. 
# Recebe A, B, escalona-os e depois resolve usando a funcao retroactiveReplacement() e retorna x
def gaussEliminationPivot(inA, inb):
    A = np.copy(inA)
    bs = np.copy(inb)
    n = bs.size
    for j in range(n-1):
        k = np.argmax(np.abs(A[j:, j])) + j
        if k != j:
            A[j, :], A[k, :] = A[k, :], A[j, :].copy()
            bs[j], bs[k] = bs[k], bs[j]
        for i in range(j+1, n):
            m = A[i, j]/A[j, j]
            A[i, j:] -= m*A[j, j:]
            bs[i] -= m*bs[j]
    xs = retroactiveReplacement(A, bs)
    return xs
    