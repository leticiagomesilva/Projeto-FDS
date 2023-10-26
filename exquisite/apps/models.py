from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    sobrenome = models.TextField(max_length=255)
    pontos = models.IntegerField()


class AvaliacaoPergunta(models.Model):
    avaliacao = models.CharField(max_length=10, choices=[('facil', 'Fácil'), ('medio', 'Médio'), ('dificil', 'Difícil')])


class PerguntasBD(models.Model):
    id_pergunta = models.AutoField(primary_key=True)
    materia = models.TextField(max_length=255)
    titulo = models.TextField(max_length=255)
    pergunta = models.TextField(max_length=1500)
    resposta = models.TextField(max_length=1500)