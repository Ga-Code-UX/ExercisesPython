# exercício número 39
# estrutura repetitiva
base = int(input(" Digite a base do triângulo: "))
altura = int(input(" Digite a altura do triângulo: "))

if (base>0) and (altura>0):
    area = (base * altura) / 2
    print(f" A área do triãngulo = {area}")
else:
    print(" Dados inválidos. Tente novamente ")