n = int(input('Digite n: '))
soma = 0
for iteracao in range(0,n,1):
    numero = int(input('Digite um numero: '))
    divisores = 0
    for i in range(2,numero,1):
        if numero%i==0:
            divisores = divisores + 1
            break
    if divisores==0:
        soma = soma + numero
    
print(soma)    