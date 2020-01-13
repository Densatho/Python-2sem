import math

while True:
        try:
            vel = int(input("Coloque a velocidade: "))
            ang = float(input("Coloque o angulo: "))
            break
        except ValueError:
            print("Não colocou um valor valido\n")

ang = ang * math.pi / 180
alcance = round((vel * vel / 10) * math.sin(2 * ang), 2)

print(f'O alcance é: {alcance:.2f}')
