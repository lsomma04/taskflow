class Tarefa:
    def __init__(self, id, titulo, descricao, prioridade):
        self.__id = id
        self.titulo = titulo
        self.descricao = descricao
        self.__prioridade = prioridade
        self.__status = "Pendente"

    @property
    def id(self):
        return self.__id

    @property
    def status(self):
        return self.__status

    @property
    def prioridade(self):
        return self.__prioridade

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