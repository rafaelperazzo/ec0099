import numpy as np

#FUNÇÕES PARA RESOLUÇÃO DO PROBLEMA

def max(A):
    maior = A[0,0]
    lin = 0
    col = 0
    for i in range(0,A.shape[0],1):
        for j in range(0,A.shape[1],1):
            if (A[i,j]>maior):
                maior = A[i,j]
                lin = i
                col = j
    return(maior,i,j)

def zeros_linhas(A):
    soma_linha = 0
    linhas_zeros = 0

    for i in range(0,A.shape[0],1):
        soma_linha = 0
        for j in range(0,A.shape[1],1):
            soma_linha = soma_linha + A[i,j]
        if (soma_linha==0):
            linhas_zeros = linhas_zeros + 1
    
    return (linhas_zeros)

def zeros_colunas(A):
    soma_coluna = 0
    colunas_zeros = 0

    for i in range(0,A.shape[0],1):
        soma_coluna = 0
        for j in range(0,A.shape[1],1):
            soma_coluna = soma_coluna + A[j,i]
        if (soma_coluna==0):
            colunas_zeros = colunas_zeros + 1
    return(colunas_zeros)


#INÍCIO DO PROGRAMA -   ENTRADAS
linhas = int(input('Digite a quantidade de linhas: '))
colunas = int(input('Digite a quantidade de colunas: '))

A = np.zeros((linhas,colunas))

for i in range(0,linhas,1):
    for j in range(0,colunas,1):
        A[i,j] = int(input('Digite o valor do elemento: '))

#PROCESSAMENTO - CHAMADA DAS FUNÇÕES
print(zeros_linhas(A))
print(zeros_colunas(A))