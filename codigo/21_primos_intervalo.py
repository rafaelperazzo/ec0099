'''
Escreva um programa em Python que mostre todos os números primos entre 2 e n. 
'''
n = int(input('Digite n: '))

for numero in range (2,n+1,1):
    divisores = 0
    for i in range(2,numero,1):
        if numero%i==0:
            divisores = divisores + 1
            break
    if divisores==0:
        print(numero)
