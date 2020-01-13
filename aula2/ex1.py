nota = []
for i in range(0,3):
    while True:
        try:
            nota.append(float(input(f"Coloque a nota {i+1}: ")))
            break
        except ValueError:
            print("Não colocou uma nota valida\n")

media = 0
x = ''
for i in range(0, len(nota)):
    x += f'A nota {i+1} é {nota[i]}, '
    media += nota[i]

media = media/len(nota)

print(x, f'Media é {media}')
