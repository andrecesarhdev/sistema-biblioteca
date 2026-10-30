import os
import boto3
from decimal import Decimal
from dotenv import load_dotenv

# Carrega as variáveis do ficheiro .env se estiveres a usá-lo localmente
load_dotenv()

# Conecta ao DynamoDB na região desejada
# (As credenciais da AWS podem vir de variáveis de ambiente ou do arquivo ~/.aws/credentials)
bd = boto3.resource('dynamodb', region_name='sa-east-1')
tabela = bd.Table('Catalogo')

def inserir_item_exemplo():
    try:
        tabela.put_item(
            Item={
                'id': '001',
                'nome': 'Notebook de Exemplo',
                'preco': Decimal('3500.00')  # Obrigatório: boto3 exige Decimal para floats no DynamoDB
            }
        )
        print("Item inserido com sucesso no DynamoDB!")
    except Exception as e:
        print(f"Erro ao inserir dados: {e}")

if __name__ == "__main__":
    inserir_item_exemplo()