pin= 1234
senha = ""
while pin != senha:
    senha = int(input("Digite a senha: "))
    if senha == pin:
        print("acesso permitido")
    else:
        print("senha incorreta")
