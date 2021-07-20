m = int(input('Digite m: '))

for n in range(1,m+1,1):
    primeiro_impar = (n*n)-(n-1)
    ultimo_impar = (n*n)+n-1
    #SOLUÇÃO 1: Sabendo o primeiro e último ímpar
    print("*****************" + str(n) + "*************************")
    for numero in range(primeiro_impar,ultimo_impar+1,2):
        print(numero)