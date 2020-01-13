lado1 = float(input("Valor do lado 1: "))
lado2 = float(input("Valor do lado 2: "))
lado3 = float(input("Valor do lado 3: "))

x = True
if lado1 + lado2 < lado3 or lado2 + lado3 < lado1 or lado1 + lado3 < lado2:
    x = False

if x:
    if lado1 == lado2 == lado3:
        print("É Equilátero.")
    elif lado1 == lado2 or lado2 == lado3 or lado1 ==lado3:
        print("É Isósceles.")
    else:
        print("É Escaleno.")
else:
    print("Não forma triangulo.")
