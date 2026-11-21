# 📚 Sistema Biblioteca

Sistema de gerenciamento de biblioteca em Python, desenvolvido em equipe na formação DevOps da FAP/Aponti, no Porto Digital. O foco do projeto é a automação do ciclo de entrega do software: testes automatizados, containerização, pipelines de CI/CD em duas plataformas e observabilidade (logs com Grafana Loki e estrutura de métricas com Prometheus).

## Funcionalidades

- Cadastro de usuários
- Login de usuários
- Cadastro de livros
- Controle de empréstimos e devoluções
- Registro de logs de todas as operações importantes (login, cadastros, empréstimos, devoluções e falhas)

## Stack técnica

| Área                        | Tecnologia                                             |
| --------------------------- | ------------------------------------------------------ |
| Linguagem                   | Python 3.11                                            |
| Testes de aplicação         | unittest                                               |
| Segurança                   | Bandit e pip-audit                                     |
| Automação de infraestrutura | Ansible                                                |
| Testes de infraestrutura    | Molecule e Testinfra                                   |
| Containerização             | Docker e Docker Compose                                |
| Logs                        | logging (Python), Grafana Alloy, Grafana Loki, Grafana |
| Métricas e alertas          | Prometheus e Alertmanager (estrutura preparada)        |
| Banco de dados              | AWS DynamoDB (boto3), em fase de integração            |
| CI/CD                       | GitHub Actions e GitLab CI                             |
| Versionamento               | Git, com repositórios espelhados no GitHub e no GitLab |

## Estrutura do projeto

```
sistema-biblioteca/
├── .github/workflows/      # Pipeline do GitHub Actions
├── Ansible/                # Automação (role biblioteca, testes com Molecule)
│   ├── ansible.cfg
│   ├── inventory.ini
│   ├── playbook.yml
│   └── roles/biblioteca/
│       ├── defaults/
│       ├── tasks/
│       └── molecule/
├── Docker/                 # Serviços do Docker Compose
│   ├── compose.yml
│   ├── alloy/              # Coletor de logs (config.alloy)
│   ├── loki/               # Armazenamento de logs (loki-config.yml)
│   ├── grafana/            # Fonte de dados provisionada (Loki e Prometheus)
│   ├── prometheus/         # Métricas e regras de alerta
│   └── alertmanager/       # Envio de alertas
├── biblioteca/             # Código da aplicação
│   ├── usuarios.py
│   ├── livros.py
│   ├── emprestimos.py
│   └── logs.py             # Configuração central do logging
├── tests/                  # Testes automatizados da aplicação
├── .gitlab-ci.yml          # Pipeline do GitLab CI
├── .env.example            # Modelo das variáveis de ambiente
├── Dockerfile              # Imagem Docker da aplicação
├── database.py             # Exemplo de acesso ao DynamoDB
├── monitoramento.py        # Estrutura de métricas (Prometheus)
├── main.py                 # Ponto de entrada
└── requirements.txt        # Dependências
```

## Rodando localmente

### Com Python

```bash
git clone https://github.com/andrecesarhdev/sistema-biblioteca.git
cd sistema-biblioteca
pip install -r requirements.txt
python main.py
```

Os logs aparecem no próprio terminal, junto com os menus.

### Com Docker (só a aplicação)

```bash
docker build -t sistema-biblioteca .
docker run -it sistema-biblioteca
```

### Com Docker Compose (aplicação + logs)

1. Crie o arquivo de variáveis de ambiente a partir do modelo e defina a senha do Grafana:

```bash
cp .env.example .env
```

2. Suba os serviços de logs e abra o menu da aplicação:

```bash
cd Docker
docker compose up -d loki alloy grafana
docker compose run --rm biblioteca
```

No Git Bash do Windows, use `winpty docker compose run --rm biblioteca` para o menu interativo funcionar. No cmd e no PowerShell o comando normal funciona.

Depois de alterar o código da aplicação, reconstrua a imagem antes de rodar de novo:

```bash
docker compose build biblioteca
```

3. Acesse as interfaces:

| Serviço       | Endereço               | Observação                                   |
| ------------- | ---------------------- | -------------------------------------------- |
| Grafana       | http://localhost:3000  | Login definido no `.env`; use a tela Explore |
| Grafana Alloy | http://localhost:12345 | Estado dos componentes de coleta             |
| Prometheus    | http://localhost:9090  | Estrutura de métricas                        |

O Loki não é exposto fora da rede do Compose, de propósito.

## Logs e monitoramento (Grafana Loki)

A aplicação usa o módulo `logging` do Python e escreve no stdout do container. O Grafana Alloy lê esses logs, transforma o nível e a funcionalidade em rótulos e envia ao Loki. O Grafana consulta o Loki com LogQL.

