from datetime import datetime


class Emprestimo:
  
  def __init__(self, id_emprestimo, usuario, livro):
    self.id_emprestimo = id_emprestimo
    self.usuario = usuario
    self.livro = livro
    self.data_emprestimo = datetime.now()
    self.data_devolução = None
    self.ativo = True
    
    
  def __str__(self):
    status = "Ativo" if self.ativo else "Devolvido"
    return f"[{self.id_emprestimo}]{self.livro.titulo} -> {self.usuario.nome}({status})"
  
  
class GerenciadorEmprestimos:

    def __init__(self, gerenciador_usuarios, gerenciador_livros):
        self.emprestimos = {}
        self.proximo_id = 1
        self.gerenciador_usuarios = gerenciador_usuarios
        self.gerenciador_livros = gerenciador_livros

    def emprestar(self, id_usuario, id_livro):
        usuario = self.gerenciador_usuarios.buscar(id_usuario)
        if usuario is None:
            raise ValueError("Usuário não encontrado.")

        livro = self.gerenciador_livros.buscar(id_livro)
        if livro is None:
            raise ValueError("Livro não encontrado.")

        if not livro.disponivel:
            raise ValueError("Livro não está disponível para empréstimo.")

        livro.disponivel = False
        emprestimo = Emprestimo(self.proximo_id, usuario, livro)
        self.emprestimos[self.proximo_id] = emprestimo
        self.proximo_id += 1
        return emprestimo

    def devolver(self, id_emprestimo):
        emprestimo = self.emprestimos.get(id_emprestimo)
        if emprestimo is None:
            raise ValueError("Empréstimo não encontrado.")

        if not emprestimo.ativo:
            raise ValueError("Este empréstimo já foi devolvido.")

        emprestimo.ativo = False
        emprestimo.data_devolucao = datetime.now()
        emprestimo.livro.disponivel = True
        return emprestimo

    def listar_ativos(self):
        return [e for e in self.emprestimos.values() if e.ativo]

    def buscar(self, id_emprestimo):
        return self.emprestimos.get(id_emprestimo)