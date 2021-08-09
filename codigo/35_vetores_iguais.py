def iguais(a,b):
    if (len(a)!=len(b)):
        return (False)
    contador = 0
    for i in range(0,len(a),1):
        if a[i]==b[i]:
            contador = contador + 1
    if (contador==len(a)):
        return (True)
    else:
        return (False)

n = int(input('Digite a quantidade de elementos: '))
a = []
b = []
for i in range(0,n,1):
    valor = int(input('Digite o valor: '))
    a.append(valor)

for i in range(0,n,1):
    valor = int(input('Digite o valor: '))
    b.append(valor)

if (iguais(a,b)):
    print("Vetores iguais!")
else:
    print("Vetores diferentes!!")
