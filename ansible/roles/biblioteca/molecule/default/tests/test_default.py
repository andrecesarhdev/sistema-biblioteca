import pytest

testinfra_hosts = ["local://localhost"]


def test_app_directory_exists(host):
    """1. Verifica se o diretório /tmp/sistema-biblioteca existe."""
    app_dir = host.file("/tmp/sistema-biblioteca")
    assert app_dir.exists


def test_app_directory_is_directory(host):
    """2. Verifica se o diretório da aplicação é realmente um diretório."""
    app_dir = host.file("/tmp/sistema-biblioteca")
    assert app_dir.is_directory


def test_venv_directory_exists(host):
    """3. Verifica se o ambiente virtual foi criado."""
    venv_dir = host.file("/tmp/sistema-biblioteca/venv")
    assert venv_dir.exists
    assert venv_dir.is_directory


def test_venv_python_executable_exists(host):
    """4. Verifica se o executável Python do ambiente virtual existe."""
    python_exec = host.file("/tmp/sistema-biblioteca/venv/bin/python3")
    assert python_exec.exists
    assert python_exec.is_file


def test_requirements_file_exists(host):
    """5. Verifica se o arquivo requirements.txt foi copiado."""
    req_file = host.file("/tmp/sistema-biblioteca/requirements.txt")
    assert req_file.exists
    assert req_file.is_file


def test_tests_folder_exists(host):
    """6. Verifica se a pasta tests/ foi copiada."""
    tests_dir = host.file("/tmp/sistema-biblioteca/tests")
    assert tests_dir.exists
    assert tests_dir.is_directory