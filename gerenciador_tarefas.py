class GerenciadorTarefas:
    def __init__(self):
        self.lista_tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.lista_tarefas.append(tarefa)

    def listar_tarefas(self):
        return self.lista_tarefas

    def remover_tarefa(self, id_tarefa):
        for t in self.lista_tarefas:
            if t.id == id_tarefa:
                self.lista_tarefas.remove(t)
                return True
        return False