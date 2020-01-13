from random import randint

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
        print(f'Nome: {self.first_name} {self.last_name}')

    def greet_user(self):
        print(f'{self.saudacao}')


class UserTDL(User):

    login_attempts = 0

    def __init__(self, fname, lname, rg1, cpf1, saudacao):
        super().__init__(fname, lname, rg1, cpf1, saudacao)

    def describe_user(self):
        super().describe_user()
        print(f'Quantidade de tentativas: {self.login_attempts}')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


nome = input('Nome: ')
unome = input('Ultimo Nome: ')
rg = input('RG: ')
cpf = input('CPF: ')
sauda = input('Saudação: ')
usuario = UserTDL(nome, unome, rg, cpf, sauda)

for i in range(0, randint(10, 100)):
    usuario.increment_login_attempts()

usuario.describe_user()
usuario.reset_login_attempts()
usuario.describe_user()


