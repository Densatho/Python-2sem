txt = input("Escreva o texto.\n")

a = txt.count('a') + txt.count('A')
i = txt.count('i') + txt.count('I')
u = txt.count('u') + txt.count('U')
e = txt.count('e') + txt.count('E')
o = txt.count('o') + txt.count('O')

dic = {"A": a, "I": i, "U": u, "E": e, "O": o}

print(dic)
