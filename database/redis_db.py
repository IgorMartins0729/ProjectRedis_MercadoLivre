import os
import redis 
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("REDIS_HOST","localhost")
port = int(os.getenv("REDIS_PORT",6379))
password = os.getenv("REDIS_PASSWORD", "")

#Conexão com o Redis
# decode_responses=True transforma os bytes retornados pelo Redis em strings limpas no Python
redis_client = redis.Redis(
    host =host,
    port=port,
    password=password,
    decode_responses=True
)