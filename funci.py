import sqlite3 as funcionarios

banco = funcionarios.connect('empresa.db')

cursor = banco.cursor()

##busca as informaçôes pedidas ##fetchall (ele busca todas as informaçôes) ##for pega cada resposta 
cursor.execute("SELECT nome, salario FROM funcionarios")
for nome, salario in cursor.fetchall():
    print(f"Nome: {nome}, Salário: {salario}")

## usamos o WHERE para escolher só as informações que eu pedir ##usamos o if para ver se tem a informação 
cursor.execute("SELECT * FROM funcionarios WHERE nome = 'Carla'")
dados = cursor.fetchall()
if dados:
    for linha in dados:
        print(linha)
else:
    print("Funcionária Carla não encontrada.")

# in = um dos jeito de coletar cada informação ### faz a analise de todas as linha para dar as informações
cursor.execute("SELECT nome, cargo FROM funcionarios WHERE departamento = 'TI'")
for nome, cargo in cursor.fetchall():
    print(f"Nome: {nome}, Cargo: {cargo}")


banco.close()


#### atvdd 2

import sqlite3

# Conecta no banco escola.db
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# 1. Listar nome e nota de todos os alunos
print("Nome e nota de todos os alunos:")
cursor.execute("SELECT nome, nota FROM alunos")
for nome, nota in cursor.fetchall():
    print(f"Nome: {nome}, Nota: {nota}")

print("\n")

2. Selecionar apenas o aluno cujo id = 3
print("Dados do aluno com id = 3:")
cursor.execute("SELECT * FROM alunos WHERE id = 3")
aluno = cursor.fetchone()
if aluno:
    print(aluno)
else:
    print("Aluno com id = 3 não encontrado.")

print("\n")

# 3. Exibir alunos da turma 'B' com nota >= 7
print("Alunos da turma 'B' com nota maior ou igual a 7:")
cursor.execute("SELECT * FROM alunos WHERE turma = 'B' AND nota >= 7")
for aluno in cursor.fetchall():
    print(aluno)


conn.close()






