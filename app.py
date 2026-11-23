from flask import Flask, render_template, request, redirect
from banco import listar, adicionar,concluido, excluir


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

@app.route("/concluir/<int:idt>", methods=["Post"])
def rota_concluir(idt):
    concluido(idt)
    return redirect("/")

@app.route("/excluir/<int:idt>", methods=["Post"])
def rota_excluir(idt):
    excluir(idt)
    return redirect("/")

@app.route("/sobre")
def sobre():
    return "Projeto para aprender Python"

if __name__ == "__main__":
    app.run(debug=True)