# exercício número 28
# estrutura repetitiva
comprovar=True
while comprovar==True:
    n=int(input(" Digite um número inteiro positivo: "))
    E=1
    def calcularFat(n):
        resultado=1
        for n in range(1,n+1):
            resultado *= n
        return  resultado
    if n> 0:
        comprovar=False
        print(" Numero correto ")
        for i in range(1, n + 1):
            E += 1 / calcularFat(i) # soma da esquerda  para a  direita
        print(f" A soma da serie hamônica da esquerda para a direita: {E:.2n}")
    else:
        print(" Este número não está correto. Tente novamente. ")

