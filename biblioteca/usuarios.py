# "Molde" (classe) que representa um usuário do sistema.
class Usuario:

    # Construtor: roda automaticamente sempre que um novo Usuario é criado.
    # "self" representa o próprio objeto sendo criado.
    def __init__(self, id_usuario, nome):
        self.id_usuario = id_usuario  # guarda o identificador do usuário
        self.nome = nome              # guarda o nome do usuário

    # Método especial que define como o objeto aparece quando usamos print().
    # Sem isso, print(usuario) mostraria algo ilegível tipo <__main__.Usuario ...>
    def __str__(self):
        # f-string: tudo dentro de { } é substituído pelo valor da variável
        return f"[{self.id_usuario}] {self.nome}"


# Classe responsável por gerenciar todos os usuários cadastrados no sistema.
class GerenciadorUsuarios:

    # Construtor: roda quando criamos o gerenciador (uma única vez, no início do programa)
    def __init__(self):
        # Dicionário vazio que vai guardar os usuários.
        # A "chave" será o id_usuario, e o "valor" será o objeto Usuario correspondente.
        self.usuarios = {}

    # Método para cadastrar um novo usuário
    def cadastrar(self, id_usuario, nome):
        # Verifica se já existe um usuário com esse ID
        if id_usuario in self.usuarios:
            raise ValueError("Usuário já cadastrado com esse ID.")

        # Cria o objeto Usuario e guarda no dicionário, usando o ID como chave
        self.usuarios[id_usuario] = Usuario(id_usuario, nome)
        return self.usuarios[id_usuario]

    # Método para buscar um usuário pelo ID
    def buscar(self, id_usuario):
        return self.usuarios.get(id_usuario)

    # Método para listar todos os usuários cadastrados
    def listar(self):
        return list(self.usuarios.values())