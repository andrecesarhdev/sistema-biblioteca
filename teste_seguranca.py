import subprocess

def executar_comando_inseguro(comando_usuario):
    subprocess.call(comando_usuario, shell=True)