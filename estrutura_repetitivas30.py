# exercício número 30
# estrutura repetitiva
n=int(input(" Digite um número inteiro positivo para resolver uma sequência: "))
soma=0
soma1=0
soma2=0
for i in range(1,n + 1):
    soma += i
print(f" O somatório de n ate n , com n={n} é igual {soma}")
for x in range(1,(2*n-1)+1):
    soma1 += x
print(f" O somatório de 2n-1, com n={n} é igual {soma1}")
for y in range(1,(2*n-1)+1):
    y=y+2
    soma2 += y
print(f" O somatório de 2n-1,com razão 2 e n={n} é igual {soma2}")
