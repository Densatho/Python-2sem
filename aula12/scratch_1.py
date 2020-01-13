from pprint import pprint

arq = open("arq2.txt")
palavras = []
for linha in arq:
    linha = linha.strip()
    palavras.append(linha)

pprint(palavras)
arq.close()
