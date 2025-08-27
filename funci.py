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





