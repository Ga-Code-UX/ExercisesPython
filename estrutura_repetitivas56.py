# exercício número 56
# estrutura repetitiva
comprovar=True
soma_impares = 0
while comprovar==True:
    n = 2000000
    if n > 0:
        comprovar=False
        print(" Numero correto ")
    else:
        print(" Digite um número maior que zero. Tente novamente. ")
for i in range(1, n+1):
    if i %2 !=0:
        lista = [i]
        soma_impares += i
        print(lista,end="")
print(f" . A soma do impares de 1 ate {n} = {soma_impares}")