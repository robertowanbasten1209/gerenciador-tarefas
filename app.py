from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Gerenciador de Tarefas"

if __name__ == "__main__":
    app.run(debug=True)