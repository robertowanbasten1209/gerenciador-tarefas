import sqlite3

def criar_tabela():
    conn = sqlite3.connect("tarefas.db")
    with conn:
        conn.execute("""Create table tarefas(
        id INTEGER PRIMARY KEY,
        titulo Varchar(100) NOT NULL,
        concluida INT DEFAULT 0)""")
    conn.close()

if __name__ == "__main__":
    criar_tabela

    conn = sqlite3.connect("tarefas.db")
    res = conn.execute("SELECT name FROM sqlite_master WHERE name = 'tarefas'")
    print(res.fetchone())
    conn.close