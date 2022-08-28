# exercício número 20
# estrutura repetitiva
n=[]
list=(n)
cont = 0
conta_par = 0
conta_impar = 0
i=0
while True:
    n.append(int(input(" Digite um num da seq: ")))
    num= input(" Vc quer continuar digite (S) ou para digite (1000):")
    if  num == "1000":
         break
print(f"Você digitou {len(n)} elementos {list}")
for i in list:
    if i%2==0:
        cont = cont + 1
        conta_par = conta_par +1
    else:
        conta_impar = conta_impar + 1
print(f"{conta_par} numeroS pares")
print(f"{conta_impar} numeroS impares")
