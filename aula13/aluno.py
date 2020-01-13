class Aluno:

    def __init__(self, prontuario, nome):
        self.pronturario = prontuario
        self.nome = nome

    def exibir(self):
        print(f"Prontuário: {self.pronturario}")
        print(f"Nome Completo: {self.nome}")


novo_aluno = Aluno(input('Prontuario: '), input('Nome Completo: '))

novo_aluno.exibir()
