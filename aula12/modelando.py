import os


def confirma_save(nome, extensao, quantidade):
    """
    :param nome: nome do arquivo
    :param extensao: Extensão do arquivo
    :param quantidade: quantidades de arquivos
    :return: sem retorno
    """
    for i in range(0, quantidade):
        try:
            with open(nome + str(i+1) + extensao):
                pass
        except FileNotFoundError:
            open(nome + str(i+1) + extensao, 'w')


def colorindo_texto(texto, cor):
    """

    :param texto: um texto
    :param cor: seleciona a cor do texto | Vermelho | Verde | Amarelo | Azul | Magenta | Cyan | Cinza
    :return: retorna o texto com a cor selecionado
    """
    cor = cor.capitalize()
    if cor == 'Vermelho':
        return '\033[1;31m' + texto + '\033[m'
    elif cor == 'Verde':
        return '\033[1;32m' + texto + '\033[m'
    elif cor == 'Amarelo':
        return '\033[1;33m' + texto + '\033[m'
    if cor == 'Azul':
        return '\033[1;34m' + texto + '\033[m'
    elif cor == 'Magenta':
        return '\033[1;35m' + texto + '\033[m'
    elif cor == 'Cyan':
        return '\033[1;36m' + texto + '\033[m'
    if cor == 'Cinza':
        return '\033[1;37m' + texto + '\033[m'


# confirma_save('save', '.svt', 1)

#
# texto = open('text.txt', 'r')
# x = texto.readlines()
# x[0].find('va')
# find_work(texto, 'va a merda')
# for linha in texto:
#     linha.find(palavra)
