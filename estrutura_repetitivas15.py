# exercício número 15
# estrutura repetitiva
n = int(input("Digite um número inteiro positivo impar:"))
for i in range( 1,n+1):
    if (n>0 and n%2!=0) and (i%2!=0 and i >0):
        print(i)
print(f"Todos esse númemeros até o número {n} que foi digitado são impares")