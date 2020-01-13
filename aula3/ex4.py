salario = float(input("Insira o salario: "))

if salario <= 1250:
    ir = 0
elif salario <= 1900:
    ir = 11 / 100
elif salario <= 2700:
    ir = 25 / 100
else:
    ir = 27.5 / 100

desconto = salario * ir
salario_total = salario - desconto
salario_total = round(salario_total, 2)

print(f"O valor do desconto do IR é {int(round(ir * 100, 0))}")
print(f"O salario com descontos é R${salario_total:.2f}")
