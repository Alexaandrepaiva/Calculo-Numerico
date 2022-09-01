import numpy as np

A = [[1, 1/2, 1/3, 1/4],
     [1/2, 1/3, 1/4, 1/5],
     [1/3, 1/4, 1/5, 1/6],
     [1/4, 1/5, 1/6, 1/7]]

b = [[77/12], [37/10], [53/20], [218/105]]

C = np.concatenate((A, b), axis = 1)

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

print(gaussEng(C))