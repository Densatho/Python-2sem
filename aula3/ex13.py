n1, n2 = input("Insira dois numeros: ").split(' ')
n1, n2 = float(n1), float(n2)

op = input("Qual operação deseja realizar? <+> <-> <*> </>\n")
r = {'+': n1+n2, '-': n1-n2, '*': n1*n2, '/': n1/n2}[op]

round(r, 2)
print(f"O resultado é {r:.2f}")
