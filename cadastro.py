# Programa simples de cadastro, alteração, exclusão, consulta e listagem de dados
# Dicionário para armazenar os dados
dados = {}

def incluir_dado():
    chave = input("Digite a chave para o novo dado: ")
    if chave in dados:
        print("Essa chave já existe. Deseja sobrescrever? (s/n)")
        resposta = input().lower()
        if resposta != "s":
            print("Inclusão cancelada.")
            return
    valor = input("Digite o valor para o novo dado: ")
    dados[chave] = valor
    print("Dado incluído com sucesso!")

def alterar_dado():
    chave = input("Digite a chave do dado que deseja alterar: ")
    if chave in dados:
        novo_valor = input("Digite o novo valor para o dado: ")
        dados[chave] = novo_valor
        print("Dado alterado com sucesso!")
    else:
        print("Dado não encontrado.")

def excluir_dado():
    chave = input("Digite a chave do dado que deseja excluir: ")
    if chave in dados:
        del dados[chave]
        print("Dado excluído com sucesso!")
    else:
        print("Dado não encontrado.")

def consultar_dado():
    chave = input("Digite a chave do dado que deseja consultar: ")
    if chave in dados:
        print(f"Valor do dado: {dados[chave]}")
    else:
        print("Dado não encontrado.")

def listar_dados():
    if dados:
        print("\n--- Lista de todos os dados cadastrados ---")
        for chave, valor in dados.items():
            print(f"{chave}: {valor}")
    else:
        print("Nenhum dado cadastrado.")

# Menu principal do programa
while True:
    print("\nMenu:")
    print("1 - Incluir dado")
    print("2 - Alterar dado")
    print("3 - Excluir dado")
    print("4 - Consultar dado")
    print("5 - Listar todos os dados")
    print("6 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        incluir_dado()
    elif opcao == "2":
        alterar_dado()
    elif opcao == "3":
        excluir_dado()
    elif opcao == "4":
        consultar_dado()
    elif opcao == "5":
        listar_dados()
    elif opcao == "6":
        print("Encerrando o programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
