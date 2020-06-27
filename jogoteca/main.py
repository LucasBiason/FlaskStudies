from flask  import Flask, render_template
from models import Jogo

app = Flask(__name__)

@app.route('/')
def teste():
    context = {
        'titulo': 'Jogos',
        'lista_jogos': Jogo.get_jogos()
    }
    return render_template(
        'lista.html', ** context
    )

# run the application
if __name__ == "__main__":
    app.run(debug=True)

