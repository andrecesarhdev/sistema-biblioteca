import logging

log = logging.getLogger("cadastro_livro")
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

        self.livros = {}

    # MONITORAMENTO: contabilizar livros cadastrados
    def cadastrar(self, id_livro, titulo):

        if id_livro in self.livros:
            log.warning("Livro já cadastrado com esse ID (id_livro=%s)", id_livro)
            raise ValueError("Livro já cadastrado com esse ID.")
        self.livros[id_livro] = Livro(id_livro, titulo)
        log.info("Livro cadastrado com sucesso (id_livro=%s)", id_livro)
        return self.livros[id_livro]

    def buscar(self, id_livro):
        return self.livros.get(id_livro)

    def listar(self):
        return list(self.livros.values())
