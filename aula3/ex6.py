compra = float(input("Insira o valor da compra: "))

if compra <= 50:
    desconto = 5 / 100
elif compra <= 100:
    desconto = 8 / 100
elif compra <= 150:
    desconto = 12 / 100
else:
    desconto = 15 / 100

desconto_total = round(compra * desconto, 2)

print(f"O valor de desconto é R${desconto_total:.2f}")
