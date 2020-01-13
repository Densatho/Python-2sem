class Restaurant:

    def __init__(self, nome, tipo):
        self.restaurant_name = nome
        self.cuisine_type = tipo

    def describe_restaurant(self):
        print(f'Nome do Restaurante: {self.restaurant_name}')
        print(f'Estilo da culinaria: {self.cuisine_type}')

    def open_restaurant(self):
        print(f'O restaurante {self.restaurant_name} esta aberto.')


class Rest(Restaurant):
    def __init__(self, nome, tipo, number_serverd=0):
        super().__init__(nome, tipo)
        self.number_serverd = number_serverd

    def describe_restaurant(self):
        super().describe_restaurant()
        print(f'Quantidade de clientes atendidos: {self.number_serverd}')

    def set_number_serverd(self, qnt):
        self.number_serverd = qnt

    def incriment_number_serverd(self, qnt):
        self.number_serverd += qnt
        print(f'A quantidade de clientes atendidos é {qnt}')


nom = input('Nome: ')
tip = input('Culinaria: ')
restaurant = Rest(nom, tip)
restaurant.describe_restaurant()
print()

while True:
    print('Escolha uma opção')
    print('1 - Definir quantidade de clientes servidos')
    print('2 - Incrementar quantidade de clientes servidos')
    print('3 - Sair')
    opc = input()
    if opc == '1':
        qnt = int(input('Quantas pessoas foram atendidas: '))
        restaurant.set_number_serverd(qnt)
        restaurant.describe_restaurant()
    elif opc == '2':
        qnt = int(input('Quantas pessoas atendidas deseja incrementar: '))
        restaurant.incriment_number_serverd(qnt)
        restaurant.describe_restaurant()
    elif opc == '3':
        break


restaurant.describe_restaurant()
restaurant.open_restaurant()
