from aluno import AlunoPessoal
from modelando import colorindo_texto

print('Banco de dados')
user = input('User: ')
password = input('Password: ')
database = input('Database: ')
aluno_class = AlunoPessoal(user, password, database)


while True:

    title = colorindo_texto("Manutenção de Alunos - Criar, Atualizar, Pesquisar e Excluir", 'amarelo')

    print(colorindo_texto('-' * len(title), 'amarelo'))
    print(title)
    print(colorindo_texto('-' * len(title), 'amarelo'))
    print()
    print('Selecione uma opção para Alunos:')
    print()
    print('1 - Exibir todos os alunos.')
    print('2 - Adicionar.')
    print('3 - Pesquisar.')
    print('4 - Atualizar.')
    print('5 - Excluir.')
    print('6 - Sair.')
    print()
    choice = input("Entre com o número da opção: ")
    print()

    if choice == "1":
        aluno_class.display_all_alunos()

    elif choice == "2":
        termoins = [input("Prontuário: ").upper(), input("Nome Completo: ").title()]
        paluno = [input('Sexo: ').title(), input('Idade: '), input('Cor de olhos: ').title()]
        aluno_class.add_new_alunos(termoins, paluno)

    elif choice == "3":
        termo = input("Entre com o termo de busca (prontuário, nome, sexo, cor de olhos): ")
        aluno_class.search_alunos(termo)

    elif choice == "4":
        tab = '   '
        aluno_id = input(f'{tab} Informe o id do aluno: ')
        
        while True:            
            print(tab, '-' * len('Selecione uma opção para Adicionar:'))
            print(tab, 'Selecione uma opção para Adicionar:')
            print(tab, '-' * len('Selecione uma opção para Adicionar:'))
            print()
            print(tab, '1 - Trocar Prontuario')
            print(tab, '2 - Trocar nome')
            print(tab, '3 - Trocar Sexo')
            print(tab, '4 - Trocar idade')
            print(tab, '5 - Trocar cor de olhos')
            print(tab, '6 - Sair')
            print()

            escolha = input(f'{tab} ')

            if escolha == '1':
                aluno = (input(f"{tab} Prontuário: ").upper(), aluno_id)
            elif escolha == '2':
                aluno = (input(f"{tab} Nome Completo: ").title(), aluno_id)
            elif escolha == '3':
                aluno = (input(f"{tab} Sexo: ").title(), aluno_id)
            elif escolha == '4':
                aluno = (input(f"{tab} Idade: "), aluno_id)
            elif escolha == '5':
                aluno = (input(f"{tab} Cor de olhos: ").title(), aluno_id)
            elif escolha == '6':
                break
            else:
                print('Opção invalida')
                continue
            
            aluno_class.update_alunos(aluno, escolha)

    elif choice == "5":
        aluno_id = [input("Entre com o idaluno: ")]
        aluno_class.delete_alunos(aluno_id)

    elif choice == "6":
        break

    else:
        print("Opção inválida. Por favor, selecione um número entre 1 e 6.")

    input()

aluno_class.close_connection()
