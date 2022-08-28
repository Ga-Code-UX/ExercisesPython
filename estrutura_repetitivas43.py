# exercício número 43
# estrutura repetitiva
soma= 0
i=0
idade = []
while True:
    idade.append(int(input(" Digite uma idade: ")))
    num = input(" se vc quer continuar digite (S) se não quiser continuar digite 0:")
    if num == "0":
        break
for i in idade:
    soma += i
    media = soma / len(idade)
print(f" A média dessas idades = {media:.2n} ")

