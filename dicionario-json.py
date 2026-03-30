import json

def contar_pendentes(tarefas):
    contador = 0
    for tarefa in tarefas:
        if not tarefa.get("concluida"):
            contador += 1
    return contador

        
tarefas = [
    {"nome": "Treinar"},
    {"nome": "Treinar", "concluida": False},
    {"nome": "Ler", "concluida": True}
]
with open("tarefas.json", "w") as arquivo:
    json.dump(tarefas, arquivo, indent=4)
try:
    with open("tarefas.json", "r") as arquivo:
        tarefas = json.load(arquivo)
except FileNotFoundError:
    tarefas = []

print(contar_pendentes(tarefas))