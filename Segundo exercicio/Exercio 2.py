from flask import Flask, request, render_template

app = Flask(__name__)

strings = []

@app.route("/", methods=["GET", "POST"])
def obter_strings():
    if request.method == "POST":
        string = request.form["string"]
        strings.append(string)
    
    resultado = verificar(strings)
    return render_template("verifica.html", strings=strings, resultado=resultado)

def verificar(strings):
    for i in range(1, len(strings)):
        if strings[i] < strings[i-1]:
            return False
    return True

if __name__ == "__main__":
    app.run(debug=True)
