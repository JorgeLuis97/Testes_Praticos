Agenda = {
    "LETICIA": "85 99999-9998",
    "MATHEUS": "88 98989-3333"
}


def adicionarcontato(nome, telefone):
    Agenda[nome] = telefone
    print("Contato Adicionado com sucesso!")


def editarcontato(nome, telefone):
    if nome in Agenda:
        Agenda[nome] = telefone
        print("Contato alterado com sucesso!\n")
        print("     Lista de Contatos     ")
        for i in Agenda:
            print("----------------")
            print(f"Nome:{i} \n"
                  f"Telefone: {Agenda[i]}")
            print("----------------")
        print("                           ")
    else:
        print("Contato não Encontrado!")


# def editarcontato1():


def buscarcontato(nome):
    if nome in Agenda:
        print(f"Nome: {nome} \n"
              f"Telefone: {Agenda[nome]} \n")


def deletarcontato(nome):
    if nome in Agenda:
        del Agenda[nome]
        print("     Lista de Contatos     ")
        for i in Agenda:
            print("----------------")
            print(f"Nome:{i} \n"
                  f"Telefone: {Agenda[i]}")
            print("----------------\n")
        print("                           ")


def listarcontato():
    print("     Lista de Contatos     ")
    for i in Agenda:
        print("----------------")
        print(f"Nome:{i} \n"
              f"Telefone: {Agenda[i]}")
        print("----------------\n")
    print("                           ")


while True:
    print("-----Agenda Telefonica----")
    opcao = int(input("1 - Adicionar Contato \n"
                      "2 - Editar Contato \n"
                      "3 - Buscar Contato \n"
                      "4 - Deletar Contato \n"
                      "5 - Listar Todos \n"
                      "6 - Sair \n"
                      "Selecione uma opção: "))
    print("")
    if opcao == 1:
        Nome = input("Nome do contato: ").upper()
        Telefone = input("Ex. 85 99999-9999 \n"
                         "Número de Contato: ")
        adicionarcontato(Nome, Telefone)
        print("     Lista de Contatos     ")
        for i in Agenda:
            print("----------------")
            print(f"Nome:{i} \n"
                  f"Telefone: {Agenda[i]}")
            print("----------------")
        print("                           ")

    elif opcao == 2:
        print("     Lista de Contatos     ")
        for i in Agenda:
            print("----------------")
            print(f"Nome:{i} \n"
                  f"Telefone: {Agenda[i]}")
            print("----------------\n")
        print("                           ")
        print("     Alteração de contato     ")
        opcaoedit = int(input("1 - Somente o nome \n"
                              "2 - Somente o Número \n"
                              "3 - Nome e Número"))
        if opcaoedit == 1:
            Nome = input("Nome do contato: ").upper()

        Nome = input("Nome do contato: ").upper()
        Telefone = input("Ex. 85 99999-9999 \n"
                         "Número de Contato: ")
        print("                              ")
        editarcontato(Nome, Telefone)

    elif opcao == 3:
        print("     Alteração de contato     ")
        print("")
        Nome = input("Nome do contato: ").upper()
        print("")
        print("                              ")
        buscarcontato(Nome)

    elif opcao == 4:
        Nome = input("Nome do contato: ").upper()
        deletarcontato(Nome)

    elif opcao == 5:
        listarcontato()

    elif opcao == 6:
        print("Saindo...")
        break
    else:
        print("!!!!!!!!!!!!!!!")
        print("Opção Invalida!")
        print("!!!!!!!!!!!!!!! \n")
