nome = ("admin")
senha = 1234
input_nome = input("Digite seu nome de usuário: ")
input_senha = int(input("Digite sua senha: "))
if input_nome == nome :
    print("Usuário encontrado.")
    if input_senha == senha:
        print("Login realizado com sucesso.")
    else :
        print("Senha incorreta.")
else :
    negado = print("Acesso negado.")