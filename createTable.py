import sqlite3


conexao = sqlite3.connect("database.db")

sql = """
  CREATE TABLE IF NOT EXISTS turmas (
    id integer PRIMARY KEY,
    curso text NOT NULL,
    turma text NOT NULL,
    nivel integer NOT NULL
  );

"""

sql2 = """
  CREATE TABLE IF NOT EXISTS alunos (
    id integer PRIMARY KEY,
    nome text NOT NULL,
    matricula text NOT NULL,
    data_nascimento integer NOT NULL,
    curso integer NOT NULL

  );
"""

conexao.execute(sql2)
conexao.close()