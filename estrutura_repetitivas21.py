# exercício número 21
# estrutura repetitiva
a= int(input(" Digite um número:"))
b= int(input(" Digite um número:"))

soma=0
soma_par=0
num= [a,b]
lista = list(num)


for i in range(a,b+1):
    for i in lista:
         if (i %2 ==0 ):
             soma_par += i
             soma = soma_par + a + b
         else:
             produto *= i
             produto= produto * a*b
print(f" A soma dos números pares do intervalo de {a} e {b} e os números digitados = {soma}")
print(f' O produto dos números impares do intervalo de {a} e {b} e os números digitados ={produto}')



