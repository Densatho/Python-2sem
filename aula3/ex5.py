valor_total = float(input("Insira o valor total de serviços: "))

if valor_total <= 5000:
    iss = 4 / 100
elif valor_total <= 10000:
    iss = 6 / 100
elif valor_total <= 20000:
    iss = 13 / 100
else:
    iss = 16 / 100

imposto = round(valor_total * iss, 2)

print(f"O valor do ISS é R${imposto:.2f}")
