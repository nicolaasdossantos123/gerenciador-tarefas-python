class Tarefa:
    def __init__(self, nome):
        self.nome = nome
        self.concluida = False
        
    def marcar_concluida(self):
        self.concluida = True
        
    def mostrar(self):
        status = "✓" if self.concluida else " "
        print(f"[{status}] {self.nome}")
        
t1 = Tarefa("Varrer")

t1.marcar_concluida()

print(t1.concluida)

t1 = Tarefa("Varrer")

t1.concluida = True

print(t1.concluida)
    
t1.mostrar()