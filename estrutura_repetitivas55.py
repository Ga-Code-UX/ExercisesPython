# exercício número 55
# estrutura repetitiva
comprovar=True
x=[]
soma_impares = 0
while comprovar==True:
    x = int(input(" Digite um número: "))
    if x > 0:
        comprovar=False
        print(" Numero correto ")
    else:
        print(" Digite um número maior que zero. Tente novamente. ")
for i in range(1, x+1):
    if i %2 !=0:
        lista = [i]
        soma_impares += i
        print(lista,end="")
print(f" . A soma do númeor impares de 1 ate {x} = {soma_impares}")