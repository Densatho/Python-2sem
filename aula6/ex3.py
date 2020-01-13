corredores = {}
aux = 0

for i in range(0 , 3):

    nome = input("Insira o nome do corredor: ")
    tempo = []
    for j in range(0, 5):
        aux = int(input(f"Coloque o {j+1}ª volta: "))
        tempo.append(aux)

    corredores[nome] = tempo

aux = 65
aux1 = 0
for i in corredores:
    for j in corredores[i]:
        if aux > j:
            aux = j
            aux1 = i

print(f"O corredor foi o {aux1} teve o tempo {aux} segundos na volta {corredores[aux1].index(aux)+1}")

media = []
aux2 = 0
for i in corredores:
    media.append([sum(corredores.get(i))/len(corredores.get(i)), i])

media.sort()
print()
for i in range(len(media)):
    print(f"O {i+1}º lugar foi o {media[i][1]} com a media de tempo de {media[i][0]}\n")
