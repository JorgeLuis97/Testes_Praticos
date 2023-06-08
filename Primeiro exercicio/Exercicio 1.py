from flask import Flask, request, render_template
from operator import itemgetter

app = Flask(__name__)

funcionarios = {}

@app.route("/", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        id = request.form["id"]
        
        if id in funcionarios:
            return render_template("index.html", message="ID já cadastrado")
        
        nome = request.form["nome"]
        cpf = request.form["cpf"]
        cargo = request.form["cargo"]
        salario = request.form["salario"]

        dicionario = {
            "id": id,
            "nome": nome,
            "cpf": cpf,
            "cargo": cargo,
            "salario": salario
        }

        funcionarios[id] = dicionario

        return render_template("index.html", message="Cadastro realizado com sucesso")
    
    return render_template("index.html")

@app.route("/funcionarios", methods=["GET"])
def obter_fun():
    ordenar = sorted(funcionarios.values(), key=itemgetter("nome"))

    return render_template("funcionarios.html", funcionarios=ordenar)


if __name__ == "__main__":
    app.run(debug=True)
