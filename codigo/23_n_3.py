m = int(input('Digite m: '))
for n in range (1,m,1):
    ultimo_impar = (n*(n+1))-1
    primeiro_impar = ultimo_impar - ((n-1)*2)
    print(n)
    for impar in range(primeiro_impar,ultimo_impar+1,2):
        print(impar)