altura = float(input("Insira a altura: "))
peso = float(input("Insira o peso: "))

imc = peso / (altura ** 2)

if imc <= 17:
    print("Muito abaixo do peso.")
elif imc < 18.5:
    print("Abaixo do peso.")
elif imc < 25:
    print("Peso normal.")
elif imc < 30:
    print("Acima do peso.")
elif imc < 35:
    print("Obesidade I.")
elif imc < 40:
    print("Obesidade II.")
else:
    print("Obesidade III.")
