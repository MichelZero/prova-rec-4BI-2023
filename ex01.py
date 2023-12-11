# autores: Cristiano e Michel
# Data: 06/12/2023
# Descrição: Exercício 02
# Questão: 


# Dada uma tupla de nomes de alunos e suas respectivas notas, 
# escreva um programa que converta a tupla em dicionário, imprima o
# nome do aluno com a # maior nota e o nome do aluno com a menor nota.
alunos = (("João", 8.5), ("Maria", 9.2), ("José", 7.1), ("Ana", 8.7), ("Carlos", 6.5))

dicionario = dict(alunos) # conversão da tupla para dicionário
print(dicionario)

maior_nota = max(dicionario.values()) # maior nota
menor_nota = min(dicionario.values()) # menor nota

for nome, nota in dicionario.items():
  if nota == maior_nota:
    print(f"Aluno com a maior nota: {nome}")
  elif nota == menor_nota:
    print(f"Aluno com a menor nota: {nome}")
    

maior_nota = max(dicionario) # maior nota
menor_nota = min(dicionario) # menor nota 

print(f"Aluno com a maior nota: {maior_nota}")
print(f"Aluno com a menor nota: {menor_nota}")  