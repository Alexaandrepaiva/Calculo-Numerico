# Feito por Alexandre Paiva
# Biblioteca de autovalores e autovetores criada para disciplina de Cálculo Numérico

# Em algumas funções, talvez tenha-se que que importa algumas das seguintes bibliotecas
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
plt.style.use("seaborn-poster")


# A = np.array([[2, 0],[0, 1]])
# x = np.array([[1],[1]])
# b = np.dot(A, x)
def plot_vect(x, b, xlim, ylim):
  plt.figure(figsize = (10, 6))
  plt.quiver(0,0,x[0],x[1],\
    color="r",angles="xy",\
    scale_units="xy",scale=1,\
    label="Vetor Original")
  plt.quiver(0,0,b[0],b[1],\
    color="g",angles="xy",\
    scale_units="xy",scale=1,\
    label ="Vetor Transformado")
  plt.xlim(xlim)
  plt.ylim(ylim)
  plt.xlabel("X")
  plt.ylabel("Y")
  plt.legend()
# plot_vect(x,b,(0,3),(0,2))

def faddeev_leverrier(A):
    A = np.array(A) #garantir que a matriz é quadrada
    n = A.shape[0]
    assert A.shape[1] == n, 'Matriz deve ser quadrada!'
    a = np.array([1.])
    Ak = np.array(A)
    for k in range(1, n + 1):
        ak = -Ak.trace() / k
        a = np.append(a, ak)
        Ak += np.diag(np.repeat(ak, n))
        Ak = np.dot(A, Ak)
    return (-1)**n*a

def autovet(A,autvalx):
    """ Algoritmo retirado do livro Métodos de Cálculo Numérico, Dieguez(2015), pag 177""" 
    A = np.array(A) #garantir que a matriz é quadrada
    n = A.shape[0]
    assert A.shape[1] == n, 'Matriz deve ser quadrada!'
    X= np.eye(n)
    a = np.array([1.])
    Ak = np.array(A)
    for k in range(1, n):
        ak =-Ak.trace()/k
        Ak += np.diag(np.repeat(ak, n))
        L=np.diag(autvalx)
        #Xt = L@np.transpose(X) + np.transpose(Ak)
        #X =np.transpose(Xt)
        X=X@L + Ak # Equação retirada Dieguez (2005)
        Ak = np.dot(A, Ak)
    for k in range(n):
        X[:,k]/= LA.norm(X[:,k])
    return X

def dec_lr(A):
  "esta função é igual a decomposição LU"
  n = A.shape[0]
  R = np.copy(A)
  L = np.identity(n)
  for j in range(n-1):
    for i in range(j+1,n):
      m = R[i,j]/R[j,j]
      R[i,j:] -= m*R[j,j:]
      L[i,j] = m
  return L, R

def metodo_lr(A,kmax=200):
  Ak = np.copy(A)
  for k in range(kmax):
    L,R = dec_lr(Ak)
    Ak = R@L
  auto_valor = np.diag(Ak)
  return auto_valor , Ak, R

def householder(x,k):
  "transformação de Holserholder para zerar parte do vetor x começando na posição k+1"
  n = x.size
  w=np.zeros(n)
  sum = x[k+1 :]@x[k+1 :]
  gk = np.sqrt(x[k]**2 + sum)
  c=np.sqrt((x[k] + gk)**2 + sum)
  w[k] = (x[k] +gk)/c
  w[k+1 :] = x[k+1 :]/c
  H = np.eye(n) - 2*np.outer(w,w.T)
  return H

def meu_QR(A):
  "fatoração QR"
  n=A.shape[0]
  R= np.copy(A)
  Q= np.eye(n)
  for k in range(n-1):
    H= householder(R[:,k],k)
    R=H@R
    Q=Q@H
  return Q , R

def autoval_qr(A,kmax=200):
  T = np.copy(A)
  for k in range(kmax):
    Q,R = meu_QR(T)
    T = R@Q
  auto_valor = np.diag(T)
  return auto_valor , T