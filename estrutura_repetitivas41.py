# exercício número 41
# estrutura repetitiva

while True:
    R1= int(input(" Digite o valor do primeiro resistor:"))
    R2= int(input(" Digite o valor do segundo resistor:"))
    R = R1 * R2 / (R1 + R2)
    if R == 0:
        print(f"O programa parou porque o valor da resistência = {R:.3n}")
        break

    else:
        print(f" O valor da resistência = {R:.3n}")
