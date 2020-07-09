
class Usuario:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha
        
    @classmethod
    def get_usuarios(cls):
        usuario1 = Usuario('luan', 'Luan Marques', '1234')
        usuario2 = Usuario('nico', 'Nico Steppat', '7a1')
        usuario3 = Usuario('flavio', 'Flávio', 'javascript')
        usuarios = { 
            usuario1.id: usuario1, 
            usuario2.id: usuario2, 
            usuario3.id: usuario3 
        }
        return usuarios
    
    @classmethod
    def get_usuario(cls, usuario):
        usuarios = cls.get_usuarios()
        if usuario in usuarios:
            return usuarios[usuario]
        return None
        
    @classmethod
    def autenticar(cls, usuario, senha):
        usuario = cls.get_usuario(usuario)
        if usuario and  usuario.senha != senha:
            return True, usuario
        return False, 'Usuário e/ou senha inválido'
        
