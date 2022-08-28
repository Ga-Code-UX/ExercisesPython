# exercício número 29
# estrutura repetitiva
n=5
S=0
def calcularFat(n):
    resultado = 1
    for n in range(1, n + 1):
        resultado *= n
    return resultado
if n> 0:
    for i in range(1, n):
        S += i/calcularFat(i*2)
    print(S)


