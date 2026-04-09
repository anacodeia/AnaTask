from src.app import adicionar_tarefa


def test_adicionar_tarefa_valida():
    lista = []
    resultado = adicionar_tarefa(lista, "Estudar")

    assert resultado == True
    assert lista == ["Estudar"]


def test_adicionar_tarefa_vazia():
    lista = []
    resultado = adicionar_tarefa(lista, "")

    assert resultado == False
    assert lista == []
