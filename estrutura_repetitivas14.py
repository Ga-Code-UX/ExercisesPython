# exercício número 14
# estrutura repetitiva
n = int(input("Digite um número inteiro:"))
for i in range( n+1,0,-1):
    if (n>0 and n%2==0) and (i%2==0 and i >0):
        print(i)