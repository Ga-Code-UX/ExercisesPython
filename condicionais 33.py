# Exercício 33 da secção 5
import math

preco_antigo= float(input(" Digite o preço antigo do produto: "))


if preco_antigo < 50:
    preco_novo = preco_antigo + preco_antigo * (5/100)
    if preco_novo <= 80:
        print(" Barato")
elif preco_antigo > 50 and preco_antigo < 100:
    preco_novo1 = preco_antigo + preco_antigo * (10/100)
    if preco_novo1 >= 80 and preco_novo1 <= 120:
        print(" Normal ")
elif preco_antigo > 100:
    preco_novo3 = preco_antigo + (preco_antigo * (15/100))
    if preco_novo3 >= 120 and preco_novo3 <= 200:
        print(" Caro ")
    else:
        print(" Muito Caro ")
else:
    print(preco_antigo)