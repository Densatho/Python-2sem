custo = float(input("Insira o custo: "))
print("#" * 60)
codigo = int(input("Insira o codigo"
                   "\n1 - cesta basica"
                   "\n2 - Eletrônica"
                   "\n3 - Serviços"
                   "\n4 - Os demais produtos\n"))

print("#" * 60)

if codigo == 1:
    icms = 0
elif codigo == 2:
    icms = 25 / 100
elif codigo == 3:
    icms = 18 / 100
else:
    icms = 12 / 100

print(f"O valor do imposto é R${round(icms * custo, 2):.2f}")
