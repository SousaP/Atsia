from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length = 200)
	body = models.TextField()
	date = models.DateTimeField()
	photo_img = models.ImageField(upload_to = "static/img/blog/", default='static/img/logo_atsia.jpg')

	def __str__(self):
	    return self.title


class Circulos(models.Model):
	title = models.CharField(max_length = 100)
	body = models.TextField()
	adress = models.TextField()
	date = models.DateTimeField()

	def __str__(self):
	    return self.title


class Emails(models.Model):
	Nome = models.CharField(max_length = 50)
	Contacto = models.CharField(max_length = 25)
	Telemovel = models.CharField(max_length = 12)
	Mensagem = models.TextField()

	def __str__(self):
	    return self.Nome


class CirculoForum(models.Model):
	nome = models.CharField(max_length = 50)
	numero_topicos = models.IntegerField()
	descricao = models.CharField(max_length = 100)

	def __str__(self):
		return self.nome


class Topico(models.Model):
	forum = models.ForeignKey(CirculoForum)
	data = models.DateTimeField(auto_now = True)
	titulo = models.CharField(max_length = 50)
	descricao = models.TextField()
	autor = models.ForeignKey(User)

	def __str__(self):
		return self.id

class Comentario(models.Model):
	TopicoId = models.ForeignKey(Topico)
	data = models.DateTimeField(auto_now=True)
	comentario = models.CharField(max_length=200)
	autor = models.ForeignKey(User)

	def __str__(self):
		return self.id





