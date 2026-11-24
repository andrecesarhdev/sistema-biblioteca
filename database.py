import os
import logging
import boto3
from botocore.exceptions import EndpointConnectionError
from decimal import Decimal
from dotenv import load_dotenv

from biblioteca.logs import configurar_logging

log= logging.getLogger("banco")
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
        log.info("Item inserido com sucesso no DynamoDB (id=001)")
    except EndpointConnectionError:
        log.error("Falha de conexão com o DynamoDB (EndpointConnectionError)")
    except Exception as e:
        log.error("Falha ao inserir dados no DynamoDB (%s)", type(e).__name__)

if __name__ == "__main__":
    configurar_logging()
    inserir_item_exemplo()