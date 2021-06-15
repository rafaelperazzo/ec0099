'''
Dado um polígono convexo de n lados, podemos 
calcular o número de diagonais diferentes (nd) desse polígono, pela fórmula:
'''
n = int(input('Digite a quantidade de lados: '))
nd = (n*(n-3))/2
print(nd)
