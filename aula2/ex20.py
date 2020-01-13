import math

while True:
        try:
            raio = float(input("Coloque o raio da circunferência: "))
            break
        except ValueError:
            print("Não colocou um valor valido\n")


area = round(math.pi * (raio ** 2), 2)
perimetro = round(math.pi * raio * 2, 2)

print(f'A area é: {area:.2f}')
print(f'o perimetro é: {perimetro:.2f}')
