#ENTRADA
n = int(input('Digite n: '))
i = int(input('Digite i: '))
j = int(input('Digite j: '))
#Contador de números que atendem a condição solicitada
cont = 0 
#Numero inicial que será testado
numero = 0
#Enquando o contador for menor do que n, segue testando os números
while (cont<n):
    #Caso o numero atual atenda a condição, mostrar e incrementar o contador
    if (numero%i==0 or numero%j==0):
        print(numero)
        cont = cont + 1
    #Passar para o próximo número
    numero = numero + 1
