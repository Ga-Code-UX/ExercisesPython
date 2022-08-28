# Escreva o menu de opções abaixo. Leia a opção do usuário e execute a opção escolhida.
# Escreva uma menssagem de erro se a opção for inválida. Escolha a opção:
# 1- Soma de dois numeros;
# 2- Diferença entre dois números (maior pelo menor);
# 3- Produto entre dois números;
# 4- Divisão entre 2 números ( o denominador não pode ser zero);
print(" Escolha a opção ")
print("1-Soma de dois numeros",end=";")
print("                    2 -Diferença entre dois números (maior pelo menor); ")
print("3-Produto entre dois números ",end=";")
print("             4-Divisão entre 2 números ( o denominador não pode ser zero); ")

n = int(input(" Digite uma opção( 1, 2, 3 ou 4): "))
x = float(input(" Digite o valor de X : "))
y = float(input(" Digite o valor de Y : "))


if n == 1:
    print(" O valor de x+y = ", x+y)
elif n == 2:
    troca = x
    x = y
    y = troca
    print(" Diferença entre =", x-y)
elif n == 3:
    print(" O produto = ", x*y)
elif n == 4 and y != 0:
    print(" A divisão =", x/y)
else:
    print(" O denominador y deve diferente de zero ")


