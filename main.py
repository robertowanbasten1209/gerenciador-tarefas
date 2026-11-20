import sqlite3

def criar_tabela():
    conn = sqlite3.connect("tarefas.db")
    with conn:
        conn.execute("""Create table IF NOT EXISTS tarefas(
        id INTEGER PRIMARY KEY,
        titulo Varchar(100) NOT NULL,
        concluida INT DEFAULT 0)""")
    conn.close()

def adicionar(titulo):
    conn = sqlite3.connect("tarefas.db")
    with conn:
        conn.execute("INSERT INTO tarefas (titulo) VALUES (?)", (titulo,))
    conn.close()

def listar():
    conn = sqlite3.connect("tarefas.db")
    resultado = conn.execute("SELECT id,titulo,concluida FROM tarefas").fetchall()
    conn.close()
    return resultado

def excluir(id):
    conn = sqlite3.connect("tarefas.db")
    with conn:
        conn.execute("DELETE FROM tarefas WHERE id = ?", (id,))
    conn.close()

def concluido(id):
    conn = sqlite3.connect("tarefas.db")
    with conn:
        conn.execute("UPDATE tarefas SET concluida = 1 WHERE id = ?", (id,))
    conn.close()

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

    conn = sqlite3.connect("tarefas.db")
    res = conn.execute("SELECT name FROM sqlite_master WHERE name = 'tarefas'")
    print(res.fetchone())
    conn.close()