a = int(input("Insira o valor de A: "))
b = int(input("Insira o valor de B: "))

if a > b:
    print(f"A diferença de A para B é {a - b}")
elif b > a:
    print(f"A diferença de B para A é {b - a}")
else:
    print("Os dois tem o mesmo valor e a diferença é zero.")
