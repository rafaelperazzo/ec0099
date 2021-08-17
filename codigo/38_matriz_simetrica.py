import numpy as np


def simetrica(A):
    cont = 0
    for i in range(0,linhas,1):
        for j in range(0,colunas,1):
            if A[i,j]==A[j,i]:
                cont +=1
    if cont==linhas*colunas:
        return(True)
    else:
        return(False)

linhas = int(input('Digite a quantidade de linhas: '))
colunas = int(input('Digite a quantidade de colunas: '))

A = np.zeros((linhas,colunas))

for i in range(0,linhas,1):
    for j in range(0,colunas,1):
        A[i,j] = float(input(f'Digite um valor pra A[{i:d}][{j:d}]'))

if simetrica(A):
    print("Simetrica")
else:
    print("Nao simetrica")



