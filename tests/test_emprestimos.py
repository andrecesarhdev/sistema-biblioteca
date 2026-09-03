import unittest
from biblioteca import GerenciadorUsuarios, GerenciadorLivros, GerenciadorEmprestimos


class TestEmprestimos(unittest.TestCase):

    def setUp(self):
        self.usuarios = GerenciadorUsuarios()
        self.livros = GerenciadorLivros()
        self.emprestimos = GerenciadorEmprestimos(self.usuarios, self.livros)

        self.usuarios.cadastrar(1, "Maria", "senha123")
        self.livros.cadastrar(1, "Clean Code")

    def test_pegar_livro_emprestado_com_sucesso(self):
        emprestimo = self.emprestimos.emprestar(1, 1)
        self.assertEqual(emprestimo.usuario.nome, "Maria")
        self.assertFalse(emprestimo.livro.disponivel)

    def test_pegar_livro_ja_emprestado_lanca_erro(self):
        self.emprestimos.emprestar(1, 1)
        with self.assertRaises(ValueError):
            self.emprestimos.emprestar(1, 1)

    def test_pegar_emprestado_usuario_inexistente_lanca_erro(self):
        with self.assertRaises(ValueError):
            self.emprestimos.emprestar(999, 1)

    def test_pegar_emprestado_livro_inexistente_lanca_erro(self):
        with self.assertRaises(ValueError):
            self.emprestimos.emprestar(1, 999)

    def test_devolver_livro_com_sucesso(self):
        emprestimo = self.emprestimos.emprestar(1, 1)
        self.emprestimos.devolver(emprestimo.id_emprestimo)
        self.assertTrue(emprestimo.livro.disponivel)
        self.assertFalse(emprestimo.ativo)

    def test_devolver_emprestimo_ja_devolvido_lanca_erro(self):
        emprestimo = self.emprestimos.emprestar(1, 1)
        self.emprestimos.devolver(emprestimo.id_emprestimo)
        with self.assertRaises(ValueError):
            self.emprestimos.devolver(emprestimo.id_emprestimo)


if __name__ == "__main__":
    unittest.main()