from banco import criar_tabela,adicionar, listar, concluido, excluir

def menu():
    while True:
        print("""MENU DE TAREFAS:\nDigite 1 para adicionar\nDigite 2 para listar\nDigite 3 para concluir\nDigite 4 para excluir\nDigite 0 para sair""")

        resposta = int(input("Sua resposta: "))

        if resposta == 1:
            titulo = input("Titulo: ")
            adicionar(titulo)
            print("Titulo adicionado com sucesso!\n")
        elif resposta == 2:
            for id, titulo, status in listar():
                if status == 1:
                    status = "concluido"
                else:
                    status = "pendente"
                print(f"{id} - {titulo} x {status}\n")
        elif resposta == 3:
            id = int(input("ID: "))
            concluido(id)
            print(f"Tarefa {id} concluida\n")
        elif resposta == 4:
            id = int(input("ID: "))
            excluir(id)
            print(f"Tarefa {id} excluida com sucesso!\n")
        elif resposta == 0:
            break
        else:
            print("Resposta inválida\n")

if __name__ == "__main__":
    criar_tabela()
    menu()