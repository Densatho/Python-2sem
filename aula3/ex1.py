salario = float(input("Insira o salario: "))

if salario <= 600:
    inss = 7 / 100
elif salario <= 800:
    inss = 8 / 100
elif salario <= 1200:
    inss = 9/100
else:
    inss = 11 / 100

desconto = salario * inss
salario_total = salario - desconto
salario_total = round(salario_total, 2)

print(f"O valor do desconto do INSS é {int(round(inss * 100, 0))}")
print(f"O salario com descontos é R${salario_total:.2f}")
