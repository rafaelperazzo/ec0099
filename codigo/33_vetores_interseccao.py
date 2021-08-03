#1 - Função que calcula a interseccao
def interseccao(a,b):
    c = []
    for i in range(0,len(a),1):
        if (a[i] in b):
            c.append(a[i])
    return c

#2 - Entrada, processamento (chamada da função) e saída
na = int(input('Digite a quantidade de numeros de a: '))
nb = int(input('Digite a quantidade de numeros de b: '))
a = []
b = []
for i in range(0,na,1):
    valor = int(input('Digite um valor para a: '))
    a.append(valor)

for i in range(0,nb,1):
    valor = int(input('Digite um valor para b: '))
    b.append(valor)

c = interseccao(a,b)
print(c)
