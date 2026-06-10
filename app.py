from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def inicio():
    nome = request.cookies.get('nome')
    email = request.cookies.get('email')
    tema = request.cookies.get('tema', 'claro')
    return render_template('inicio.html', nome=nome, email=email, tema=tema)

@app.route('/salvar', methods=['POST'])
def salvar():
    nome = request.form.get('nome')
    email = request.form.get('email')
    resp = make_response("Preferências salvas com sucesso <a href='/'>Voltar</a>")
    resp.set_cookie('nome', nome, max_age=60*60*24*30)
    resp.set_cookie('email', email, max_age=60*60*24*30)
    return resp

@app.route('/tema/<modo>')
def tema(modo):
    resp = make_response("Tema atualizado com sucesso <a href='/'>Voltar</a>")
    resp.set_cookie('tema', modo, max_age=60*60*24*30)
    return resp

if __name__ == '__main__':
    app.run(debug=True)
