# Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto
# se for divisível por 400 ou se for divisível por 4 e não for divisível por 100.
# Por exemplo: 1988,1992 e 1996.

ano = int(input(" Digite o ano: "))


if (ano % 400 == 0):
    print(" Este ano é bissexto ")
elif (ano % 4 == 0) and (ano % 100 != 0):
    print(" Este ano é bissexto ")
else:
    print(" Este ano não é bissexto ")




