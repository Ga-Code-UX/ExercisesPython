# Usando um switch, escreva um programa que leia um número inteiro entre 1 e 12 e imprima
# o dia da semana correspondente a este número. Isto é, janeiro se 1, fevereiro se 2, e assim por diante.

## Voubusar o if no lugar de switch.

x = int(input(" Digite um número: "))

if x == 1:
    print(" Domingo ")
elif x == 2:
    print(" Segunda-feira ")
elif x == 3:
    print(" Terça-feira ")
elif x == 4:
    print(" Quarta-feira ")
elif x == 5:
    print(" Quinta-feira ")
elif x == 6:
    print(" Sexta-feira ")
elif x == 7:
    print(" Sábado ")
else:
    print(" Imprima um número entre 1 até 7 ")




