valor = float(input("Insira o valor do emprestimo: "))
parcelas = int(input("Insira a quantidade de parcelas: "))

if parcelas <= 3:
    juros = 6 / 100
elif parcelas <= 6:
    juros = 9 / 100
elif parcelas <= 12:
    juros = 22 / 100
else:
    juros = 34 / 100

juros_total = round(valor * juros, 2)

print(f"O valor de juros é R${juros_total:.2f}")
