nota = []
peso = []
for i in range(0,3):
    while True:
        try:
            x1, x2 = input(f"Coloque a nota {i+1} e o seu peso: ").split(', ')
            x1, x2 = float(x1), float(x2)
            nota.append(x1)
            peso.append(x2)
            break
        except ValueError:
            print("Não colocou uma nota valida\n")

media = 0
x = ''
for i in range(0, len(nota)):
    if i != len(nota)-1:
        x += f'A nota {i+1} é {nota[i]} e o peso dela é {peso[i]}, '
    else:
        x += f'A nota {i+1} é {nota[i]} e o peso dela é {peso[i]}'
    media += nota[i]*peso[i]/10

print(f'{x}\nMedia é {media:2.2}')
