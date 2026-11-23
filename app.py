from flask import Flask, render_template, request, redirect
from banco import listar, adicionar


app = Flask(__name__)

@app.route("/")
def inicio():
    resultado = listar()
    return render_template("index.html", tarefas=resultado)

@app.route("/adicionar", methods=["Post"])
def rota_adcionar():
    titulo = request.form["titulo"]
    adicionar(titulo)
    return redirect("/")

@app.route("/sobre")
def sobre():
    return "Projeto para aprender Python"

if __name__ == "__main__":
    app.run(debug=True)