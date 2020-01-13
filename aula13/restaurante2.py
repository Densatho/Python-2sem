class Restaurant:

    def __init__(self, nome, tipo, hora, horaf, freezer, principal):
        self.restaurant_name = nome
        self.cuisine_type = tipo

        self.horario_de_abertura = hora
        self.horario_de_fechamento = horaf
        self.estado_do_freezer = freezer
        self.prato_principal = principal


    def describe_restaurant(self):
        print(f'Nome do Restaurante: {self.restaurant_name}')
        print(f'Estilo da culinaria: {self.cuisine_type}')
        print(f'Hora de abertura: {self.horario_de_abertura}')
        print(f'Hora de Fechamento: {self.horario_de_fechamento}')
        print(f'Prato principal: {self.prato_principal}')

    def open_restaurant(self, hora):
        if self.horario_de_abertura <= hora <= self.horario_de_fechamento:
            print(f'O restaurante esta aberto.')
        else:
            print('Restaurante esta fechado.')


nom = input('Nome: ')
tip = input('Culinaria: ')
hor = float(input('Abertura(exemplo: 12.30): '))
horf = float(input('Fechamento(exemplo: 12.30): '))
free = input('Freezer esta: ')
pp = input('Prato principal: ')
rest = Restaurant(nom, tip, hor, horf, free, pp)
rest.describe_restaurant()
rest.open_restaurant(float(input('Hora(exemplo: 12.30): ')))
