'''
Escreva uma função MAX que recebe como entrada uma matriz inteira A e devolve três inteiros: k, lin e col. 
O inteiro k é um maior elemento de A e é igual a A[lin,col].

'''
import numpy as np

def max(A):
    maior = A[0,0]
    lin = 0
    col = 0
    for i in range(0,A.shape[0],1):
        for j in range(0,A.shape[1],1):   
            if A[i,j]>maior:
                maior = A[i,j]
                lin = i
                col = j
    return(maior,lin,col)


linhas = int(input('Digite a quantidade de linhas: '))
colunas = int(input('Digite a quantidade de colunas: '))

A = np.zeros((linhas,colunas))

for i in range(0,linhas,1):
    for j in range(0,colunas,1):
        A[i,j] = int(input(f'Digite um valor pra A[{i:d}][{j:d}]'))

print(max(A))