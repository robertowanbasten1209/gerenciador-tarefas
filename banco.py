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
