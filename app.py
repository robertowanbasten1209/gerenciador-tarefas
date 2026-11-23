from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Gerenciador de Tarefas"

@app.route("/sobre")
def sobre():
    return "Projeto para aprender Python"

if __name__ == "__main__":
    app.run(debug=True)