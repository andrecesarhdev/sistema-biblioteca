
class Livro:

   
    def __init__(self, id_livro, titulo, disponivel=True):
        self.id_livro = id_livro
        self.titulo = titulo
        self.disponivel = disponivel  

    
    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"[{self.id_livro}] {self.titulo} - {status}"
      
      

class GerenciadorLivros:

    def __init__(self):
        # Dicionário vazio que vai guardar os livros.
        # A "chave" será o id_livro, e o "valor" será o objeto Livro correspondente.
        self.livros = {}

    # Método para cadastrar um novo livro
    def cadastrar(self, id_livro, titulo):
        
        if id_livro in self.livros:
            raise ValueError("Livro já cadastrado com esse ID.")
        self.livros[id_livro] = Livro(id_livro, titulo)
        return self.livros[id_livro]

    # Método para buscar um livro pelo ID
    def buscar(self, id_livro):
        return self.livros.get(id_livro)

    # Método para listar todos os livros cadastrados
    def listar(self):
        return list(self.livros.values())