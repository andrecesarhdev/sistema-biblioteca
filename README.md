# 📚 Sistema Biblioteca

Sistema de gerenciamento de biblioteca em Python, desenvolvido em equipe na formação DevOps da FAP/Aponti, no Porto Digital. O foco do projeto é a automação do ciclo de entrega do software, com testes automatizados, containerização e pipelines de CI/CD em duas plataformas.

## Funcionalidades

- Login de usuários
- Cadastro de usuários
- Cadastro de livros
- Controle de empréstimos

## Stack técnica

| Área | Tecnologia |
|---|---|
| Linguagem | Python |
| Testes | unittest |
| Containerização | Docker |
| CI/CD | GitHub Actions e GitLab CI |
| Versionamento | Git, com repositórios espelhados no GitHub e no GitLab |

## Pipelines de CI/CD

O projeto tem pipelines configurados em duas plataformas, com as mesmas etapas:

1. **Build:** prepara o ambiente e instala as dependências
2. **Test:** executa os testes automatizados com unittest
3. **Deploy:** etapa final, executada somente se os testes passarem

- GitHub Actions: `.github/workflows/`
- GitLab CI: `.gitlab-ci.yml`

## Estrutura do projeto

```
sistema-biblioteca/
├── .github/workflows/   # Pipeline do GitHub Actions
├── biblioteca/          # Código da aplicação
├── tests/               # Testes automatizados
├── .gitlab-ci.yml       # Pipeline do GitLab CI
├── Dockerfile           # Imagem Docker da aplicação
├── main.py              # Ponto de entrada
└── requirements.txt     # Dependências
```

## Rodando localmente

### Com Python

```bash
git clone https://github.com/andrecesarhdev/sistema-biblioteca.git
cd sistema-biblioteca
pip install -r requirements.txt
python main.py
```

### Com Docker

```bash
docker build -t sistema-biblioteca .
docker run -it sistema-biblioteca
```

### Rodando os testes

```bash
python -m unittest discover tests
```

## Equipe

Projeto desenvolvido em grupo na turma de DevOps da FAP/Aponti:

- André César ([GitHub](https://github.com/andrecesarhdev) · [LinkedIn](https://www.linkedin.com/in/andrecesar-dev/))
