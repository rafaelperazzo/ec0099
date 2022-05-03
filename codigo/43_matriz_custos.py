import numpy as np

def custo(A,rota):
    soma = 0
    for i in range(0,len(rota)-1,1):
        soma = soma + A[rota[i],rota[i+1]]
    return (soma)

