# Exercício 28 da secção 5
print(" 1 pergunta: ")
a = int(input(" Digite um número: "))
b = int(input(" Digite um número: "))

if (a >= 1 and a <= 100) and (b >=1 and b <= 100):
   y = int(input(" A soma desses números = "))
   while a + b == y:
         print(" Voce acertou ")
         print(" 2 pergunta: ")
         a = int(input(" Digite um número: "))
         b = int(input(" Digite um número: "))
         y = int(input(" A soma desses números ="))

         print(" 3 pergunta: ")
         a = int(input(" Digite um número: "))
         b = int(input(" Digite um número: "))
         y = int(input(" A soma desses números ="))

         print(" 4 pergunta: ")
         a = int(input(" Digite um número: "))
         b = int(input(" Digite um número: "))
         y = int(input(" A soma desses números ="))

         print(" 5 pergunta: ")
         a = int(input(" Digite um número: "))
         b = int(input(" Digite um número: "))
         y = int(input(" A soma desses números ="))

   else:
         print(f" A resposta é {a+b == y} ")
         print(" Voce errou essa pergunta! ")
else:
    print(" Digite um número inteiro positivo entre 1 a 100  ")





