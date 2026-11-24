import logging
from datetime import datetime


log_emprestimo = logging.getLogger("emprestimo")
log_devolucao = logging.getLogger("devolucao")


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
        
    # MONITORAMENTO: contabilizar empréstimos realizados
    def emprestar(self, id_usuario, id_livro):
        usuario = self.gerenciador_usuarios.buscar(id_usuario)
        if usuario is None:
            log_emprestimo.warning("Usuário não encontrado (id_usuario=%s)", id_usuario)
            raise ValueError("Usuário não encontrado.")

        livro = self.gerenciador_livros.buscar(id_livro)
        if livro is None:
            log_emprestimo.warning("Livro não encontrado (id_livro=%s)", id_livro)
            raise ValueError("Livro não encontrado.")

        if not livro.disponivel:
            log_emprestimo.warning("Livro não está disponível para empréstimo (id_livro=%s)", id_livro)
            raise ValueError("Livro não está disponível para empréstimo.")

        livro.disponivel = False
        emprestimo = Emprestimo(self.proximo_id, usuario, livro)
        self.emprestimos[self.proximo_id] = emprestimo
        self.proximo_id += 1
        log_emprestimo.info("Empréstimo realizado (id_emprestimo=%s, id_usuario=%s, id_livro=%s)", emprestimo.id_emprestimo, id_usuario, id_livro,
        )
        return emprestimo
    
    # MONITORAMENTO: contabilizar devoluções realizadas
    def devolver(self, id_emprestimo):
        emprestimo = self.emprestimos.get(id_emprestimo)
        if emprestimo is None:
            log_devolucao.warning("Empréstimo não encontrado (id_emprestimo=%s)", id_emprestimo)
            raise ValueError("Empréstimo não encontrado.")

        if not emprestimo.ativo:
            log_devolucao.warning("Este empréstimo já foi devolvido (id_emprestimo=%s)", id_emprestimo)
            raise ValueError("Este empréstimo já foi devolvido.")

        emprestimo.ativo = False
        emprestimo.data_devolucao = datetime.now()
        emprestimo.livro.disponivel = True
        log_devolucao.info("Livro devolvido (id_emprestimo=%s)", id_emprestimo)
        return emprestimo

    def listar_ativos(self):
        return [e for e in self.emprestimos.values() if e.ativo]

    def buscar(self, id_emprestimo):
        return self.emprestimos.get(id_emprestimo)