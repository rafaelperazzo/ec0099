'''
Escreva um programa que leia inteiros positivos m e n e os elementos de uma matriz A de números 
inteiros de dimensão m x n e conta o número de linhas e colunas que tem apenas zeros.

'''

import numpy as np

def linhas_zeros(A):
    linhas_zeros = 0
    for i in range(0,A.shape[0],1):
        cont = 0
        for j in range(0,A.shape[1],1):    
            if A[i,j]==0:
                cont+=1
        if cont==A.shape[1]:
            linhas_zeros+=1
    return(linhas_zeros)

def colunas_zeros(A):
    colunas_zeros = 0
    for i in range(0,A.shape[1],1):
        cont = 0
        for j in range(0,A.shape[0],1):    
            if A[j,i]==0:
                cont+=1
        if cont==A.shape[0]:
            colunas_zeros+=1
    return(colunas_zeros)

linhas = int(input('Digite a quantidade de linhas: '))
colunas = int(input('Digite a quantidade de colunas: '))

A = np.zeros((linhas,colunas))

for i in range(0,linhas,1):
    for j in range(0,colunas,1):
        A[i,j] = float(input(f'Digite um valor pra A[{i:d}][{j:d}]'))

print(linhas_zeros(A))
print(colunas_zeros(A))