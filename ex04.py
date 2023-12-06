# autores: Cristiano e Michel
# Data: 06/12/2023
# Descrição: Exercício 04
# Questão: Faça uma lista de compras de supermercado utilizando um dicionário.
# A entrada dos produtos deve ser feita através de uma estrutura de repetição.
# Calcule a média dos preços dos produtos.

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
