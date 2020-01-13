resposta1 = input(f"Resposta da questão 1: ")
resposta2 = input(f"Resposta da questão 2: ")
resposta3 = input(f"Resposta da questão 3: ")
gabarito1 = input(f"Gabarito questão 1}: ")
gabarito2 = input(f"Gabarito questão 2: ")
gabarito3 = input(f"Gabarito questão 3: ")


acertos = 0
if resposta1 == gabarito1:
    acertos += 1
if resposta2 == gabarito2:
    acertos += 1
if resposta3 == gabarito3:
    acertos += 1

print(f"Acertou {acertos} questões.")
