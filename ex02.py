# autores: Cristiano e Michel
# Data: 06/12/2023
# Descrição: Exercício 02
# Questão: 

# Em linguagem Python, faça um programa que leia 6 valores e os 
# armazene em uma lista, imprima a lista e mostre o menor elemento 
# e a posição que ele se encontra.

lista = [] # lista vazia

for i in range(6):
  valor = int(input("Digite um valor: "))
  lista.append(valor)
  
print(f"Lista: {lista}")
print(f"Menor elemento: {min(lista)}")
print(f"Posição do menor elemento: {lista.index(min(lista))}")


