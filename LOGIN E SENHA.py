usuario = []
senha = []

while True:
    print('escolha uma das opções abaixo: \n ')
    resposta = int(input(' 1 - Login \n 2 - Resgistrar \n 3 - Sair \n'))

    if resposta == 2:
        while True:
             user = input("Novo usuario: ")
             for i in usuario[:]:
                if user == usuario:
                    pass
             senhac = input("Senha: ")
             if senhac == input("Confirme sua senha: "):
                break

        usuario.append(user)
        senha.append(senhac)
        print('Usuário registrado com sucesso!')
    if resposta == 1:
        while True:
            # Login
            print("           Login           ")

            while True:
                teste = False
                log = input("User: ")
                for i in usuario[:]:
                    if log == i:
                        aux = usuario.index(log)
                        teste = True
                if teste:
                    break

            if senha[aux] == input("senha: "):
                print(f"Logado como {usuario[aux]}")
                break


    if resposta == 3:
        exit(void)
