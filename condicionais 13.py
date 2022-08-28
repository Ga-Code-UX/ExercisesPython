# Faça um algoritmo que calcule  a media ponderada das notas de 3 provas. A primeira e segunda
# prova tem peso 1 e a terceira prova tem peso 2. Ao final, mostrar a média do aluno e indicar se
# o aluno foi aprovado ou reprovado. A nota para aprovação dever ser igual ou superior a 60 pontos.

nota1 = float(input(" Digite a primeira nota = "))
nota2 = float(input(" Digite a segunda nota = "))
nota3 = float(input(" Digite a terceira nota = "))

peso1 = 1
peso2 = 2
media_ponderada = ((peso1 * nota1) + (peso1 * nota2) + (peso2 * nota3)) // (peso1 + peso1 + peso2)
if (media_ponderada >= 60):
    print(f" Média Ponderada = {media_ponderada:.2f} ")
    print(f" Aluno aprovado ")
else:
    print(f" Média Ponderada = {media_ponderada:.2f} ")
    print( " Aluno Reprovado")




