import flask
from flask  import Flask, render_template
from models import Jogo, Usuario
from decorators import login_required

app = Flask(__name__)
app.secret_key = 'SECRET_KEY'

JOGOS =  Jogo.get_jogos()

@app.route('/')
@login_required
def listagem():
    context = {
        'titulo': 'Jogos',
        'lista_jogos': JOGOS
    }
    return render_template( 'lista.html', ** context)
    

@app.route('/novo', methods=['GET', 'POST' ])
@login_required
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
        flask.flash(
            'Jogo {} cadastrado com sucesso.'.format(
                jogo_novo.nome
            ),
            'success'
        )
        return flask.redirect('/home')
        
    return render_template(
        'novo.html', ** context
    )

    
@app.route('/login')
def login():
    proxima = flask.request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    status, retorno = Usuario.autenticar(
         flask.request.form['usuario'],
         flask.request.form['senha']         
    )
    if status:
        flask.flash(retorno.nome + ' logou com sucesso!', 'success')
        proxima_pagina =  flask.request.form.get('proxima', '')
        flask.session['usuario_logado'] = retorno.id
        return  flask.redirect('/' if not proxima_pagina else proxima_pagina)
    
    flask.flash(retorno, 'danger')
    return  flask.redirect (flask.url_for('login'))
        

@app.route('/logout')
def logout():
    flask.session['usuario_logado'] = None
    return flask.redirect(flask.url_for('login'))

# run the application
if __name__ == "__main__":
    app.run(debug=True)

