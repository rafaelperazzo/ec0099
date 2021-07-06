'''
Sabe-se que um número da forma n3 é igual a soma de n ímpares consecutivos.
Exemplo: 13= 1, 23= 3+5, 33= 7+9+11,  43= 13+15+17+19,...
Dado m, determine os ímpares consecutivos cuja soma é igual a n3 para n assumindo valores de 1 a m.

'''
m = int(input('Digite m: '))
for n in range (1,m,1):
    ultimo_impar = (n*(n+1))-1
    primeiro_impar = ultimo_impar - ((n-1)*2)
    print(n)
    for impar in range(primeiro_impar,ultimo_impar+1,2):
        print(impar)