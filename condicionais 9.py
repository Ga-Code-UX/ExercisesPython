# Leia o salário de um trabalhador e o valor da prestação de um empréstimo.
# Se a prestação for maior que 20% do salário, imprima: "Empréstimo não concedido"
# caso contrário imprima: " Empréstimo concedido".

salario = float(input(" Digite seu salário = "))
prestacao = float(input(" Digite a prestação do emprétimo = "))

if prestacao > (20 * salario)/100:
    print(f" Empréstimo não concedido ")
else:
    print(" Empréstimo concedido ")





