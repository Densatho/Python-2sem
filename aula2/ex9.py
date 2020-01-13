while True:
        try:
            deposito = float(input("Coloque o valor do deposito: "))
            break
        except ValueError:
            print("Não colocou um valor valido\n")

for i in range(0 , 2):
    while True:
        try:
            cheque = float(input("Coloque o valor do cheque: "))

            aux = cheque * 0.38
            deposito -= (aux + cheque)
            break
        except ValueError:
            print("Não colocou um valor valido\n")
deposito = round(deposito)

print(f'O saldo atual é R${deposito:.2f}')
