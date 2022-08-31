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

    