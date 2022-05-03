import numpy as np


def media_diagonal(A):
    soma = 0
    for i in range(0,A.shape[0],1):
        soma = soma + A[i,i]
    media = soma/A.shape[0]
    return media

linhas = int(input('Digite a quantidade de linhas: '))
colunas = int(input('Digite a quantidade de colunas: '))

A = np.zeros((linhas,colunas))

for i in range(0,linhas,1):
    for j in range(0,colunas,1):
        A[i,j] = float(input(f'Digite um valor pra A[{i:d}][{j:d}]'))

print(media_diagonal(A))
