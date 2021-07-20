n = int(input('Digite n: '))
primeiro_impar = (n*n)-(n-1)
ultimo_impar = (n*n)+n-1
#SOLUÇÃO 1: Sabendo o primeiro e último ímpar
for numero in range(primeiro_impar,ultimo_impar+1,2):
    print(numero)

'''
#SOLUÇÃO 2: Sabendo o primeiro ímpar
print(primeiro_impar)
for i in range(1,n,1):
    primeiro_impar = primeiro_impar + 2
    print(primeiro_impar)
'''
#SOLUÇÃO 3: Sabendo o último ímpar, somar até somatório=N^3
print("SOLUCAO 3")
soma = 0
soma = soma + primeiro_impar
while (soma<=(n*n*n)):
    print(primeiro_impar)
    primeiro_impar = primeiro_impar + 2
    soma = soma + primeiro_impar
