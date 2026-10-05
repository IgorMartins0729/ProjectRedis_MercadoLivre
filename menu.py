import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_env = os.path.join(diretorio_atual, "atlas-credentials.env")

# Carrega o arquivo
load_dotenv(caminho_env)

uri = os.getenv("MONGODB_URI")
print("Testando a URI:", uri)

client = MongoClient(uri, server_api=ServerApi('1'))
global db
db = client.mercadolivre

#===========================================================
#===========================================================

