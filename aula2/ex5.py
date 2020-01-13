while True:
        try:
            numero = float(input("Coloque um numero positivo e maior que zero: "))
            if numero <= 0:
                print("Não colocou um valor valido\n")
                pass
            else:
                break
        except ValueError:
            print("Não colocou um valor valido\n")

numero = round(numero, 2)
quadrado = round(numero ** 2, 2)
cubo = round(numero ** 3, 2)
raiz_quadrada = round(numero ** (1/2), 2)
raiz_cubica = round(numero ** (1/3), 2)
soma = round(quadrado + cubo, 2)

print(f'O numero {numero} tem os seguintes resultados:')
print(f'\t{numero} ao quadrado é {quadrado};')
print(f'\t{numero} ao cubo é {cubo};')
print(f'\tRaiz quadrada do {numero} é {raiz_quadrada};')
print(f'\tRaiz cubica do {numero} é {raiz_cubica};')
print(f'\tA soma do quadrado com o cubo do {numero} é {soma}.')
