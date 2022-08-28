# Faça um programa que mostre ao usuário um menu com 4 opções de operações
# matemáticas ( as básicas , por exemplo). O usuário escolhe uma das opções e
# o seu programa pede dois valores númericos e realiza a operaçõe
# mostrando o resultado e saindo.

print(" Digite o número de uma das opções abaixo ")
print(" 1 = Adição        ---> " ,end="")
print(" 2 = Subtração ")
print(" 3 = Multiplicação ---> ", end="")
print(" 4 = Divisão ")

a = float(input(" Digite  a opção 1, 2, 3 ou 4 : "))
x = float(input(" Digite o valor de x: "))
y = float(input(" Digite o valor de y: "))

if a == 1:
        adicao = x + y
        print(f"Você escolheu a soma. A soma de x e y = {adicao:.2f} ")
elif a == 2:
        subtracao = x - y
        print(f" x - y =  {subtracao:.2f}")
elif a == 3:
        multiplicacao = x * y
        print(f" Você escolheu a multiplicação. A multiplicação de x e y = {multiplicacao:.2f}")
elif a == 4:
        divisao = x / y
        print(f" Você escolheu a divisão. A divisão de x e y = {divisao:.2f}")
else:
        print (" Número inválido. Digite uma opção entre 1 e 4 ")
