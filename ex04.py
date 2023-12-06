# autores: Cristiano e Michel
# Data: 06/12/2023
# Descrição: Exercício 04
# Questão: 

# Crie uma lista de compras de supermercado utilizando um 
# dicionário. A entrada dos produtos será realizada por 
# meio de uma estrutura de repetição. Além disso, você 
# deverá calcular a média dos preços dos produtos. O usuário
# deve informar a quantidade de produtos que deseja inserir.

# Para completar este exercício, você deve criar um programa 
# que permita ao usuário inserir produtos e seus respectivos 
# preços em um dicionário. Utilize uma estrutura de repetição 
# para facilitar a entrada de múltiplos produtos. 
# Ao final, calcule a média dos preços dos produtos inseridos.


produtos = {}
total_precos = 0
quantidade_produtos = int(input("Quantidade de produtos: "))

for i in range(quantidade_produtos):
  nome_produto = input("Nome do produto: ")
  preco_produto = float(input("Preço do produto: "))
  produtos[nome_produto] = preco_produto
  total_precos += preco_produto

media_precos = total_precos / quantidade_produtos

print("Produtos:", produtos)
print("Média dos preços:", media_precos)
