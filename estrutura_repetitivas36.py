# exercício número 36
# estrutura repetitiva
n=100
soma=0
comprovar=True
while comprovar==True:
    if n > 0:
        comprovar=False
        print(" Numero correto ")
        soma=0
        for i in range(n+1):
            soma+= i**2
            soma1= soma**2
            diferenca= soma1-soma
        print(f" A soma dos quadrados dos 100 primeiros numeros naturais = {soma}")
        print(f" O quadrado da soma dos 100 primeiros numeros naturais = {soma1}")
        print(f" A diferença do quadrado da soma dos 100 primeiros numeros naturais menos o quadrado da soma dos quadrados dos 100 primeiros numeros naturais = {diferenca}")
    else:
        print(" Digite um número maior que zero. Tente de novo ")