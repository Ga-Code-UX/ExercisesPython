# exercício número 40
# estrutura repetitiva
lista = []
while True:
    n = int(input("Digite o número: "))
    lista.append(n)
    if n <= 0:
        break
print (f" O maior número da lista é: {max(lista)} e o menor número da lista = {min(lista)}")

