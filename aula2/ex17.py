while True:
        try:
            valor = int(input("Coloque um valor inteiro: "))
            break
        except ValueError:
            print("Não colocou um valor valido\n")

nota50 = valor // 50
aux = valor % 50
nota10 = aux // 10
nota1 = aux % 1

print(f'Notas de 50: {nota50}')
print(f'Notas de 10: {nota10}')
print(f'Notas de 1: {nota1}')
