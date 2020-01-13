while True:
        try:
            x = int(input("Coloque o valor de x: "))
            y = int(input("Coloque o valor de y: "))
            break
        except ValueError:
            print("Não colocou um valor valido\n")

aux = x
x = y
y = aux

print(f'O valor de x é {x} e o de y é {y}')
