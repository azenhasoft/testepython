# Programa simples de cadastro, alteração, exclusão e consulta de dados

# Dicionário para armazenar os dados (poderia ser um banco de dados real)
dados = {}

def incluir_dado():
    # Função para incluir um novo dado
    chave = input("Digite a chave para o novo dado: ")
    valor = input("Digite o valor para o novo dado: ")
    dados[chave] = valor
    print("Dado incluído com sucesso!")

def alterar_dado():
    # Função para alterar um dado existente
    chave = input("Digite a chave do dado que deseja alterar: ")
    if chave in dados:
        novo_valor = input("Digite o novo valor para o dado: ")
        dados[chave] = novo_valor
        print("Dado alterado com sucesso!")
    else:
        print("Dado não encontrado.")

def excluir_dado():
    # Função para excluir um dado existente
    chave = input("Digite a chave do dado que deseja excluir: ")
    if chave in dados:
        del dados[chave]
        print("Dado excluído com sucesso!")
    else:
        print("Dado não encontrado.")

def consultar_dado():
    # Função para consultar um dado existente
    chave = input("Digite a chave do dado que deseja consultar: ")
    if chave in dados:
        print("Valor do dado:", dados[chave])
    else:
        print("Dado não encontrado.")

# Menu principal do programa
while True:
    print("\nMenu:")
    print("1 - Incluir dado")
    print("2 - Alterar dado")
    print("3 - Excluir dado")
    print("4 - Consultar dado")
    print("5 - Sair")

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
        break
    else:
        print("Opção inválida.")
