while True:
        try:
            tempo = float(input("Coloque o tempo(em minutos) que o objeto levou para chegar: "))
            km = float(input("Coloque a distância(em km): "))
            break
        except ValueError:
            print("Não colocou um valor valido\n")

metro = 1000 * km
segundos = tempo * 60
metrops = round(metro / segundos, 2)

print(f'O projétil teve a velocidade de {metrops} m/s.')
