# exercício número 8
# estrutura repetitiva
a = int(input(" Digite o primeiro número:"))
b = int(input(" Digite o segundo número:"))
c = int(input(" Digite o terceiro número:"))
d = int(input(" Digite o quarto número:"))
e = int(input(" Digite o quinto número:"))
f = int(input(" Digite o sexto número:"))
g = int(input(" Digite o sétimo número:"))
h = int(input(" Digite o oitavo número:"))
i = int(input(" Digite o nono número:"))
j = int(input(" Digite o décimo número:"))
min_value = 10
max_value = 10
list=[a,b,c,d,e,f,g,h,i,j]
for num in list:
        if (max_value == 10 or num > max_value):
                 max_value = num
print('Maximum value:', max_value)
for num1 in list:
        if(min_value == 10 or num1 < min_value):
         min_value = num1
print('Mínimo value:', min_value)









