# exercício número 57
# estrutura repetitiva


cont=0
a = int(input(" Digite o primeiro número: "))
b = int(input(" Digite o segundo número: "))
if b<a:
        a, b = b, a
for i in range(a, b+1):
    if i %2 !=0:
        lista = [i]
        cont= cont+ len(lista)
        print(lista,end="")
print(f" . A quantidade total de números impares de {a} ate {b} = {cont} elementos")