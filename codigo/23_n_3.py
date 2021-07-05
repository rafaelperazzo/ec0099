n = int(input('Digite n: '))
ultimo_impar = (n*(n+1))-1
primeiro_impar = ultimo_impar - ((n-1)*2)
for impar in range(primeiro_impar,ultimo_impar+1,2):
    print(impar)