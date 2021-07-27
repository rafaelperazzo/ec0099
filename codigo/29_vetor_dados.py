def quantidades(vetor,valor):
    cont = 0
    for i in range(0,len(vetor),1):
        if vetor[i]==valor:
            cont = cont + 1
    return (cont)

#ENTRADA
n = int(input('Digite a quantidade de lancamentos: '))
lancamentos = []
for i in range(0,n,1):
    valor = int(input('Digite o lado sorteado: '))
    lancamentos.append(valor)

#SAIDA
quantos_6 = quantidades(lancamentos,6)
print(quantos_6)
