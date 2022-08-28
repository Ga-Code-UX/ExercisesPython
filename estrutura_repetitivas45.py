# exercício número 45
# estrutura repetitiva
opcao=input(" Digite uma das opções que você quer converter (km/h) ou (m/s)?")
while True:
    velocidade=(int(input(" Digite a velocidade: ")))
    finalizar= input(" Digite 0 para finalizar o programa e para converter as unidades:")
    if finalizar == "0":
        break
if opcao=="km/h":
    metros_segundo= velocidade/3.6
    print(f" A velocidade convertidade de km/h para m/s = {metros_segundo:} m/s")
elif opcao == "m/s":
        km_horas= velocidade*3.6
        print(f" A velocidade convertidade de m/s para km/h  = {km_horas:} km/h")

