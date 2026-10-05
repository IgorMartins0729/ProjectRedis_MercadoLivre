import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from mymongo.server_api import ServerApi

#Carrega as variaveis do .env
load_dotenv()

uri = os.getenv("MONGODB_URI")

if not uri:
    raise ValueError("A variável MONGODB_URI não foi encontrada no .env")

#Cria a conexão
client = MongoClient(uri, server_api=ServerApi('1'))

# Exporta o banco de dados para ser importado em outros arquivos
db = client.mercadolivre