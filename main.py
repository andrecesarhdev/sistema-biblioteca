from biblioteca import GerenciadorUsuarios, GerenciadorLivros, GerenciadorEmprestimos


def main():
    usuarios = GerenciadorUsuarios()
    livros = GerenciadorLivros()
    emprestimos = GerenciadorEmprestimos(usuarios, livros)

    usuarios.cadastrar(1, "Andre", "senha123")
    usuarios.cadastrar(2, "Marcos", "outrasenha")
    usuarios.cadastrar(3, "Felipe", "123senha")
    livros.cadastrar(1, "Java Básico")
    
    id_usuario = int(input("Digite o ID do usuário: "))
    senha = input("Digite a senha: ")

    try:
        usuario_logado = usuarios.login(id_usuario, senha)
    except ValueError as erro:
        print(f"Erro ao fazer login: {erro}")
        return

    print(f"Login realizado: {usuario_logado}")

    try:
        emprestimo = emprestimos.emprestar(usuario_logado.id_usuario, 1)
    except ValueError as erro:
        print(f"Erro ao realizar empréstimo: {erro}")
        return

    print(f"Empréstimo realizado: {emprestimo}")


if __name__ == "__main__":
    main()
