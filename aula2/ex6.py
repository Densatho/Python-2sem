while True:
        try:
            pes = float(input("Coloque um numero positivo e maior que zero: "))
            break
        except ValueError:
            print("Não colocou um valor valido\n")

pes = round(pes, 2)
metros = round(pes / 3.281, 2)

print(f'O numero em pes {pes} é {metros} em metros.')
