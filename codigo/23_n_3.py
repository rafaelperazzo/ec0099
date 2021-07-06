'''
Sabe-se que um número da forma n3 é igual a soma de n ímpares consecutivos.
Escreva um programa em Python que mostre os n ímpares consecutivos para um dado valor de n. 

'''
n = int(input('Digite n: '))
ultimo_impar = (n*(n+1))-1
primeiro_impar = ultimo_impar - ((n-1)*2)
for impar in range(primeiro_impar,ultimo_impar+1,2):
    print(impar)