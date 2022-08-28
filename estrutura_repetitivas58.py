# exercício número 58
# estrutura repetitiva

soma_impares = 0

a = int(input(" Digite o primeiro número: "))
b = int(input(" Digite o segundo número: "))
if b<a:
        a, b = b, a
for i in range(a, b+1):
    if i %2 !=0:
        lista = [i]
        soma_impares += i
        print(lista,end="")
print(f" . A soma do número impares de {a} ate {b} = {soma_impares}")