import unittest
from biblioteca import GerenciadorLivros


class TestCadastroLivros(unittest.TestCase):

    def setUp(self):
        self.livros = GerenciadorLivros()

    def test_cadastrar_livro_com_sucesso(self):
        livro = self.livros.cadastrar(1, "Clean Code")
        self.assertEqual(livro.titulo, "Clean Code")
        self.assertTrue(livro.disponivel)

    def test_cadastrar_livro_duplicado_lanca_erro(self):
        self.livros.cadastrar(1, "Clean Code")
        with self.assertRaises(ValueError):
            self.livros.cadastrar(1, "Outro Livro")

    def test_buscar_livro_existente(self):
        self.livros.cadastrar(1, "Clean Code")
        livro = self.livros.buscar(1)
        self.assertIsNotNone(livro)
        self.assertEqual(livro.titulo, "Clean Code")

    def test_buscar_livro_inexistente_retorna_none(self):
        livro = self.livros.buscar(999)
        self.assertIsNone(livro)


if __name__ == "__main__":
    unittest.main()