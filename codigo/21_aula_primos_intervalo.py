#ENTRADA
n = int(input('Digite n: '))
#Montar a repetição do intervalo
for numero in range(2,n,1):
    divisores = 0
    #Procurando divisores...
    for i in range(2,numero,1):
        if numero%i==0:
            divisores = divisores + 1
            break
    if divisores==0:
        print(numero)
