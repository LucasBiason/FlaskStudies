import flask
from flask  import Flask, render_template
from models import Jogo

app = Flask(__name__)
app.secret_key = 'SECRET_KEY'


JOGOS =  Jogo.get_jogos()

@app.route('/home')
def listagem():
    context = {
        'titulo': 'Jogos',
        'lista_jogos': JOGOS
    }
    return render_template( 'lista.html', ** context)
    

@app.route('/novo', methods=['GET', 'POST' ])
def cadastro():
    context = {
        'titulo': 'Jogos - Cadastro',
    }
    
    if flask.request.method == 'POST':
        nome =  flask.request.form.get('nome')
        categoria =  flask.request.form.get('categoria')
        console =  flask.request.form.get('console')
        jogo_novo = Jogo(nome, categoria, console)
        JOGOS.append(jogo_novo)
        flask.flash(f'Jogo {jogo_novo.nome} cadastrado com sucesso.', 'success')
        return flask.redirect('/home')
        
    return render_template(
        'novo.html', ** context
    )


# run the application
if __name__ == "__main__":
    app.run(debug=True)

