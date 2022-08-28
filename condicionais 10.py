# Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
# utilizando as seguintes fórmulas ( onde h corresponde a altura): homem = (72.7*h)-58:
# mulheres = (62.1*h)-44.7

altura= float(input(" Digite sua altura = "))
sexo = input(" Digite seu sexo (F/M): ")

if (sexo == " F ") or (sexo == "M"):
    peso1 = (72.7 * altura) - 58
    print(f" Seu peso = {peso1:.2f} ")
else:
    peso2 = (62.1 * altura) - 44.7
    print(f" Seu peso = {peso2:.2f} ")






