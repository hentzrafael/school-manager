from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
import sqlite3
from forms import FormularioAluno,FormularioTurma

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config["SECRET_KEY"] = "ansçofihqoe8e297iufbkifhao"


@app.route("/")
def home():
  return render_template("home.html", titulo="Gerenciador Escolar")

@app.route("/cadastrarAluno", methods=['GET',"POST"])
def cadastro():
  formAluno = FormularioAluno()
  if formAluno.validate_on_submit():
    dados= (formAluno.nomeAluno.data,
    formAluno.matriculaAluno.data,
    formAluno.dataNascimento.data,
    formAluno.cursoAluno.data
    )
    try:
      with sqlite3.connect("database.db") as conexao:
        cursor = conexao.cursor()
        sql = """
          INSERT INTO alunos (nome, matricula, data_nascimento, curso) VALUES (?, ?, ?, ?)
        """
        cursor.execute(sql, dados)
        conexao.commit()
        flash("Aluno adicionado","success")
    except sqlite3.Error as erro:
      print("Erro no INSERT: {}".format(erro))
      flash("Erro ao inserir o aluno","danger")    
    finally:
      conexao.close()
  return render_template("cadastro.html", titulo="Cadastro de alunos", form=formAluno)

@app.route("/listaAluno")
def listaAluno():
  try:
    with sqlite3.connect("database.db") as conexao:
        cursor = conexao.cursor()
        sql = """
          SELECT * FROM alunos
        """
        cursor.execute(sql)
        linhas = cursor.fetchall()
  except sqlite3.Error as erro:
      print("Erro no SELECT: {}".format(erro))
  finally:
    conexao.close()
  return render_template("listaAluno.html",titulo="Lista dos Alunos",linhas=linhas)  

@app.route("/cadastrarTurma", methods=['GET',"POST"])
def cadastroTurma():
  formTurma = FormularioTurma()
  if formTurma.validate_on_submit():
    dados= (formTurma.nomeCurso.data,
    formTurma.nomeTurma.data,
    formTurma.nivel.data,
    )
    try:
      with sqlite3.connect("database.db") as conexao:
        cursor = conexao.cursor()
        sql = """
          INSERT INTO turmas (curso, turma, nivel) VALUES (?, ?, ?)
        """
        cursor.execute(sql, dados)
        conexao.commit()
        flash("Turma adicionada","success")
    except sqlite3.Error as erro:
      print("Erro no INSERT: {}".format(erro))
      flash("Erro ao inserir a turma","danger")    
    finally:
      conexao.close()
  return render_template("cadastro.html", titulo="Cadastro Turma", form=formTurma)

@app.route("/listaTurma")
def listaTurma():
  try:
    with sqlite3.connect("database.db") as conexao:
        cursor = conexao.cursor()
        sql = """
          SELECT * FROM turmas
        """
        cursor.execute(sql)
        linhas = cursor.fetchall()
  except sqlite3.Error as erro:
      print("Erro no SELECT: {}".format(erro))
  finally:
    conexao.close()
  return render_template("listaTurma.html",titulo="Lista das Turmas",linhas=linhas)  

if __name__ == "__main__":
  app.run(
    host = "0.0.0.0",
    port=8453,
    debug = True
  )