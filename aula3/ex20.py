n1 = float(input("Insira o valor da primeira nota: "))
n2 = float(input("Insira o valor da segunda nota: "))
n3 = float(input("Insira o valor da terceira nota: "))
n4 = float(input("Insira o valor da quarta nota: "))

md1 = (n1 + n2 + n3 + n4) / 4

if md1 >= 7:
    print("APROVADO.")
else:
    ne = float(input("Insira o valor da nota do exame: "))
    md2 = ne + md1 / 2
    if md2 >= 5:
        print("APROVADO DE EXAME.")
    else:
        print("REPROVADO.")
