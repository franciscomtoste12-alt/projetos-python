lista = []  
while True:
    print("adicionar tarefa: ")
    print("Ver tarefas: ")
    print("Remover tarefa: ")
    print("Sair: ")
    escolha_lista = input("Escolhe uma opção: ")
    if escolha_lista == "4":
        print("obrigado")
        break
    elif escolha_lista == "1":
        tarefa = input("Digite a tarefa: ")
        lista.append(tarefa)
        print("Tarefa adicionada com sucesso!")
    elif escolha_lista == "2":
        for tarefa in lista:
            print(tarefa)
    elif escolha_lista == "3":
        tarefa_remover = input("Digite a tarefa que deseja remover: ")
        if tarefa_remover in lista:
            lista.remove(tarefa_remover)
            print("Tarefa removida com sucesso!")
        else:
            print("Tarefa não encontrada na lista.")
