def novoVetor(vetor):
    b = []
    for i in range(0,len(vetor),1):
        fracionaria = vetor[i]%10
        if (vetor[i]%7==0) or (fracionaria==7):
            b.append(vetor[i])
    return (b)

n = int(input('Digite a quantidade de elementos: '))
a = []
for i in range(0,n,1):
    valor = int(input('Digite o valor: '))
    a.append(valor)
print(novoVetor(a))
