from pprint import pprint
from modelando import colorindo_texto

arq = open('arq3.txt')
texto = arq.readlines()
arq.close()

aux = []
for linhas in texto:
    aux.append(linhas.strip().split())

for i in range(0, len(aux)):
    for j in range(0, len(aux[i])):
        try:
            aux[i][j] = int(aux[i][j])
        except ValueError:
            pass

for i in range(0, len(aux)):
    media = (aux[i][1] + aux[i][2]) / 2
    aux[i].append(media)

mediatotal = 0

for i in range(0, len(aux)):
    mediatotal += aux[i][3]

mediatotal /= len(aux)

for i in range(0, len(aux)):
    if aux[i][3] > round(mediatotal, 2):
        aux[i].append('É maior que a media da turma')
    else:
        aux[i].append('Não é maior que a media da turma')

for i in aux:
    print(f"Aluna: {colorindo_texto(str(i[0]), 'azul')}")
    if i[1] > 6:
        print(f"nota: {colorindo_texto(str(i[1]), 'verde')}")
    else:
        print(f"nota: {colorindo_texto(str(i[1]), 'vermelho')}")
    if i[2] > 6:
        print(f"nota: {colorindo_texto(str(i[2]), 'verde')}")
    else:
        print(f"nota: {colorindo_texto(str(i[2]), 'vermelho')}")
    if i[3] > 6:
        print(f"nota media: {colorindo_texto(str(i[3]), 'verde')}")
    else:
        print(f"nota media: {colorindo_texto(str(i[3]), 'vermelho')}")
    print(f"{i[4]}")
    print("-" * 15)
print(round(mediatotal, 2))
