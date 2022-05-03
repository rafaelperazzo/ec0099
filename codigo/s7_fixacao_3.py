for i in range(1000,9999,1):
    #separando os numeros
    parte1 = i//100
    parte2 = i%100
    raizDeI = i**(0.5)
    if (raizDeI==parte1+parte2):
        print(i)
