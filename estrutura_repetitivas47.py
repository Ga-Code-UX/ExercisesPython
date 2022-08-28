# exercício número 47
# estrutura repetitiva
print(" Escolha umas das opções a segui:")
print(" Adição = (opção 1)       | ", end="")
print(" Subtração = (opção 2) ")
print(" Multiplicação = (opção 3)|", end="")
print(" Divisão = (opção 4)")
print(" Saída = (opção 5)")
opcao=int(input(" Digite a opção(1,2,3,4 ou 5): "))

lista=[]
adicao=0
subtracao=0
multiplicacao=0
divisao=0
while True:
    lista.append(int(input(" Digite o primeiro valor :")))
    finalizar= input(" Voce digitou o primeiro valor, agora para continuar e obter o calculo desejado digite (S):")
    lista.append(int(input(" Digite o segundo valor:")))
    saida = input(" Voce digitou o segundo valor, digite opção 5 para obter o resultado:")
    if saida == "5":
        break
for i in lista:
    if opcao == 1:
        adicao = lista[0]+lista[1]
        print(f" Voce escolheu a opção 1 = adição, o somatório dos dois números digitados = {adicao}")
    if opcao == 2:
        subtracao = lista[0]-lista[1]
        print(f" Voce escolheu a opção 2 = subtração, a subtração dos dois números digitados = {subtracao}")
    if opcao == 3:
        multiplicacao = lista[0]*lista[1]
        print(f" Voce escolheu a opção 3 = multiplicação, a multiplicação dos dois números digitados = {multiplicacao}")
    if opcao == 4:
        divisao = lista[0]/lista[1]
        print(f" Voce escolheu a opção 4 = divisão, a divisão dos dois números digitados = {divisao}")

