# Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar.
# As condições para a aposentadoria são: ter pelo menos 65 anos; ter trabalhado
# pelo menos 30 anos; ou ter pelo menos 65 anos e trabalhado pelo menos 25 anos.

idade = float(input(" Digite sua idade: "))
tempo_servico = float(input(" Digite seu tempo de serviço: "))

if (idade >= 65) and (tempo_servico >= 25):
    print(" Você pode se aposentar ")
elif idade >= 65 and tempo_servico >= 30:
    print(" Você pode se aposentar")
else:
    print(" Você ainda não pode se aposentar ")



