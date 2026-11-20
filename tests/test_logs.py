import unittest

from biblioteca import GerenciadorUsuarios, GerenciadorLivros, GerenciadorEmprestimos

class TestLogging(unittest.TestCase):

    def setUp(self):
        self.usuarios = GerenciadorUsuarios()
        self.livros = GerenciadorLivros()
        self.emprestimos = GerenciadorEmprestimos(self.usuarios, self.livros)
        self.usuarios.cadastrar(1, "Tonha", "senha123")
        self.livros.cadastrar(1, "Clean Code")

    def teste_login_com_senha_errada_gera_warning_sem_vazar_senha(self):
        with self.assertLogs("login", level="WARNING") as cm:
            with self.assertRaises(ValueError):
                self.usuarios.login(1, "senha_errada")
        self.assertIn("senha incorreta (id_usuario=1)", cm.output[0])
        self.assertNotIn("senha_errada", cm.output[0])

    def teste_loguin_com_sucesso_gera_info(self):
        with self.assertLogs("login", level="INFO") as cm:
            self.usuarios.login(1, "senha123")
        self.assertIn("Login realizado com sucesso (id_usuario=1)", cm.output[0])
        self.assertNotIn("senha123", cm.output[0])

    def teste_emprestimo_realizado_gera_info(self):
        with self.assertLogs("emprestimo", level="INFO") as cm:
            self.emprestimos.emprestar(1, 1)
        self.assertIn("Empréstimo realizado (id_emprestimo=1, id_usuario=1, id_livro=1)", cm.output[0])

    def test_livro_indisponivel_gera_warning(self):
        self.emprestimos.emprestar(1, 1)
        with self.assertLogs("emprestimo", level="WARNING") as cm:
            with self.assertRaises(ValueError):
                self.emprestimos.emprestar(1, 1)
        self.assertIn("Livro não está disponível para empréstimo (id_livro=1)", cm.output[0])

    def teste_livro_duplicado_gera_warning(self):
        with self.assertLogs("cadastro_livro", level="WARNING") as cm:
            with self.assertRaises(ValueError):
                self.livros.cadastrar(1, "Outro")
        self.assertIn("id_livro=1", cm.output[0])

if __name__ == "__main__":
    unittest.main()