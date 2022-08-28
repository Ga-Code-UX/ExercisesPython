# Dados três valores,A,B e C verificar se eles podem ser valores dos lados de um triângulo
# e, se forem,se é um triângulo escaleno, equilátero ou isósceles, considerando os seguintes
# conceitos:
# 1- O comprimento de cada lado de um triângulo é menor do que  a soma dos outros dois lados;
# 2- Chama-se equilátero o triângulo que tem 3 lados iguais;
# 3- Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais;
# 4- Recebe o nome de escaleno o triângulo que tem os três lados diferentes;

A = float(input(" Digite valor do lado A: "))
B = float(input(" Digite valor do lado B: "))
C = float(input(" Digite valor do lado C: "))

if (A < B+C) and ( B < A+C) and (C <A+B):
    if (A == B == C):
        print (" Esse triângulo é equilátero ")
    elif ((A == B and C != A ) or (A == C and B != C) or (B == C and B != A)):
        print (" Esse triângulo é isoscele ")
    else:
        print(" Esse triângulo é escaleno ")
else:
    print(" Esses valores não são válidos porque cada lado de um triângulo "
          " deve ser menor do que  a soma dos outros dois lados")