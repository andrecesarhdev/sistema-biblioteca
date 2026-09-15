from biblioteca import GerenciadorUsuarios, GerenciadorLivros, GerenciadorEmprestimos


def cadastrar_usuario(usuarios):
    id_usuario = int(input("Digite o ID do novo usuário: "))
    nome = input("Digite o nome: ")
    senha = input("Digite a senha: ")

    try:
        usuarios.cadastrar(id_usuario, nome, senha)
        print(f"Usuário '{nome}' cadastrado com sucesso!")
    except ValueError as erro:
        print(f"Erro ao cadastrar: {erro}")


def fazer_login(usuarios):
    id_usuario = int(input("Digite o ID do usuário: "))
    senha = input("Digite a senha: ")

    try:
        usuario_logado = usuarios.login(id_usuario, senha)
        print(f"Login realizado: {usuario_logado}")
        return usuario_logado
    except ValueError as erro:
        print(f"Erro ao fazer login: {erro}")
        return None


def listar_livros_disponiveis(livros):
    disponiveis = [livro for livro in livros.listar() if livro.disponivel]

    if not disponiveis:
        print("Não há livros disponíveis no momento.")
        return

    print("\nLivros disponíveis:")
    for livro in disponiveis:
        print(f"  {livro}")


def pegar_livro_emprestado(usuario_logado, emprestimos, livros):
    listar_livros_disponiveis(livros)
    try:
        id_livro = int(input("Digite o ID do livro que deseja pegar emprestado: "))
        emprestimo = emprestimos.emprestar(usuario_logado.id_usuario, id_livro)
        print(f"Empréstimo realizado: {emprestimo}")
    except ValueError as erro:
        print(f"Erro ao pegar livro emprestado: {erro}")


def devolver_livro(emprestimos):
    try:
        id_emprestimo = int(input("Digite o ID do empréstimo a devolver: "))
        emprestimo = emprestimos.devolver(id_emprestimo)
        print(f"Livro devolvido: {emprestimo.livro.titulo}")
    except ValueError as erro:
        print(f"Erro ao devolver: {erro}")


def menu_usuario_logado(usuario_logado, emprestimos, livros):
    while True:
        print(f"\n--- Bem-vindo(a), {usuario_logado.nome} ---")
        print("1 - Listar livros disponíveis")
        print("2 - Pegar livro emprestado")
        print("3 - Devolver livro")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_livros_disponiveis(livros)
        elif opcao == "2":
            pegar_livro_emprestado(usuario_logado, emprestimos, livros)
        elif opcao == "3":
            devolver_livro(emprestimos)
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


def main():
    usuarios = GerenciadorUsuarios()
    livros = GerenciadorLivros()
    emprestimos = GerenciadorEmprestimos(usuarios, livros)

    # Dados iniciais de exemplo
    usuarios.cadastrar(1, "Maria", "senha123")
    livros.cadastrar(1, "Clean Code")
    livros.cadastrar(2, "O Programador Pragmático")
    livros.cadastrar(3, "Introdução a Algoritmos")

    while True:
        print("\n=== Sistema de Biblioteca ===")
        print("1 - Cadastrar usuário")
        print("2 - Login")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario(usuarios)
        elif opcao == "2":
            usuario_logado = fazer_login(usuarios)
            if usuario_logado:
                menu_usuario_logado(usuario_logado, emprestimos, livros)
        elif opcao == "3":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()