idade = int(input("Insira a idade do nadador: "))

if idade <= 7:
    categoria = "infantil A"
elif idade <= 10:
    categoria = "infantil B"
elif idade <= 13:
    categoria = "juvenil A"
elif idade <= 17:
    categoria = "juvenil B"
else:
    categoria = "senior"

print(f"A categoria do nadador é {categoria}")
