# Calcule as raízes da equação do 2º grau. Lembrando que:
# x = -b +- raiz de Delta  onde Delta = b**2 - 4ac
# E "ax**2 + bx + c = 0" representa uma equação do 2º grau. A variável "a" tem que ser
# diferente de zero. Caso seja igual imprima a mensagem "não é uma equação do 2 grau".
# Se delta < 0 não existe real, imprima a mensagem " não existe raiz".
# Se delta = 0 existe uma raiz real, imprima a mensagem " existe uma raíz única".
# Se delta >= 0 existe duas raízes reais
import math

print(" Vamos resolver uma equação do 2º grau do tipo  ax² + bx + c ")
a= float(input(" Digite o valor de a : "))
b= float(input(" Digite o valor de b : "))
c= float(input(" Digite o valor de c : "))

delta = (b*b) - (4*a*c)


if a != 0 and delta < 0:
    print(f" Não existe raíz ")
elif a != 0 and delta == 0:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    print(f" Existe uma raíz única, {raiz1:.2f} ")
elif a != 0 and delta > 0:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f" existe duas raízes reais {raiz1:.2f}, e {raiz2:.2f} ")
else:
    print(" Não é uma equação do 2º grau ")






