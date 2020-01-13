import mysql.connector
import modelando
from mysql.connector import Error, connect


class Conexao:

    def __init__(self, user, password, database):
        self.user = user
        self.password = password
        self.database = database

        try:
            self.connection = mysql.connector.connect(host='localhost', database=self.database, user=user,
                                                      password=self.password, auth_plugin='mysql_native_password')
            print("Testando a conexão...")
            if self.connection.is_connected():
                info = self.connection.get_server_info()
                print("Conectado com sucesso ao Servidor MySQL versão: ", info)

        except Error as e:
            print("Um erro ocorreu durante a conexão com o BD MySQL", e)


class Aluno(Conexao):

    def __init__(self, user, password, database):
        super().__init__(user, password, database)

    def display_all_alunos(self):
        """Método para exibir todos os alunos do BD."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM alunos;")
        records = cursor.fetchall()

        heading = f"Total de alunos registrados no sistema: {cursor.rowcount} alunos."
        print(heading)
        print("-" * len(heading))
        for row in records:
            print(f"ID: {row[0]}")
            print(f"Prontuario: {row[1]}")
            print(f"Nome: {row[2]}\n")

        cursor.close()

    def search_alunos(self, query):
        """Método para selecionar alunos específicos do BD."""

        sql_stmt = f"SELECT * FROM alunos WHERE nomecompleto LIKE '%{query}%' OR prontuario LIKE '%{query}%'"

        cursor = self.connection.cursor()
        cursor.execute(sql_stmt)
        records = cursor.fetchall()

        heading = f"A pesquisa para '{query}' retornou: {cursor.rowcount} linhas."
        print(heading)
        print("-" * len(heading))
        for row in records:
            print(f"ID: {row[0]}")
            print(f"Prontuario: {row[1]}")
            print(f"Nome: {row[2]}\n")

        cursor.close()

    def add_new_alunos(self, aluno):
        """Método para inserir alunos do BD."""
        sql_stmt = "INSERT INTO alunos (prontuario, nomecompleto) VALUES (%s,%s)"

        cursor = self.connection.cursor(prepared=True)
        cursor.execute(sql_stmt, aluno)
        self.connection.commit()
        cursor.close()

    def update_alunos(self, aluno, escolha):

        if escolha == '1':
            sql_stmt = "UPDATE alunos SET prontuario = %s WHERE idaluno = %s"
        elif escolha == '2':
            sql_stmt = "UPDATE alunos SET nomecompleto = %s WHERE idaluno = %s"

        cursor = self.connection.cursor(prepared=True)
        cursor.execute(sql_stmt, aluno)
        self.connection.commit()
        cursor.close()

    def delete_alunos(self, aluno):
        sql_stmt = "DELETE FROM alunos WHERE idaluno = %s"
        cursor = self.connection.cursor(prepared=True)
        cursor.execute(sql_stmt, aluno)
        self.connection.commit()
        cursor.close()

        print("O registro foi excluído com sucesso!")

    def close_connection(self):
        self.connection.close()
        print("A conexão com o BD Mysql foi fechada.")


class AlunoPessoal(Aluno):
    
    def __init__(self, user, password, database):
        super().__init__(user, password, database)
        
    def display_all_alunos(self):
        """Método para exibir todos os alunos do BD."""
        cursor = self.connection.cursor()
        select = """SELECT a.*, p.sexo, p.idade, p.cordeolhos
        FROM alunos a, alunopessoal p
        where a.idaluno = p.idalunopessoal;"""
        cursor.execute(select)
        records = cursor.fetchall()

        heading = f"Total de alunos registrados no sistema: {cursor.rowcount} alunos."
        print(heading)
        print("-" * len(heading))
        for row in records:
            print(f"ID: {row[0]}")
            print(f"Prontuario: {row[1]}")
            print(f"Nome: {row[2]}")
            print(f"Sexo: {row[3]}")
            print(f"Idade: {row[4]}")
            print(f"Cor de olhos: {row[5]}\n")

        cursor.close()

    def search_alunos(self, query):
        """Método para selecionar alunos específicos do BD."""

        sql_stmt = f"""SELECT a.*, p.sexo, p.idade, p.cordeolhos
        FROM alunos a, alunopessoal p
        WHERE (a.nomecompleto LIKE '%{query}%' OR a.prontuario LIKE '%{query}%'
        or p.cordeolhos like '%{query}%' OR p.sexo like '%{query}%') and a.idaluno = p.idalunopessoal;"""

        cursor = self.connection.cursor()
        cursor.execute(sql_stmt)
        records = cursor.fetchall()

        heading = f"A pesquisa para '{query}' retornou: {cursor.rowcount} linhas."
        print(heading)
        print("-" * len(heading))
        for row in records:
            print(f"ID: {row[0]}")
            print(f"Prontuario: {row[1]}")
            print(f"Nome: {row[2]}")
            print(f"Sexo: {row[3]}")
            print(f"Idade: {row[4]}")
            print(f"Cor de olhos: {row[5]}\n")

        cursor.close()

    def add_new_alunos(self, aluno, paluno):
        super().add_new_alunos(aluno)
        
        cursor = self.connection.cursor()
        cursor.execute('select idaluno from alunos order by idaluno desc limit 1;')
        records = cursor.fetchall()
        cursor.close()
        paluno.append(records[0][0])
        
        sql_stmt = 'insert into alunopessoal (sexo, idade, cordeolhos, alunopessoalid) values (%s,%s,%s,%s)'
        
        cursor = self.connection.cursor()
        cursor.execute(sql_stmt, paluno)
        self.connection.commit()
        cursor.close

    def update_alunos(self, aluno, escolha):

        if escolha == '1':
            sql_stmt = "UPDATE alunos SET prontuario = %s WHERE idaluno = %s"
        elif escolha == '2':
            sql_stmt = "UPDATE alunos SET nomecompleto = %s WHERE idaluno = %s"
        elif escolha == '3':
            sql_stmt = "UPDATE alunopessoal SET sexo = %s WHERE alunopessoalid = %s"
        elif escolha == '4':
            sql_stmt = "UPDATE alunopessoal SET idade = %s WHERE alunopessoalid = %s"
        elif escolha == '5':
            sql_stmt = "UPDATE alunopessoal SET cordeolhos = %s WHERE alunopessoalid = %s"
            
        cursor = self.connection.cursor(prepared=True)
        cursor.execute(sql_stmt, aluno)
        self.connection.commit()
        cursor.close()

    def delete_alunos(self, aluno):
        
        sql_stmt = "DELETE FROM alunopessoal WHERE alunopessoalid = %s"
        cursor = self.connection.cursor(prepared=True)
        cursor.execute(sql_stmt, aluno)
        
        self.connection.commit()
        cursor.close()
        
        super().delete_alunos(aluno)

        # print("O registro pessoal do aluno foi excluído com sucesso!")

    def close_connection(self):
        super().close_connection()
    