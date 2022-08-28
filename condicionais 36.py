# Exercício 36 da secção 5
import math

venda_mensal = float(input(" Digite a venda mensal: "))


if venda_mensal >= 100000.00:
    comissao = 700 + (venda_mensal * (16/100))
    print(f" O vendedor recebe de comissão, {comissao:.2f}")
elif venda_mensal>= 80000.00 and venda_mensal< 100000.00:
    comissao1 = 650 + (venda_mensal * (14/100))
    print(f" O vendedor recebe de comissão, {comissao1:.2f}")
elif venda_mensal >= 60000.00 and venda_mensal < 80000.00:
    comissao2 = 600 + (venda_mensal * (14 / 100))
    print(f" O vendedor recebe de comissão, {comissao2:.2f}")
elif venda_mensal >= 40000.00 and venda_mensal < 60000.00:
    comissao3 = 550 + (venda_mensal * (14 / 100))
    print(f" O vendedor recebe de comissão, {comissao3:.2f}")
elif venda_mensal >= 20000.00 and venda_mensal < 40000.00:
    comissao4 = 500 + (venda_mensal * (14 / 100))
    print(f" O vendedor recebe de comissão, {comissao4:.2f}")
elif venda_mensal < 20000.00:
    comissao5 = 400 + (venda_mensal * (14 / 100))
    print(f" O vendedor recebe de comissão, {comissao5:.2f}")
else:
    print(venda_mensal)


