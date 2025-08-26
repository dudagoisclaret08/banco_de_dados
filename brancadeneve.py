import sqlite3

banco = sqlite3.connect('banco.db')

cursor = banco.cursor()

# cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text,'sala de aula text','escola text')")

cursor.execute(" INSERT INTO pessoas VALUES('Davi','10','daviclaret@gmail.com','azul','chácara')")

banco.commit()

cursor.execute("select * fron pessoas ")
print(cursor.fetchall())



