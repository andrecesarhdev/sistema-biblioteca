class Usuario:

    def __init__(self, id_usuario, nome, senha):
        self.id_usuario = id_usuario
        self.nome = nome
        self.senha = senha

    def __str__(self):

        return f"[{self.id_usuario}] {self.nome}"


class GerenciadorUsuarios:

    def __init__(self):

        self.usuarios = {}

    def cadastrar(self, id_usuario, nome, senha):

        if id_usuario in self.usuarios:
            raise ValueError("Usuário já cadastrado com esse ID.")

        self.usuarios[id_usuario] = Usuario(id_usuario, nome, senha)
        return self.usuarios[id_usuario]

    def buscar(self, id_usuario):
        return self.usuarios.get(id_usuario)

    def listar(self):
        return list(self.usuarios.values())
    
    def login(self, id_usuario,senha):
        usuario = self.buscar(id_usuario)
        
        if usuario is None:
            raise ValueError("Usuario não encontrado")
        
        if usuario.senha != senha:
            raise ValueError("Senha incorreta")
        
        return usuario
        
