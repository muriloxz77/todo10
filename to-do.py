tarefas = []


def cadastrar_tarefa():
    descricao = input("Digite a descrição da tarefa: ")
    tarefa = {"descricao": descricao, "concluida": False}
    tarefas.append(tarefa)
    print("Tarefa cadastrada com sucesso!")

def listar_tarefas():
    if not tarefas:
        print("Não há tarefas cadastradas.")
    else:
        print("Lista de tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f"{i}. {tarefa['descricao']} - Status: {status}")

def alterar_status_tarefa():
    listar_tarefas()
    numero_tarefa = int(input("Digite o número da tarefa que deseja alterar: ")) - 1
    if 0 <= numero_tarefa < len(tarefas):
        tarefa = tarefas[numero_tarefa]
        tarefa["concluida"] = not tarefa["concluida"]
        print("Status da tarefa alterado com sucesso!")
    else:
        print("Número de tarefa inválido.")

def excluir_tarefa():
    listar_tarefas()
    numero_tarefa = int(input("Digite o número da tarefa que deseja excluir: ")) - 1
    if 0 <= numero_tarefa < len(tarefas):
        tarefa = tarefas.pop(numero_tarefa)
        print(f"Tarefa '{tarefa['descricao']}' excluída com sucesso!")
    else:
        print("Número de tarefa inválido.")


def main():
    while True:
        print("\nMenu de Tarefas:")
        print("1. Cadastrar Tarefa")
        print("2. Listar Tarefas")
        print("3. Alterar Status de Tarefa")
        print("4. Excluir Tarefa")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrar_tarefa()
        elif escolha == "2":
            listar_tarefas()
        elif escolha == "3":
            alterar_status_tarefa()
        elif escolha == "4":
            excluir_tarefa()
        elif escolha == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

       
else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
