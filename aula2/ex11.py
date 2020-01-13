while True:
        try:
            qnt = float(input("Coloque a quantidade de quilowatts: "))
            salario_minimo = float(input("Coloque o valor do salario minimo: "))
            break
        except ValueError:
            print("Não colocou um valor valido\n")

valor_por_kw = round((salario_minimo / 7) / 100)
valor_kw = round(qnt * valor_por_kw)
valor_total = round(valor_kw * 0.9)

print(f'Valor por quilowatt: R${valor_por_kw:.2f}')
print(f'Valor a ser pago sem descontos: R${valor_kw:.2f}')
print(f'Valor a ser pago com descontos: R${valor_total:.2f}')
