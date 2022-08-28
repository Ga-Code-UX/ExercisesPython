# exercício número 24
# estrutura repetitiva
n=int(input(" Digite um número: "))
soma=0
def divisores(n):
    for i in range(1, n//2+1):
        if n % i == 0:
            yield i
    yield n
lista=list(divisores(n))
print(f" Os divisores de {n} são:{lista}")
for i in lista:
    soma += i
print(f" A soma dos divisores de {n} são:",soma)