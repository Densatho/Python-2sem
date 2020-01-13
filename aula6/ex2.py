alunos = {}
while True:
    nome = input("Coloque o nome:")
    if nome == "": break
    alunos[nome] = [int(input("nota 1: ")),
                    int(input("nota 2: "))]

nome = input("Qual o aluno que deseja ver a media?\n")
print(sum(alunos[nome])/len(alunos[nome]))
