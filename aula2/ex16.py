while True:
        try:
            x = [float(input("Coloque o 1º valor: "))]
            for i in range(0, 4):
                x.append(float(input(f"Coloque o {i+2}º valor: ")))

            break
        except ValueError:
            print("Não colocou um valor valido\n")

aux = 0
for i in range(0, len(x)):
    aux += x[i]

media = round(aux / len(x), 1)

print(f'Media: {media}')
