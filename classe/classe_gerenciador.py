class Tarefa:
    def __init__(self, nome):
        self.nome = nome
        self.concluida = False


class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar(self, nome):
        tarefa = Tarefa(nome)
        self.tarefas.append(tarefa)

    def listar(self):
        for i, tarefa in enumerate(self.tarefas):
            status = "✔" if tarefa.concluida else "❌"
            print(f"{i} - {tarefa.nome} [{status}]")

    def concluir(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].concluida = True
        else:
            print("Índice inválido")

    def remover(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas.pop(indice)
        else:
            print("Índice inválido")



g = GerenciadorTarefas()

g.adicionar("Estudar Python")
g.adicionar("Fazer projeto")

g.listar()

g.concluir(0)
g.listar()

g.remover(1)
g.listar()