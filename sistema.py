from tarefa import TarefaPessoal, TarefaProfissional
from gerenciador_tarefas import GerenciadorTarefas


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

                if not encontrada:
                    print("Não encontrada.")

            except:
                print("ID inválido.")

        elif opcao == "4":
            try:
                id_rem = int(input("ID para remover: "))

                if gerenciador.remover_tarefa(id_rem):
                    print("Removida.")
                else:
                    print("Não encontrada.")

            except:
                print("ID inválido.")

        elif opcao == "5":
            break