#ENTRADA
n = int(input('Digite o tamanho da lista: '))
a = []
for i in range(0,n,1):
    numero = int(input('Digite um numero: '))
    a.append(numero)

#PROCESSAMENTO
b = []
for i in range(0,len(a),1):
    if (a[i] not in b):
        b.append(a[i])
#SAIDA
print(len(b))