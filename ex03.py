# autores: Cristiano e Michel
# Data: 06/12/2023
# Descrição: Exercício 04
# Questão: 

# Considere o seguinte cenário: você está organizando uma festa 
# de aniversário e precisa gerenciar a lista de convidados. 
# Crie um programa em Python que permita a entrada de dados
# para adicionar e remover convidados da lista. Ao final, 
# exiba todos os convidados presentes na lista.

# Inicializando a lista de convidados
lista_convidados = []

# Loop principal do programa
while True:
    # Exibindo as opções para o usuário
    print("\n--- Gerenciador de Lista de Convidados ---")
    print("1. Adicionar convidado")
    print("2. Remover convidado")
    print("3. Exibir lista de convidados")
    print("4. Sair")

    # Solicitando a escolha do usuário
    escolha = input("Escolha uma opção (1-4): ")

    # Verificando a escolha do usuário
    if escolha == "1":
        # Adicionar convidado
        convidado = input("Digite o nome do convidado a ser adicionado: ")
        lista_convidados.append(convidado)
        print(f"{convidado} foi adicionado à lista de convidados.")

    elif escolha == "2":
        # Remover convidado
        if len(lista_convidados) == 0:
            print("A lista de convidados está vazia.")
        else:
            print("Lista de Convidados:")
            for i, convidado in enumerate(lista_convidados):
                print(f"{i + 1}. {convidado}")

            indice_remover = int(input("Digite o número do convidado a ser removido: ")) - 1

            if 0 <= indice_remover < len(lista_convidados):
                convidado_removido = lista_convidados.pop(indice_remover)
                print(f"{convidado_removido} foi removido da lista de convidados.")
            else:
                print("Índice inválido. Tente novamente.")

    elif escolha == "3":
        # Exibir lista de convidados
        print("Lista de Convidados:")
        for i, convidado in enumerate(lista_convidados):
            print(f"{i + 1}. {convidado}")

    elif escolha == "4":
        # Sair do programa
        print("Saindo do programa. Obrigado por usar o Gerenciador de Lista de Convidados!")
        break

    else:
        # Opção inválida
        print("Opção inválida. Tente novamente.")
