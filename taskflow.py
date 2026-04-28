class Tarefa:
    def __init__(self, id, titulo, descricao, prioridade):
        self.__id = id
        self.titulo = titulo
        self.descricao = descricao
        self.__prioridade = prioridade
        self.__status = "Pendente"

    @property
    def id(self): return self.__id

    @property
    def status(self): return self.__status

    @property
    def prioridade(self): return self.__prioridade

    def concluir(self):
        self.__status = "Concluída"

    def exibir_dados(self):
        return f"ID: {self.__id} | {self.titulo} - Status: {self.__status} | Prioridade: {self.__prioridade}"

class TarefaPessoal(Tarefa):
    def __init__(self, id, titulo, descricao, prioridade, categoria):
        super().__init__(id, titulo, descricao, prioridade)
        self.categoria_pessoal = categoria

    def exibir_dados(self):
        return super().exibir_dados() + f" | Categoria: {self.categoria_pessoal}"

class TarefaProfissional(Tarefa):
    def __init__(self, id, titulo, descricao, prioridade, area):
        super().__init__(id, titulo, descricao, prioridade)
        self.area_responsavel = area

    def exibir_dados(self):
        return super().exibir_dados() + f" | Área: {self.area_responsavel}"

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

def executar_sistema():
    gerenciador = GerenciadorTarefas()
    contador_id = 1

    while True:
        print("\n--- MENU TASKFLOW ---")
        print("1. Cadastrar Tarefa")
        print("2. Listar Tarefas")
        print("3. Concluir Tarefa")
        print("4. Excluir Tarefa")
        print("5. Sair")
        
        opcao = input("Escolha: ")

        if opcao == "1":
            print("\n1. Pessoal | 2. Profissional")
            tipo = input("Tipo: ")
            titulo = input("Título: ")
            desc = input("Descrição: ")
            prio = input("Prioridade: ")

            if tipo == "1":
                cat = input("Categoria: ")
                nova = TarefaPessoal(contador_id, titulo, desc, prio, cat)
            else:
                area = input("Área Responsável: ")
                nova = TarefaProfissional(contador_id, titulo, desc, prio, area)
            
            gerenciador.adicionar_tarefa(nova)
            contador_id += 1
            print("Sucesso!")

        elif opcao == "2":
            for t in gerenciador.listar_tarefas():
                print(t.exibir_dados())

        elif opcao == "3":
            try:
                id_sel = int(input("ID da tarefa: "))
                encontrada = False
                for t in gerenciador.listar_tarefas():
                    if t.id == id_sel:
                        t.concluir()
                        print("Tarefa concluída!")
                        encontrada = True
                if not encontrada: print("Não encontrada.")
            except: print("ID inválido.")

        elif opcao == "4":
            try:
                id_rem = int(input("ID para remover: "))
                if gerenciador.remover_tarefa(id_rem):
                    print("Removida.")
                else:
                    print("Não encontrada.")
            except: print("ID inválido.")

        elif opcao == "5":
            break

if __name__ == "__main__":
    executar_sistema()