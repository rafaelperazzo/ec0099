#ENTRADA
total_eleitores = int(input('Digite a quantidade de eleitores: '))
brancos = int(input('Votos brancos: '))
nulos = int(input('Votos nulos: '))
validos = int(input('Votos validos: '))

p_brancos = (brancos/total_eleitores)*100
p_nulos = (nulos/total_eleitores)*100
p_validos = (validos/total_eleitores)*100

print(p_brancos)
print(p_nulos)
print(p_validos)