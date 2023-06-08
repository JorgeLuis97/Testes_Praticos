from flask import Flask, jsonify, render_template, request, redirect
from operator import itemgetter

app = Flask(__name__)

funcionarios = {}

@app.route('/', methods=['GET', 'POST'])
def index():
        if request.method == 'POST':
            id = request.form['id']

            if id in funcionarios:
                return render_template('index.html', message='ID já cadastrado, Favor inserir outro ID')

            nome = request.form['nome']
            cpf = request.form['cpf']
            cargo = request.form['cargo']
            salario = request.form['salario']

            funcionario_dicionario = {
                'id': id,
                'nome': nome,
                'cargo': cargo,
                'cpf': cpf,
                'salario': salario
            }

            funcionarios[id] = funcionario_dicionario

            return render_template('index.html', message='Cadastro realizado com sucesso')

        return render_template('index.html')

@app.route('/funcionarios/delete/<int:id>', methods=['GET'])
def deleta_funcionario(id):
    if id in funcionarios:
        del funcionarios[id]
        return redirect('/funcionarios')
    else:
        return "Funcionário não encontrado"
                           
@app.route('/funcionarios', methods=['GET'])
def lista_funcionarios():
    ordenacao = sorted(funcionarios.values(), key=itemgetter('nome'))

    return render_template('funcionarios.html', funcionarios=ordenacao)


if __name__ == '__main__':
     app.run(debug=True)