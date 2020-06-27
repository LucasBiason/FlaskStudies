
class Jogo:
    
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
        
    @classmethod
    def get_jogos(cls):
        jogo1 = Jogo('Super Mario', 'Acao', 'SNES')
        jogo2 = Jogo('Pokemon Gold', 'RPG', 'GBA')
        jogo3 = Jogo('Mortal Kombat', 'Luta', 'SNES')
        lista = [jogo1, jogo2, jogo3]
        return lista