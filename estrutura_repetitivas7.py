# exercício número 7
# estrutura repetitiva
quantidade= int(input(" Digite a quantidade de números inteiro que é o valor 10:"))
soma=0

for n in range (1, 10+1):
        num= int(input(f" Insira o número {n} / {quantidade} valor:"))
        if num >=0:
                soma= soma +num
                media = soma/quantidade
        else:
                print(" Digite um número maior que zero")
print(f" A média desses números = {media}")






