'''
Escreva uma função que calcule a soma n primeiros termos da série de fibonacci. 
1,1,2,3,5,8,13,21,...
'''

def soma_fibonacci(n):
    a1 = 1
    a2 = 1
    soma = 2
    for i in range(3,n+1,1):
        prox = a1 + a2
        soma = soma + prox
        a1 = a2
        a2 = prox
    return(soma)

n = int(input('Digite o termo:'))
if (n==1):
    print(1)
elif (n==2):
    print(2)
else:
    print(soma_fibonacci(n))
