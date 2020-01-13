while True:
        try:
            n1 = float(input("Coloque o primeiro valor: "))
            n2 = float(input("Coloque o segundo valor: "))
            break
        except ValueError:
            print("Não colocou um valor valido\n")


soma = round(n1 + n2, 2)
subtracao = round(n1 - n2, 2)
multiplicacao = round(n1 * n2, 2)
divisao = round(n1 / n2, 2)
resto = round(n1 % n2, 2)
potencia = round(n1 ** n2, 2)
raiz = round(n1 ** (1/n2), 2)

print(f'Soma: {soma:.2f}')
print(f'Subtração: {subtracao:.2f}')
print(f'Multiplicação: {multiplicacao:.2f}')
print(f'Divisão: {divisao:.2f}')
print(f'Resto da divisão: {resto:.2f}')
print(f'Exponenciação: {potencia:.2f}')
print(f'Radiciação: {raiz:.2f}')
