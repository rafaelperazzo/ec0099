def mostrarInfo(vetor):
    somaPares = 0
    somaImpares = 0
    pares = []
    impares = []
    for i in range(0,len(vetor),1):
        if (vetor[i]%2==0):
            somaPares = somaPares + vetor[i]
            pares.append(vetor[i])
        else:
            somaImpares = somaImpares + vetor[i]
            impares.append(vetor[i])
    print(pares)
    print(impares)

n = int(input('Digite a quantidade de elementos: '))
a = []
for i in range(0,n,1):
    valor = int(input('Digite o valor: '))
    a.append(valor)

mostrarInfo(a)
