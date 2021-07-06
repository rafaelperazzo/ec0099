'''
 Dados n números inteiros positivos, calcular a soma dos que são primos.
'''
n = int(input('Digite n: '))
soma = 0
for i in range(0,n,1):
    numero = int(input('Digite o numero: '))
    divisores = 0
    for j in range(2,numero,1):
        if numero%j==0:
            divisores = divisores + 1
            break
    if divisores==0:
        soma = soma + numero
print(soma)