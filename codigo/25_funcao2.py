'''
Escreva uma função que receba um valor inteiro n como parâmetro, e retorno verdadeiro (True), 
caso n seja primo, e falso(False) caso n não seja primo
'''
def primo(n):
    contador = 0
    for i in range(2,n,1):
        if n%i==0:
            contador = contador + 1
            break
    if contador==0:
        return(True)
    else:
        return (False)

if primo(7):
    print("PRIMO")

if primo(199987):
    print("PRIMO")
else:
    print("NAO PRIMO")
    
    