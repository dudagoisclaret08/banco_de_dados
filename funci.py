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

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

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

print("Alunos da turma 'B' com nota maior ou igual a 7:")
cursor.execute("SELECT * FROM alunos WHERE turma = 'B' AND nota >= 7")
for aluno in cursor.fetchall():
    print(aluno)


conn.close()




###atvdd3
import sqlite3

conn = sqlite3.connect('loja.db')
cursor = conn.cursor()

print("Produto e cliente de todas as vendas:")
cursor.execute("SELECT produto, cliente FROM vendas")
for produto, cliente in cursor.fetchall():
    print(f"Produto: {produto}, Cliente: {cliente}")

print("\n")

print('Vendas realizadas pelo cliente "João":')
cursor.execute("SELECT * FROM vendas WHERE cliente = 'João'")
vendas = cursor.fetchall()
if vendas:
    for venda in vendas:
        print(venda)
else:
    print("Nenhuma venda encontrada para o cliente João.")

print("\n")

print("Produtos com preço unitário maior que 50:")
cursor.execute("SELECT produto FROM vendas WHERE preco_unitario > 50")
produtos = cursor.fetchall()
for (produto,) in produtos:
    print(produto)


conn.close()



##atvdd4  
import sqlite3

conn = sqlite3.connect('cinema.db')
cursor = conn.cursor()

print("Títulos e gêneros de todos os filmes:")
cursor.execute("SELECT titulo, genero FROM filmes")
for titulo, genero in cursor.fetchall():
    print(f"Título: {titulo}, Gênero: {genero}")

print("\n")

print('Dados do filme "Matrix":')
cursor.execute("SELECT * FROM filmes WHERE titulo = 'Matrix'")
filme = cursor.fetchone()
if filme:
    print(filme)
else:
    print("Filme 'Matrix' não encontrado.")

print("\n")

print("Títulos e avaliações dos filmes lançados após 2010:")
cursor.execute("SELECT titulo, avaliacao FROM filmes WHERE ano > 2010")
for titulo, avaliacao in cursor.fetchall():
    print(f"Título: {titulo}, Avaliação: {avaliacao}")


conn.close()




