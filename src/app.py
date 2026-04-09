def adicionar_tarefa(lista, tarefa):
    if tarefa == "":
        return False
    lista.append(tarefa)
    return True


tarefas = []

while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Sair")

    opcao = input("Digite a opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")

        if adicionar_tarefa(tarefas, tarefa):
            print("Tarefa adicionada!")
        else:
            print("Tarefa inválida!")

    elif opcao == "2":
        print("\nLista de tarefas:")
        for t in tarefas:
            print("-", t)

    elif opcao == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
