def horner(c,z):
  "c= [c[n],c[n-1],...,c[1],c[0]] referente aos coeficientes do polinômio"
  "esse algoritmo avaliar o o polinômio de ordem p_n(x) no valor z"
  n=len(c)-1 # grau do polinômio
  b=[]
  b.append(c[0])
  for k in range(1,n+1):
    b.append(c[k]+b[k-1]*z)
  y=b[n]
  q=b[ :-1 ]  #coeficientes do polinômio associado
  return y,q

def newtonHorner(c,r0,tol=1.e-04,kmax=100):
  n=len(c)-1 # grau do polinômio
  raizes=[]
  iter =[]
  for k in range(n):
    niter =0
    r=r0
    delta = tol +1
    while niter < kmax and delta >= tol:
      [pr,b]=horner(c,r)
      [dpr,b]=horner(b,r)
      #método de newton
      rnovo= r -pr/dpr
      delta = abs(rnovo - r)
      #========================
      niter =niter+1
      r=rnovo
    [pr,c]=horner(c,r)
    raizes.append(r)
    iter.append(niter)
  return raizes,iter