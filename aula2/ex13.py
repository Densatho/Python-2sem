while True:
        try:
            n = int(input("Coloque o numero de lados do poligono: "))
            break
        except ValueError:
            print("Não colocou um valor valido\n")

diagonais = int((n * (n - 3)) / 2)

print(f'O numero de diagonais: {diagonais}')
