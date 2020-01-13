valor = float(input("Insira o valor total: "))

if valor <= 100:
    parcelas = 2
elif valor <= 200:
    parcelas = 3
elif valor <= 400:
    parcelas = 4
else:
    parcelas = 5

valor_per_parcela = round(valor / parcelas, 2)

print(f"O valor de juros é R${valor_per_parcela:.2f}")
