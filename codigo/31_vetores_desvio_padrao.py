#1 - Calculando a média aritmética
def media(vetor):
    soma = 0
    for i in range(0,len(vetor),1):
        soma = soma + vetor[i]
    media  = soma/len(vetor)
    return media

#2 - Calculando o desvio padrão
def desvio_padrao(vetor):
    m = media(vetor)
    soma = 0
    for i in range(0,len(vetor),1):
        soma = soma + ((vetor[i]-m)**2)
    temp = soma*(1/(len(vetor)-1))
    desv_pad = temp**(0.5)
    return desv_pad

#3 - Entrada, processamento (chamada das funções) e Saída
n = int(input('Digite a quantidade de elementos: '))
dados = []
for i in range(0,n,1):
    valor = float(input('Digite um valor'))
    dados.append(valor)

desv_pad = desvio_padrao(dados)
print(desv_pad)

