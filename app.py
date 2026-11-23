from flask import Flask, render_template
from banco import listar


app = Flask(__name__)

@app.route("/")
def inicio():
    resultado = listar()
    return render_template("index.html", tarefas=resultado)


@app.route("/sobre")
def sobre():
    return "Projeto para aprender Python"

if __name__ == "__main__":
    app.run(debug=True)