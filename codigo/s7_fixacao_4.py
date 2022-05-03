p = int(input("Digite p: "))
q = int(input("Digite q: "))

#Contar digitos de p
digitosP = 0
temp = p
while(temp>0):
    temp = temp//10
    digitosP = digitosP + 1

#Verificando se é subnumero
contador = 0
while(q>0):
    resto = q%(10**digitosP)
    if (p==resto):
        contador = contador + 1
        break
    q = q//10

if contador>0:
    print('SIM')
else:
    print('NAO')
