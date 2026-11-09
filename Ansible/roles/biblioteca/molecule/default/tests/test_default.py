import os

APP_DIR = "/tmp/sistema-biblioteca"
VENV_DIR = os.path.join(APP_DIR, "venv")

def test_app_directory_exists(host):
    f = host.file(APP_DIR)
    assert f.exists

def test_app_directory_is_directory(host):
    f = host.file(APP_DIR)
    assert f.is_directory

def test_virtualenv_exists(host):
    v = host.file(VENV_DIR)
    assert v.exists
    assert v.is_directory

def test_python_executable_exists(host):
    py = host.file(os.path.join(VENV_DIR, "bin", "python"))
    assert py.exists
    assert py.is_file

def test_requirements_copied(host):
    req = host.file(os.path.join(APP_DIR, "requirements.txt"))
    assert req.exists
    assert req.is_file

def test_tests_directory_copied(host):
    t = host.file(os.path.join(APP_DIR, "tests"))
    assert t.exists
    assert t.is_directory