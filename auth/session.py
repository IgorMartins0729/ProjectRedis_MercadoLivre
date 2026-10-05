from database.redis_db import redis_client

def realizar_login():
    #Dados hardcoded
    email = 'vinicius@gmail.com'
    nome = 'Vinicius da Silva'

    print(f"A iniciar sessão automaticamente para: {email}...")

    # Guarda o utilizador no Redis com a função expire (ex=60 define 60 segundos)
    redis_cliente.set("usuario_atual",email, ex=60)

    print("Login efetuado com sucesso! Sessão temporária de 60 segundos iniciada.")
    return True

def verificar_sessao():
    email_atual = redis_client.get("usuario_atual")


    # Verifica se o email atual está registrado e se a sessão ainda não expirou
    if email_atual and redis_client.exists(email_atual):
        tempo_restante = redis_client.ttl(email_atual)
        nome = redis_client.get(email_atual)
        print(f"\n[SESSÃO ATIVA] {nome} | Expira em: {tempo_restante}")
        return True
    else:
        print("\[ACESSO NEGADO] Sessão expirada. Efetue o login (Opção 0) para continuar.")
        return False