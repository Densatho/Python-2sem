volume_mensal = float(input("Insira o volume de vendas mensal: "))

if volume_mensal <= 5000:
    comissao = 2 / 100
elif volume_mensal <= 10000:
    comissao = 5 / 100
elif volume_mensal <= 1200:
    comissao = 7 / 100
else:
    comissao = 9 / 100

print(f"O valor da comissão é R${round(comissao * volume_mensal, 2):.2f}")
