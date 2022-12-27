PASSWORD = 8857
USER_ID = 84837


def validaAcesso(userId, password):
    if userId != USER_ID:
        return 'Usuario invalido!'
    if password != PASSWORD:
        return 'senha incorreta'
    return 'acesso permitido'


userId = int(input())
password = int(input())
print(f"""
Código: {userId}
Senha: {password}
Saída: {validaAcesso(userId, password)}
""")