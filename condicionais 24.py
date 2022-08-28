# Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui
# uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RG 15% e MS 8%). Faça
# um programa em que o usuário entre com o valor e o estado destino do produto
# e o programa retorne o preço final acrescido do imposto do estado em que ele
# será vendido. Se o estado digitado não for válido, mostrar uma mensagem de erro.


valor_produto = float(input(" Digite o valor do produto: "))
estado = input(" Digite o Estado destino do produto ( MG,SP,RG ou MS): ")


if estado == "MG":
    produto1 = valor_produto + (valor_produto * 7)/100
    print(f" Preço final do produto = {produto1:.2f} ")
elif estado == "SP":
    produto2 = valor_produto + (valor_produto*12)/100
    print(f" Preço final do produto = {produto2:.2f} ")
elif estado == "RG":
    produto3 = valor_produto + (valor_produto*15)/100
    print(f"Preço final do produto = {produto3:.2f} ")
elif estado == "MS":
    produto4 = valor_produto + (valor_produto*8) /100
    print(f"Preço final do produto = {produto4:.2f} ")
else:
    print(" ERRO. Esse estado não está na lista de cálculo ")




