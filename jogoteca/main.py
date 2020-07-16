import flask, os, time
from flask  import Flask, render_template
from models import Jogo, Usuario
from decorators import login_required

app = Flask(__name__)
app.secret_key = 'SECRET_KEY'

from flask_mysqldb import MySQL
app.config['MYSQL_HOST'] = "0.0.0.0"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "admin"
app.config['MYSQL_DB'] = "jogoteca"
app.config['MYSQL_PORT'] = 3306
app.config['UPLOAD_PATH'] = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
db = MySQL(app)


@app.route('/')
@login_required
def listagem():
    context = {
        'titulo': 'Jogos',
        'lista_jogos':  Jogo.get_jogos(db)
    }
    return render_template( 'lista.html', ** context)
    

@app.route('/novo', methods=['GET', 'POST' ])
@login_required
def cadastro():
    context = {
        'titulo': 'Jogos - Cadastro',
        'jogo': None,
        'capa_jogo': '',
        'timestamp':''
    }
    
    if flask.request.method == 'POST':
        id =  flask.request.form.get('id')
        nome =  flask.request.form.get('nome')
        categoria =  flask.request.form.get('categoria')
        console =  flask.request.form.get('console')
        jogo = Jogo(nome, categoria, console, id=id)
        Jogo.salvar(db, jogo)
            
        arquivo =  flask.request.files['arquivo']
        upload_path = app.config['UPLOAD_PATH']
        arquivo.save(f'{upload_path}/capa{jogo.id}.jpg')
    
        flask.flash(
            f'Jogo {jogo.nome} salvo com sucesso.',
            'success'
        )
        return flask.redirect('/')
        
    return render_template(
        'novo.html', ** context
    )


@app.route('/editar/<int:id>', methods=['GET', 'POST' ])
@login_required
def editar(id):
    jogo = Jogo.busca_por_id(db, id)
    context = {
        'titulo': 'Jogos - Editando jogo',
        'jogo': jogo,
        'capa_jogo': f'capa{id}.jpg',
        'timestamp': time.time()
    }    
    return render_template('novo.html', ** context)

@app.route('/deletar/<int:id>')
def deletar(id):
    Jogo.deletar(db, id)
    flask.flash('O jogo foi removido com sucesso!', 'success')
    return flask.redirect( flask.url_for('listagem'))
    
    

@app.route('/uploads/')    
@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo=None):
    default = 'capa_padrao.jpg'
    if not nome_arquivo:
        nome_arquivo =default
    try:
        return flask.send_from_directory('uploads', nome_arquivo)
    except:
        return flask.send_from_directory('uploads', default)



@app.route('/login')
def login():
    proxima = flask.request.args.get('proxima', '')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST',])
def autenticar():
    status, retorno = Usuario.autenticar(
        db,
        flask.request.form['usuario'],
        flask.request.form['senha']         
    )
    if status:
        flask.flash(retorno.nome + ' logou com sucesso!', 'success')
        proxima_pagina =  flask.request.form.get('proxima', '')
        flask.session['usuario_logado'] = retorno.id
        print("proxima_pagina: ", proxima_pagina)
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

