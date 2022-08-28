# exercício número 42
# estrutura repetitiva
import  math
lista = []
while True:
    numero = int(input(" Digite um número:"))
    lista.append(numero)
    if numero <= 0:
        print(" O programa parou porque digitou número menor ou igual a zero ")
        break
    for i in lista:
        x = [i**2], [i**3], [math.sqrt(i)]
    print(f" O quadrado, o cubo e a raiz quadrada de {i} é respectivamente = {x}")

