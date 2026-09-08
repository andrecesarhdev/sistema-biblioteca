import unittest
from biblioteca import GerenciadorUsuarios


class TestCadastroUsuarios(unittest.TestCase):

    def setUp(self):
        self.usuarios = GerenciadorUsuarios()

    def test_cadastrar_usuario_com_sucesso(self):
        usuario = self.usuarios.cadastrar(1, "Maria", "senha123")
        self.assertEqual(usuario.id_usuario, 1)
        self.assertEqual(usuario.nome, "Maria")

    def test_cadastrar_usuario_duplicado_lanca_erro(self):
        self.usuarios.cadastrar(1, "Maria", "senha123")
        with self.assertRaises(ValueError):
            self.usuarios.cadastrar(1, "Outra Maria", "outrasenha")


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.usuarios = GerenciadorUsuarios()
        self.usuarios.cadastrar(1, "Maria", "senha123")

    def test_login_com_senha_correta(self):
        usuario = self.usuarios.login(1, "senha123")
        self.assertEqual(usuario.nome, "Andre")

    def test_login_com_senha_incorreta_lanca_erro(self):
        with self.assertRaises(ValueError):
            self.usuarios.login(1, "senhaerrada")

    def test_login_usuario_inexistente_lanca_erro(self):
        with self.assertRaises(ValueError):
            self.usuarios.login(999, "qualquersenha")


if __name__ == "__main__":
    unittest.main()