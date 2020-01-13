class User:

    def __init__(self, fname, lname, rg1, cpf1, saudacao):
        self.first_name = fname
        self.last_name = lname
        self.rg = rg1
        self.cpf = cpf1
        self.saudacao = saudacao

    def describe_user(self):
        print(f'RG: {self.rg}')
        print(f'CPF: {self.cpf}')
        print(f'Name: {self.first_name} {self.last_name}')

    def greet_user(self):
        print(f'{self.saudacao}')


usuario = []
while True:
    nome = input('Nome: ')
    if nome == '':
        break
    unome = input('Ultimo Nome: ')
    rg = input('RG: ')
    cpf = input('CPF: ')
    sauda = input('Saudação: ')
    usuario.append(User(nome, unome, rg, cpf, sauda))

for i in range(0, len(usuario)):
    usuario[i].describe_user()
    usuario[i].greet_user()



