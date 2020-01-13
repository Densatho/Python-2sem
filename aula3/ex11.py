n = int(input("Insira um numero: "))

if n < 0:
    categoria = "Negativo"
elif n == 0:
    categoria = "Zero"
else:
    categoria = "Positivo"

print(f"O numero é {categoria}")
