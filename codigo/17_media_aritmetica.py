n = int(input('Digite a quantidade de numeros: '))
soma = 0
for i in range(0,n,1):
    x = int(input('Digite um numero: '))
    soma = soma + x

media = soma/n
print(media)