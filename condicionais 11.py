# Faça um programa que leia um número inteiro maior do que zero e devolva na tela,a soma de
# de todos os seus algorismos. Se o número lido for menor do que zero o programa
# terminará com a mensagem " número inválido".
import math
x = int(input(" Digite um número = "))
soma = 0
if x > 0:
    while x != 0:
        resto = x % 10
        x = (x- resto) // 10
        soma = soma + resto
    print(soma)
else:
    print( " Número inválido ")




