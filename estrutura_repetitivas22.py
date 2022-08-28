# exercício número 22
# estrutura repetitiva
n=[]
soma= 0
i=0
while True:
    n.append(int(input(" Digite uma nota: ")))
    num= input(" Vc quer continuar digite (S/N):")
    if (num == "N" ):
        break
    if i <= 10 and i >= 20:
        print(" Digite valores válidos entre 10 a 20 ")
for i in n:
    soma+=i
    media= soma / len(n)
print(f" Sua média aritimética = {media:.2n} ")





