while True:
        try:
            salario_velho = float(input("Coloque o salario: "))
            break
        except ValueError:
            print("Não colocou um salario valido valida\n")

while True:
        try:
            percentual = float(input("Coloque o percentual: "))
            break
        except ValueError:
            print("Não colocou um percentual valido\n")

percentual /= 100
aumento = salario_velho * percentual
salario_novo = salario_velho + aumento

aumento = round(aumento, 2)
salario_novo = round(salario_novo, 2)

print(f"Teve um aumento de R${aumento} com um salario total de R${salario_novo}")
