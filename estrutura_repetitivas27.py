
# exercício número 27
# estrutura repetitiva
comprovar=True
while comprovar==True:
    n=int(input(" Digite um número inteiro positivo: "))
    soma_de=0
    soma_ed=0
    if n> 0:
        comprovar=False
        print(" Numero correto ")
        for i in range(1, n + 1):
            soma_ed += 1 / i  # soma da esquerda  para a  direita
            soma_de += 1 / (n + 1 - i)  # somar da direita para a esquerda
        print(f" A soma da serie hamônica da esquerda para a direita: {soma_ed:.2n}")
        print(f" A soma da serie harmônica da direita para esquerda: {soma_de:.2n} ")
    else:
        print(" Este número não está correto. Tente novamente. ")



