

listas = ["coisa 1", "coisa 2", "coisa 3"]

while True:
    nova_tarefa = input("Qual a sua nova tarefa? (Digite 'sair' para terminar): ")
    
    if nova_tarefa.lower() == 'sair':
        break
    
    listas.append(nova_tarefa)
    
    print("Lista atualizada:", listas)  