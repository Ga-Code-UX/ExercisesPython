# exercício número 23
# estrutura repetitiva
n=int(input(" Digite um número: "))
def divisores(n):
    for i in range(1, n//2+1):
        if n % i == 0:
            yield i
    yield n
print(list(divisores(n)))


#for i in range(1,n+1):
   # if n>0 and (n % i) == 0:
        #print (i)
