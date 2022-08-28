# exercício número 19
# estrutura repetitiva
num = int(input("Informe um número entre 100 e 999:"))
unidade = num//1%10
dezena = num//10%10
centena =num//100%10
milhar = num//1000%10
if num>100 and num < 999:
        print("Analisando o número {}".format(num))
        print("Unidade:{}".format(unidade))
        print("Dezena:{}".format(dezena))
        print("Centena:{}".format(centena))
        print("Milhar:{}".format(milhar))