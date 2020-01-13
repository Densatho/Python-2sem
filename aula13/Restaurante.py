class Restaurant:

    def __init__(self, nome, tipo):
        self.restaurant_name = nome
        self.cuisine_type = tipo

    def describe_restaurant(self):
        print(f'Nome do Restaurante: {self.restaurant_name}')
        print(f'Estilo da culinaria: {self.cuisine_type}')

    def open_restaurant(self):
        print(f'O restaurante esta aberto.')


pe_de_fava = Restaurant(input('Nome: '), input('Culinaria: '))
pe_de_fava.describe_restaurant()
pe_de_fava.open_restaurant()
