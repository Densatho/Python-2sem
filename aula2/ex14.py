while True:
        try:
            while True:
                faces = int(input("Coloque o numero de faces: "))
                if faces > 0:
                    break
                else:
                    print("Não colocou um valor valido\n")

            while True:
                arestas = int(input("Coloque o numero de arestas: "))
                if arestas > 0:
                    break
                else:
                    print("Não colocou um valor valido\n")
            break
        except ValueError:
            print("Não colocou um valor valido\n")

vertices = arestas + 2 - faces

print(f'O numero de vértices: {vertices}')
