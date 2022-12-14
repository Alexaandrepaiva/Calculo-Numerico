# Feito por Alexandre Paiva
# Biblioteca de sistemas lineares criada para disciplina de Cálculo Numérico

# Em algumas funções, talvez tenha-se que que importar as seguintes bibliotecas
import numpy as np
import math

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

def findRow(A, n):
    ans = -1
    for i in range(n+1, len(A)):
        if(A[i, n] != 0):
            ans = i
    return ans

# Substituicao Sucessiva - Resolve L*x = b_s. 
# Recebe L (triangular inferior), b e retona x
def substSucessiva(L, b_s):
    n=b_s.size
    xs=np.zeros(n)
    for i in range(n):
        xs[i] = (b_s[i] -L[i,:i]@xs[:i])/L[i,i]
    return xs

# Substituicao retroativa - Resolve U*x = b. 
# Recebe U (triangular superior), b e retona x
def substRetroativa(matrix_U, matrix_b):
    n = matrix_b.size
    x_s = np.zeros(n)
    for i in reversed(range(n)):
        x_s[i] = (matrix_b[i] - matrix_U[i, i+1:]@x_s[i+1:])/matrix_U[i, i]
    return x_s

#Eliminação de Gauss eng
def gaussEng(table):
    table_np = np.array(table)
    n_lines = len(table_np)
    n_colum = len(table_np[0])

    if n_lines+1!=n_colum:
        exit("Sistema sem solução")

    for i in range(n_lines):
        if table_np[i][i] !=0:
            pivot = table_np[i][i]
        else:
            for j in range(i+1,n_lines):
                if table_np[j][i]:
                    ans = list(table_np[i])
                    table_np[i] = -table_np[j]
                    table_np[j] = np.array(ans)
                    pivot = table_np[i][i]
                    break

        for j in range(i+1,n_lines):
            if not table_np[j][i]:
                continue
            else:
                table_np[j] = table_np[j]*pivot - table_np[j][i]*table_np[i]
    print(table_np)
    next_roots = list() #implementação da parte que pegar as raizes.
    for i in range(n_lines):
        soma = 0
        root = 0
        for j in range(i):
            soma += next_roots[j]*table_np[n_lines-1-i][n_colum-2-j]
        if table_np[n_lines-1-i][n_lines-1-i]:
            root =  (table_np[n_lines-1-i][n_colum-1] - soma)/table_np[n_lines-1-i][n_lines-1-i]
        next_roots.append(root)
    next_roots.reverse()
    return next_roots

#Eliminação de Gauss bigo
def gaussBigo(A, b):
    for i in range(0, len(A)):
        # pivots in case of 0 in main diagonal
        if(A[i, i] == 0):
            n = findRow(A, i)
            if(n == -1):
                print("det(A) = 0")
                break
            else:
                temp = A[i]
                A[i] = A[n]
                A[n] = temp
                temp = b[i]
                b[i] = b[n]
                b[n] = temp
        
        for j in range(1+i, len(A)):
            r = A[j, i]/A[i, i]
            b[j] -= r*b[i]
            for k in range(i, len(A)):
                A[j, k] -= r*A[i, k]
    return A, b

#Eliminação de Gauss
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

# Eliminacao de Gauss com pivotamento.- Resolve A*x = B. 
# Recebe A, B, escalona-os e depois resolve usando a funcao substRetroativa() e retorna x
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
    xs = substRetroativa(A, bs)
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

def solutionLU(matrix_A,matrix_b):
  L,U = decompositionLU(matrix_A)
  ys = substSucessiva(L,matrix_b)
  xs = substRetroativa(U,ys)
  return xs

# Decompoe matrix_A em LDL^T
# Recebe matrix_A simétrica e retorna L, D e L^T juntos na mesma matriz
def LDU(matrix_A):
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

# Resolve LL^T*X = B
# Recebe L e B e retorna x
def solutionCholeski(L, b):
    n = len(b)
    x = np.zeros((n))
    y = np.zeros((n))
    # Solução de [L]{y} = {b}
    for k in range(n):
        y[k] = (b[k] - L[k, 0:k]@y[0:k])/L[k, k]
    # Solução [L_T]{x} = {y}
    for k in range(n-1, -1, -1):
        x[k] = (y[k] - L[k+1:n, k]@x[k+1:n])/L[k, k]
    return x

