# Exercício 32 da secção 5
import math
print(" Código")
print(" Cachorro quente = 100",end= " | ")
print("   Bauru simples = 101 ")
print(" Bauru com ovo = 102", end="   | ")
print("   Hamburguer = 103")
print(" Cheesebuguer = 104", end="    | " )
print("   Suco = 105")
print(" refrigerante = 106")
print()

codigo_cachorro_quente= float(input(" Digite o código do cachorro quente: "))
quantidade1 = float(input(" Digite a quantidade do cachorro quente: "))
codigo_bauru_simples = float(input(" Digite o código do bauru simples: "))
quantidade2 = float(input(" Digite a quantidade do bauru simples: "))
codigo_bauru_ovo= float(input(" Digite o código do bauru com ovo: "))
quantidade3 = float(input(" Digite a quantidadedo bauru com ovo: "))
codigo_hamburguer = float(input(" Digite o código do hamburguer: "))
quantidade4 = float(input(" Digite a quantidade do hamburguer: "))
codigo_cheeseburguer = float(input(" Digite o código do cheesebuguer: "))
quantidade5 = float(input(" Digite a quantidade do cheesebuguer: "))
codigo_suco = float(input(" Digite o código do suco: "))
quantidade6 = float(input(" Digite a quantidade do suco: "))
codigo_refrigerante = float(input(" Digite o código do refrigerante : "))
quantidade7 = float(input(" Digite a quantidade do refrigerante : "))

soma = 0

if codigo_cachorro_quente == 100 and codigo_bauru_simples == 101 and codigo_bauru_ovo == 102 and codigo_hamburguer == 103 and codigo_cheeseburguer == 104 and codigo_suco == 105 and codigo_refrigerante == 106:
    soma = soma + (1.2*quantidade1) + (1.3*quantidade2) + (1.50*quantidade3) + (1.20*quantidade4)+(1.7*quantidade5)+(2.20*quantidade6)+(1*quantidade7)
    print(f" Total = {soma} euros ")
else:
    print(soma)



