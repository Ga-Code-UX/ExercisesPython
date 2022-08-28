# A nota final de um aluno é calculada a parti de 3 notas atribuídas entre um intervalo de 0 a 10
# respectivamente, a um trabalho de laboratório, a uma avaliação semestral  e a um exame final.
# A média da 3 notas mencionadas anteriormente obdece aos pesos: trabalho de laboratório = 2;
# avaliação semestral = 3; exame final = 5. De acordo com o resultado mostre na tela se
# o aluno está reprovado ( media entre 0 e 2.9) de recuperação ( media entre 3 e 4.9) ou se foi
# aprovado. Faça todas as sverificações necessárias.

nota1 = float(input(" Digite a primeira nota = "))
nota2 = float(input(" Digite a segunda nota = "))
nota3 = float(input(" Digite a terceira nota = "))

peso1 = 2
peso2 = 3
peso3 = 5
media_ponderada = ((peso1 * nota1) + (peso2 * nota2) + (peso3 * nota3)) // (peso1 + peso2 + peso3)
if (media_ponderada >= 0) and (media_ponderada <= 2.9):
    print(f" Média Ponderada = {media_ponderada:.2f} ")
    print(f" O aluno está reprovado ")
elif (media_ponderada >= 3) and (media_ponderada <= 4.9):
    print(f" Média Ponderada = {media_ponderada:.2f} ")
    print( " O aluno está de recuperação ")
else:
    print(f" Média Ponderada = {media_ponderada:.2f} ")
    print("O aluno está aprovado " )




