# Feito por Alexandre Paiva
# Biblioteca de sistemas lineares criada para disciplina de Cálculo Numérico

import numpy as np

# Determiante - Calcula o determinante de uma matriz
# Recebe matrix e retorna seu determinante
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

# Substituicao Sucessiva - Resolve L*x = b_s. 
# Recebe L (triangular inferior), B e retona x
def sucessiveReplacement(L, b_s):
    n=b_s.size
    xs=np.zeros(n)
    for i in range(n):
        xs[i] = (b_s[i] -L[i,:i]@xs[:i])/L[i,i]
    return xs

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

# Metodo do gradiente conjugado - Resolve A*x = B
# Recebe A, B e o valor inicial x0 e retona x
def linearConjugateGradient(A, b, x0, tol=1e-5):
    xk = x0
    rk = np.dot(A, xk) - b
    pk = -rk
    rk_norm = np.linalg.norm(rk)

    num_iter = 0
    curve_x = [xk]
    while rk_norm > tol:
        apk = np.dot(A, pk)
        rkrk = np.dot(rk, rk)

        alpha = rkrk / np.dot(pk, apk)
        xk = xk + alpha * pk
        rk = rk + alpha * apk
        beta = np.dot(rk, rk) / rkrk
        pk = -rk + beta * pk

        num_iter += 1
        curve_x.append(xk)
        rk_norm = np.linalg.norm(rk)
        print('Iteration: {} \t x = {} \t residual = {:.4f}'.
              format(num_iter, xk, rk_norm))

    print('\nSolution: \t x = {}'.format(xk))

    return np.array(curve_x)

#Decomposição LU - decompoõe uma matriz 
#Recebe A e retorna L e U
def decompositionLU(matrix_A):
    n = matrix_A.shape[0]
    U = np.copy(matrix_A)
    L = np.identity(n)
    for j in range(n-1):
        for i in range(j+1,n):
            m = U[i,j]/U[j,j]
            U[i,j:] -= m*U[j,j:]
            L[i,j] = m
    return L, U

# Decompoe matrix_A em LDL^T
# Recebe matrix_A e retorna L, D e L^T juntos na mesma matriz
def LDLT(matrix_A):
    a = matrix_A.copy()
    n=len(a)
    for k in range(n-1):#resolve o sistem Lv=A
        for i in range(k+1,n):
            m=a[i,k]/a[k,k]
            a[i,k+1:n] = a[i,k+1:n] - m*a[k,k+1:n]
            a[i,k]=m
        for i in range(k+1,n):
            a[k,i]=a[i,k]
    #for j in range(n):  
        #a[j,j+1:n] = a[j,j+1:n]/a[j,j]
    return a

# Fatora uma matriz simetrica, definida e positiva (x^T*A*x > 0) como A = LL^T
# Recebe A e retorna L
def choleski(A):
    L = A.copy()
    n = len(A)
    for k in range(n):
        try:
            L[k, k] = math.sqrt(L[k, k] - L[k, 0:k]@L[k, 0:k])
        except ValueError:
            print('matriz não é definita e positiva')
        for i in range(k+1, n):
            L[i, k] = (L[i, k] - L[i, 0:k]@L[k, 0:k])/L[k, k]
    for k in range(1, n):
        L[0:k, k] = 0.0
    return L

    