aprendizado

# 📘 Meu Aprendizado em Python

## 🧠 Conceitos Fundamentais

### 🔹 Funções (`def`)
- Uma função serve para organizar o código
- Regra principal:
  
  **1 função = 1 responsabilidade**

Exemplo:
```python
def saudacao():
    print("Olá!")
🔹 Estrutura de uma função
def nome_funcao():
    # código
    return resultado
🔹 Função principal (main)
Controla o fluxo do programa
def main():
    while True:
        jogar()

if __name__ == "__main__":
    main()
🔥 Organização com Funções
Função	Responsabilidade
escolher_dificuldade	entrada do usuário
obter_chute	entrada segura
jogar	lógica do sistema
menu	controle do usuário
main	fluxo principal
⚠️ Indentação (MUITO IMPORTANTE)
Python usa espaços para definir blocos
✅ Correto:
def teste():
    print("ok")
❌ Errado:
def teste():
print("ok")

Erro:

IndentationError
🔹 Try / Except

Usado para evitar erros:

try:
    numero = int(input("Digite: "))
except ValueError:
    print("Erro!")
🔹 Tipos de erro comuns
ValueError → valor inválido
IndexError → índice fora da lista
FileNotFoundError → arquivo não encontrado
📂 JSON (Salvar dados)

Salvar:

import json

with open("arquivo.json", "w") as f:
    json.dump(dados, f)

Carregar:

with open("arquivo.json", "r") as f:
    dados = json.load(f)
🧱 Classes (POO)
🔹 Exemplo básico
class Tarefa:
    def __init__(self, nome):
        self.nome = nome
        self.concluida = False
🔹 self
Representa o próprio objeto
t1 = Tarefa("Estudar")
print(t1.nome)
🔹 Métodos
def marcar_concluida(self):
    self.concluida = True

Uso:

t1.marcar_concluida()
🔄 Diferença importante
❌ Dicionário
tarefa["nome"]
✅ Classe
tarefa.nome
🚀 Boas práticas
usar funções para organizar
tratar erros com try/except
evitar código repetido
usar nomes claros
dividir o código em partes
🎯 O que já sei fazer

✔ Criar sistemas com input
✔ Usar listas e dicionários
✔ Salvar dados em JSON
✔ Tratar erros
✔ Criar funções organizadas
✔ Criar classes e métodos
✔ Refatorar código

🚀 Próximos passos
aplicar classes no projeto de tarefas
criar projetos maiores
melhorar organização do código
aprender interfaces (web ou GUI)