import numpy as np

def origem(A,k):
    soma = 0
    for j in range(0,A.shape[1],1):
        soma = soma + A[k,j]
    return (soma-1)

def destino(A,k):
    soma = 0
    for i in range(0,A.shape[0],1):
        soma = soma + A[i,k]
    return (soma-1)

def mais_chega(A):
    somas = []
    soma_coluna = 0
    for j in range(0,A.shape[1],1):
        soma_coluna = 0
        for i in range(0,A.shape[0],1):
            soma_coluna = soma_coluna + A[i,j]
        somas.append(soma_coluna-1)
    
    cidade = 0
    maximo = somas[0]
    for i in range(0,len(somas),1):
        if (somas[i]>maximo):
            cidade = i
    return (cidade)

def mao_dupla(A,k):
    for j in range(0,A.shape[1],1):
        if (k!=j):
            if (A[k,j]==A[j,k]==1):
                print(k,j)

linhas = int(input('Digite a quantidade de linhas: '))
colunas = int(input('Digite a quantidade de colunas: '))

A = np.zeros((linhas,colunas))

for i in range(0,linhas,1):
    for j in range(0,colunas,1):
        A[i,j] = float(input(f'Digite um valor pra A[{i:d}][{j:d}]'))




