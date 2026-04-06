tarefas = []
while True:
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Sair")

    opcao = input("Digite a tarefa:")
    if opcao == "1":
        tarefa = input("Digite a tarefa:")

        if tarefa == "":
            print("Tarefa inválida!")
        else:
            tarefa.append(tarefa)
            print("Tarefa adicional!")
