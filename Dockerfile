FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# 1. Cria um usuário comum para não rodar o sistema como administrador (root)
RUN adduser --disabled-password --gecos "" appuser

# 2. Atualiza os programas do Python e força versões seguras para urllib3 e msgpack
RUN pip install --no-cache-dir --upgrade pip setuptools wheel "urllib3>=2.8.0" "msgpack>=1.2.1"

# 3. Copia e instala as dependências do projeto
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copia os arquivos do projeto e ajusta as permissões de acesso
COPY . .
RUN chown -R appuser:appuser /app

# 5. Define a execução sob o usuário comum
USER appuser

EXPOSE 8000

CMD ["python", "app.py"]