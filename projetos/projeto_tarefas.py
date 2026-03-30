import json

def salvar_tarefas(tarefas):
    with open("tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo, indent=4)

def carregar_tarefas():
    try:
        with open("tarefas.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

tarefas = carregar_tarefas()

def adicionar_tarefa(tarefas):
    nome = input("Digite a tarefa: ")

    if nome.strip() == "":
        print("Tarefa não pode ser salva")
        return

    tarefa = {
        "nome": nome,
        "concluida": False
    }

    tarefas.append(tarefa)
    salvar_tarefas(tarefas)

    print("Tarefa adicionada!")

def mostrar_tarefas(tarefas):
    if len(tarefas) == 0:
        print("Nenhuma tarefa.")
        return

    for i, tarefa in enumerate(tarefas):
        status = "✓" if tarefa["concluida"] else " "
        print(f"{i+1} - [{status}] {tarefa['nome']}")

def concluir_tarefa(tarefas):
    mostrar_tarefas(tarefas)

    try:
        numero = int(input("Qual tarefa foi concluída? "))
        indice = numero - 1

        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = True
            salvar_tarefas(tarefas)
            print("Tarefa concluída!")
        else:
            print("Número inválido.")

    except ValueError:
        print("Digite apenas números.")

def remover_tarefa(tarefas):
    mostrar_tarefas(tarefas)

    try:
        numero = int(input("Qual tarefa deseja remover? "))
        indice = numero - 1

        if 0 <= indice < len(tarefas):
            tarefas.pop(indice)
            salvar_tarefas(tarefas)
            print("Tarefa removida!")
        else:
            print("Número inválido.")

    except ValueError:
        print("Digite apenas números.")


while True:
    try:
        print("\nGERENCIADOR DE TAREFAS")
        print("1 - Adicionar tarefa")
        print("2 - Ver tarefas")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("0 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            adicionar_tarefa(tarefas)

        elif opcao == 2:
            mostrar_tarefas(tarefas)

        elif opcao == 3:
            concluir_tarefa(tarefas)

        elif opcao == 4:
            remover_tarefa(tarefas)

        elif opcao == 0:
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

    except ValueError:
        print("Digite apenas números.")