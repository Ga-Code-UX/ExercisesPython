# exercício número 35
# estrutura repetitiva
comprovar=True
while comprovar==True:
    x = int(input(" Digite o valor inicial do intervalo: "))
    y = int(input(" Digite o valor final do intervalo:"))
    if x < y:
        comprovar=False
        print(" Numero correto ")
        soma=0
        for i in range(x,y+1):
            if (i%2) != 0:
                soma += i
        print(f" A soma dos números ímpares do intervalo {x} e {y} = {soma} ")
    else:
        print(" Intervalo de valores inválido. Tente novamente. ")

