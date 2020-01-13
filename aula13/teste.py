from random import randint

def monster(tipo, nv):
    if tipo == 1:
        return Slime(nv)
    elif tipo == 2:
        return Dragon(nv)

class Slime:
    def __init__(self, nv):
        self.nv = nv
        self.nome = 'Slime Nv' + str(self.nv)
        self.vida = 15 + 3 * self.nv
        self.atq = 5 + 1 * self.nv
        self.defe = 2 + 1 * self.nv

    def status(self):
        print(f'{self.nome}')
        print(f'{self.vida}')
        print(f'{self.atq}')
        print(f'{self.defe}')

class Dragon:
    def __init__(self, nv):
        self.nv = nv
        self.nome = 'Dragon Nv' + str(self.nv)
        self.vida = 15 + 100 * self.nv
        self.atq = 5 + 100 * self.nv
        self.defe = 2 + 100 * self.nv

    def status(self):
        print(f'{self.nome}')
        print(f'{self.vida}')
        print(f'{self.atq}')
        print(f'{self.defe}')

monstro = monster(randint(1,2), randint(0, 100))
monstro.status()
