def autentica(login: str, senha: str) -> bool:
    if login == "admin" and senha == "123":
        return True
    else:
        return False


chances = 3

for i in range(1, chances+1):
    usuario = input("Usuário: ")
    senhas = input("Senha: ")
    Validador = autentica(usuario, senhas)
    if Validador:
        print("Login Realizado!")
        break
    else:
        print("Falha no login")
