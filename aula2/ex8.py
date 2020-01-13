while True:
        try:
            horas = float(input("Coloque a quantidade de horas trabalhadas: "))
            salario_minimo = float(input("Coloque o valor do salario minimo: "))
            break
        except ValueError:
            print("Não colocou um valor valido\n")

hora_trabalhada = salario_minimo / 2
salario_bruto = round(hora_trabalhada * horas, 2)
imposto = round(salario_bruto * 0.3, 2)
salario = round(salario_bruto - imposto, 2)

print(f'O salario bruto é R${salario_bruto:.2f}, o imposto é R${imposto:.2f} e o salario é de R${salario:.2f}.')
