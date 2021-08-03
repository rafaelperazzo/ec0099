#1 - Função para verificar se um número é primo
def primo(numero):
    divisores = 0
    for i in range(2,int(numero/2),1):
        if numero%i==0:
            divisores = divisores + 1
            break
    if divisores==0:
        return True
    else:
        return False

#2 - Números primos, com as respectivas posições
def primos_posicoes(vetor):
    for i in range(0,len(vetor),1):
        if (primo(vetor[i])):
            print(vetor[i],i)

#3 - Entrada, processamento (chamada da função) e saída
n = int(input('Digite a quantidade de numeros: '))
dados = []
for i in range(0,n,1):
    valor = int(input('Digite um valor: '))
    dados.append(valor)

primos_posicoes(dados)
