
def positivos(vetor):
    '''
    FUNÇÃO QUE DADO UM VETOR, 
    RETORNE OUTRO VETOR
    APENAS COM OS NÚMEROS POSITIVOS
    '''
    pos = []
    for i in range(0,len(vetor),1):
        if vetor[i]>0:
            pos.append(vetor[i])
    return (pos)

def sem_repeticao(vetor):
    '''
    FUNÇÃO QUE DADO UM VETOR, 
    RETORNA OUTRO VETOR SEM 
    VALORES REPETIDOS
    '''
    semdup = []
    for i in range(0,len(vetor),1):
        if vetor[i] not in semdup:
            semdup.append(vetor[i])
    return (semdup)

#ENTRADA
n = int(input('Digite o tamanho do vetor: '))
vet = []
for i in range(0,n,1):
    valor = int(input('Digite um valor'))
    vet.append(valor)

#PROCESSAMENTO
pos = positivos(vet)
semdup = sem_repeticao(pos)

#SAÍDA
print(pos)
print(semdup)