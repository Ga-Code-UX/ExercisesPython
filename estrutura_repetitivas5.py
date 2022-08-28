# exercício número 5
# estrutura repetitiva
quantidade= int(input(" Digite a quantidade de 10 números:"))
soma=0

for n in range (1, 10+1):
        num= int(input(f" Insira o número {n} / {quantidade} valor:"))
        soma= soma +num
print(f" A soma desses números = {soma}")

