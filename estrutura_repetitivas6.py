# exercício número 6
# estrutura repetitiva
quantidade= int(input(" Digite a quantidade de números inteiros que é o valor 10:"))
soma=0

for n in range (1, 10+1):
        num= int(input(f" Insira o número {n} / {quantidade} valor:"))
        soma= soma +num
        media = soma/quantidade
print(f" A média desses números = {media}")

