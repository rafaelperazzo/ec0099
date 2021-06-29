#ENTRADA
a = float(input('Digite a:'))
b = float(input('Digite b:'))
c = float(input('Digite c:'))
#Calcular delta
delta = b*b - (4*a*c)
#Verificar se existem raizes reais
if (delta>=0):
    x1 = (-b+(delta**0.5))/(2*a)
    x2 = (-b-(delta**0.5))/(2*a)
    print(x1)
    print(x2)
else:
    print("Nao existem raizes reais!")
