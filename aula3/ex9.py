valor = float(input("Insira o valor da compra: "))

if valor <= 150:
    desconto = 5 / 100
elif valor <= 300:
    desconto = 7 / 100
elif valor <= 500:
    desconto = 10 / 100
else:
    desconto = 20 / 100

valor_desconto = round(valor * desconto, 2)

print(f"O valor de desconto é R${valor_desconto:.2f}")
