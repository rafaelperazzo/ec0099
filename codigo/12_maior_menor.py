a = int(input('Digite a: '))
b = int(input('Digite b: '))
c = int(input('Digite c: '))

#Testar se o a é o maior
if ((a>=b)and(a>=c)):
    print(a)
elif ((b>=a)and(b>=c)): #Testar se o b é o maior
    print(b)
else: #Senão é a nem b então é c
    print(c)

#Testar se o a é o menor
if ((a<=b)and(a<=c)):
    print(a)
elif ((b<=a)and(b<=c)): #Testar se o b é o menor
    print(b)
else: #Senão é a nem b então é c
    print(c)
