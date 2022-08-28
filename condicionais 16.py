# Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:
# A = (( basemaior + basemenor) * altura) / 2. Lembre-se a base maior e a base menor
# devem ser números maiores que zero.

base_maior = float(input(" Digite a base maior do trapzio: "))
base_menor = float (input(" Digite a base menor do trapézio: "))
altura = float(input(" Digite a altura: "))

area = (( base_maior + base_maior) * altura )/ 2

if (base_maior > 0) and (base_menor > 0):
   print(f" Área do trapézio = {area:.2f} metros ao quadrado ")
else:
    print(" Base maior e base menor tem que ser números maiores que zero ")




