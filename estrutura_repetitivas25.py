# exercício número 25
# estrutura repetitiva

soma=0
soma2=0

for i in range(1,9):
        resto = i % 10
        i = (i - resto) // 10
        soma = soma + resto
        soma=soma
        print(soma)
        if (soma1%3==0):
            lista=[soma1]
            print(lista)
            list2=(lista)
            for x in list2:
                    soma2+=x
print(f"A soma dos números múltiplos de 3  são: {soma2}")
