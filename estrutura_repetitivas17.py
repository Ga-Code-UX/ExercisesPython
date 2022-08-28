# exercício número 17
# estrutura repetitiva
n = int(input("Digite um número inteiro positivo:"))
soma = 0
for i in range(1, n + 1):
    if n > 0:
        soma += i
print(soma)