# Escreva um programa que receba dois números, mostre na tela o maior deles e
#  se por acaso os dois números forem iguais mostre uma mensagem "números iguais"
a = int(input(" Digite um número:"))
b = int(input(" Digite outro número:"))

if a < b:
    maior = b
elif a > b:
    maior = a
    print(f"Maior = {maior} ")
else:
    a == b
    print(" Números iguais ")









