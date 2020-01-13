while True:
        try:
            valor_hora_aula = float(input("Coloque o valor da hora aula: "))
            aulas_mes = float(input("Coloque a quantidade de aulas dadas no mês: "))
            inss = float(input("Coloque o percentual de desconto do INSS: "))
            break
        except ValueError:
            print("Não colocou um valor valido\n")

inss = inss/100
salario = round(valor_hora_aula * aulas_mes - (inss * valor_hora_aula * aulas_mes), 2)

print(f'Valor a receber será: R${salario:.2f}')
