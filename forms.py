from wtforms import StringField, DateField, IntegerField,SelectField, SubmitField
from flask_wtf import FlaskForm

class FormularioAluno(FlaskForm):
  listaCurso = [
    ("","Escolha o curso do aluno"),
    ("1","Técnico em Agropecuária"),
    ("2","Técnico em Alimentos"),
    ("3","Técnico em Informática para Internet"),
  ]

  nomeAluno = StringField("Nome:")
  matriculaAluno = IntegerField("Matrícula: ")
  dataNascimento = DateField("Data de Nascimento: ")
  cursoAluno = SelectField("Selecione o curso:", choices=listaCurso)
  enviar = SubmitField("Cadastrar")


class FormularioTurma(FlaskForm):
  listaNiveis = [
    ("", "Escolha o nível do curso"),
    ("1","Ensino Médio/Técnico"),
    ("2", "Ensino Superior"),
    ("3","Pós-Graduação")]
  
  nomeCurso = StringField("Nome Curso:")
  nomeTurma = StringField("Nome Turma:")
  nivel = SelectField("Nível:",choices=listaNiveis)
  submit = SubmitField("Cadastrar")