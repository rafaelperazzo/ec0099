n = int(input('Digite o numero: '))
i = 1
while(i*(i+1)*(i+2)<n):
    i = i + 1

if (i*(i+1)*(i+2)==n):
    print("TRIANGULAR")
else:
    print("NAO TRIANGULAR")