tarefas = []

while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Sair")

    opcao = input("Digite a opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")

        if tarefa == "":
            print("Tarefa inválida!")
        else:
            tarefas.append(tarefa)
            print("Tarefa adicionada!")

    elif opcao == "2":
        print("\nLista de tarefas:")
        for t in tarefas:
            print("-", t)

    elif opcao == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
