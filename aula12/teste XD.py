# arq = open('arq2.txt', 'a')
# arq.write("Dennis \"Densatho\" Santos Jacintho XD\n")
# arq.close()


arq = open('arq2.txt')
texto = arq.readlines()

for linha in texto:
    print(linha.strip())

aux = []

for i in range(0, len(texto)):
    for j in range(0, len(texto)):
        if texto[i] != texto[j]:
            aux.append(i)
            break


for i in aux[:]:
    texto.pop(i)
    break

for linha in texto:
    print(linha.strip())


