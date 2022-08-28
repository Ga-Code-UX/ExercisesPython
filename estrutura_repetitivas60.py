# exercício número 60
# estrutura repetitiva
comprovar=True
num =[]
lista=(num)
soma = 0
soma_pares=0
cont=0
while comprovar==True:
    num.append(int(input(" Digite um número: ")))
    resp= input(" Digite S para continuar ou 0 para finalizar: ")
    if resp == "0":
        break
for i in num:
    soma += i
    cont = len(lista)
    media = soma/len(lista)
    maior_numero = max(num)
    menor_numero = min(num)
print(f" A soma dos números digitados = {soma}")
print(f" A quantidade de números digitados = {cont}")
print(f" A média dos números digitados = {media}")
print(f" O maior  número digitado = {maior_numero}")
print(f" O menor número digitado = {menor_numero}")
for i in num:
    if i%2==0:
        soma_pares += i
        lista2 = [i]
        media_pares = soma_pares/len(lista2)
print(f" a média dos números pares = {media_pares}")