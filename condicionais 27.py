# Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes categorias:
# Infantil A entre 5 a 7; Infantil B entre 8 a 10; Juvenil A entre 11 a 13; Juvenil B entre 14 a 17 e
# Sênior maiores de 18 anos.
print(" Classificação de categorias para nadadores ")
idade = int(input(" Digite sua idade: "))

if idade >= 5 and idade <=7:
    print(" Infantil A ")
elif idade >= 8 and idade <= 10:
    print(" Infantil B ")
elif idade >= 11 and idade<= 13:
    print(" Juvenial A ")
elif idade >= 14 and idade <= 17:
    print(" Juvenil B ")
elif idade >= 18:
    print(" Sênior ")
else:
    print(f"Idade = {idade} anos. Essa idade ainda não possui classificação ")






