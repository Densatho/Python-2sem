while True:
        try:
            valor = float(input("Coloque o valor: "))
            taxa = float(input("Coloque a taxa: "))
            tempo = int(input("Coloque o tempo: "))
            break
        except ValueError:
            print("Não colocou um valor valido\n")

taxa /= 100
prestacao = round(valor + (valor * (valor / 100) * tempo), 2)

print(f'A prestação é: {prestacao:.2f}')