```
Sistema de Biblioteca → stdout do container → Grafana Alloy → Loki → Grafana
```

### Formato do registro

```
AAAA-MM-DD HH:MM:SS NÍVEL [módulo] mensagem
```

Exemplo:

```
2026-11-20 08:31:12 WARNING [login] Tentativa de login inválida: senha incorreta (id_usuario=1)
```

### Níveis

| Nível   | Quando usar                                                                                    |
| ------- | ---------------------------------------------------------------------------------------------- |
| INFO    | Operação concluída normalmente (login, cadastro, empréstimo, devolução)                        |
| WARNING | Situação anormal tratada pelo sistema (login inválido, cadastro duplicado, livro indisponível) |
| ERROR   | Falha que impediu a operação (erro inesperado, banco de dados inacessível)                     |

### Módulos e rótulos

| Módulo (`funcionalidade`) | Eventos                                           |
| ------------------------- | ------------------------------------------------- |
| `login`                   | Login com sucesso e tentativas inválidas          |
| `cadastro_usuario`        | Cadastro de usuário e cadastro duplicado          |
| `cadastro_livro`          | Cadastro de livro e cadastro duplicado            |
| `emprestimo`              | Empréstimo realizado, livro indisponível e falhas |
| `devolucao`               | Livro devolvido e devolução inválida              |
| `banco`                   | Falhas de conexão com o DynamoDB                  |

Rótulos no Loki: `app` (sempre `biblioteca`), `level` e `funcionalidade`. Identificadores como `id_usuario` ficam no texto da mensagem e não viram rótulo.

### Consultas úteis (LogQL)

Todos os erros da aplicação:

```logql
{app="biblioteca", level="ERROR"}
```

Tentativas de login malsucedidas:

```logql
{app="biblioteca", funcionalidade="login", level="WARNING"}
```

Empréstimos realizados:

```logql
{app="biblioteca", funcionalidade="emprestimo"} |= "Empréstimo realizado"
```

Falhas de uma funcionalidade específica (troque o valor de `funcionalidade`):

```logql
{app="biblioteca", funcionalidade="emprestimo", level="ERROR"}
```

Logins inválidos a cada 5 minutos (base para um alerta):

```logql
sum(count_over_time({app="biblioteca", funcionalidade="login", level="WARNING"}[5m]))
```

### Segurança dos logs

- Senhas e credenciais nunca são registradas. Apenas o identificador do usuário aparece.
- O Grafana exige login (definido no `.env`) e o Loki não fica exposto fora do servidor.
- Os logs ficam guardados por 7 dias no Loki, e o Docker limita o tamanho dos arquivos de log da aplicação.

### Métricas (Prometheus)

A estrutura de métricas (Prometheus, Alertmanager e `monitoramento.py`) está preparada, mas a coleta de métricas da aplicação ainda não foi implementada.

## Pipelines de CI/CD

O projeto tem pipelines configurados em duas plataformas, com as mesmas etapas:

1. **Build:** prepara o ambiente e verifica se o código compila
2. **Security:** análise estática com Bandit e verificação de dependências com pip-audit
3. **Test:** executa os testes automatizados com unittest
4. **Deploy:** etapa final (simulada), executada somente se as etapas anteriores passarem

- GitHub Actions: `.github/workflows/pipeline.yml`
- GitLab CI: `.gitlab-ci.yml`

## Automação com Ansible

- **`Ansible/ansible.cfg`**: configuração central do Ansible.
- **`Ansible/inventory.ini`**: inventário local (localhost).
- **`Ansible/playbook.yml`**: playbook principal, que executa a role `biblioteca`.
- **`Ansible/roles/biblioteca/`**: valida o Python, cria o diretório `/tmp/sistema-biblioteca`, copia a aplicação e seus testes, cria o `.venv`, instala as dependências e roda a suíte de testes.

## Rodando os testes

Testes unitários da aplicação:

```bash
python -m unittest discover -s tests -v
```

Automação com Ansible:

```bash
cd Ansible
ansible-playbook -i inventory.ini playbook.yml
```

Validação de idempotência e testes de infraestrutura com Molecule:

```bash
cd Ansible/roles/biblioteca
export ANSIBLE_ROLES_PATH="$(pwd)/.."
molecule test
```

## Equipe

Projeto desenvolvido em grupo na turma de DevOps da FAP/Aponti:

- André César ([GitHub](https://github.com/andrecesarhdev) · [LinkedIn](https://www.linkedin.com/in/andrecesar-dev/))
- Marcos Nascimento ([GitHub](https://github.com/MarcosNasc-DEV))
- Luiz Felipe ([GitHub](https://github.com/LuizFelipeMoraesSantos))