# Recebe matrizes coluna c, d, e, b e retorna a solução do sistema Ax=b em que A é uma matriz tridiagonal
def tridiagonal(c,d,e,b):
  n=len(d)
  k=np.ones((n))
  t=np.ones((n))
  x =np.ones((n))
  for i in range(n):
    dem=d[i] - c[i]*t[i-1]
    k[i] =(b[i] -c[i]*k[i-1])/dem
    t[i]=e[i]/dem
  x[n-1]=k[n-1]
  for i in reversed(range(n-1)):
    x[i]=k[i] - t[i]*x[i+1]
  return x  

# Recebe matrizes coluna a, c, d, e, f, b e retorna a solução do sistema Ax=b em que A é uma matriz pentadiagonal
def pentadiagonal(a,c,d,e,f,b):
  n=len(d)
  p=np.zeros((n))
  t=np.zeros((n))
  v= np.zeros((n))
  x =np.zeros((n))
  p[0]=b[0]/d[0]
  t[0]=e[0]/d[0]
  v[0]=f[0]/d[0]
  for i in range(n):
    l=c[i] - a[i]*t[i-2]
    k=d[i] -l*t[i-1] -a[i]*v[i-2]
    p[i] =(b[i] -a[i]*p[i-2] -l*p[i-1])/k
    t[i]=(e[i]-l*v[i-1])/k
    v[i]=f[i]/k
  x[n-1]=p[n-1]
  x[n-2]=p[n-2] - t[n-2]*x[n-1]
  for i in reversed(range(n-2)):
    x[i]=p[i] - t[i]*x[i+1] -v[i]*x[i+2]
  return x

def solutionJacobi(A, b, x0, kmax=100):
    d = np.diag(A)
    for k in range(kmax):
        r = b - A@x0
        h = r/d
        if np.linalg.norm(h) < 1e-16 + 1e-16*np.linalg.norm(x0):
            return x0
        x0 += h
    return x0


def solutionGaussSeidel(A, b, x0, kmax=100):
    M = np.tril(A)
    for k in range(kmax):
        r = b - A@x0
        h = substSucessiva(M, r)
        if np.linalg.norm(h) < 1e-16 + 1e-16*np.linalg.norm(x0):
            break
        x0 += h
    return x0


def nonLinearNewton(f, x, tol=1.0e-9, kmax=100):
    def jacobiana(f, x):
        h = 1.0e-4
        n = len(x)
        J = np.zeros((n, n))
        f0 = f(x)
        for i in range(n):
            x_original = x[i]
            x[i] = x_original + h
            f1 = f(x)
            x[i] = x_original
            J[:, i] = (f1-f0)/h
        return J, f0
    for k in range(kmax):
        J, f0 = jacobiana(f, x)
        if np.linalg.norm(f0)/len(x) < tol:
            return x
        dx = gaussEliminationPivot(J, -f0)
        x = x + dx
        if np.linalg.norm(dx) < tol*max(max(abs(x)), 1.0):
            # return x
            break
    print('não convergiu')
    # else:
    #     x = None
    return x


def newtonModified(f, x, kmax=100, tau=1.0e-10, tau1=1.0e-10, tau2=1.0e-10):
    def jacobiana(f, x):
        h = 1.0e-4
        n = len(x)
        J = np.zeros((n, n))
        f0 = f(x)
        for i in range(n):
            x_original = x[i]
            x[i] = x_original + h
            f1 = f(x)
            x[i] = x_original
            J[:, i] = (f1-f0)/h
        return J, f0
    J, f0 = jacobiana(f, x)
    L, U = decompositionLU(J)
    for k in range(kmax):
     # solução do (LU)dx=-fk
        fk = f(x)
        dy = substSucessiva(L, -fk)
        dx = substRetroativa(U, dy)
        x += dx
        if np.linalg.norm(dx) < tau + tau1*np.linalg.norm(x):
            return x
        fk_velho = np.copy(fk)
        f_k_novo = f(x)  # f_{k+1}
        if np.linalg.norm(f_k_novo) >= tau2*np.linalg.norm(fk_velho):
            J, f0 = jacobiana(f, x)
            L, U = decompositionLU(J)
    print('não convergiu')
    return x

    