from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length = 200)
	body = models.TextField()
	date = models.DateTimeField()
	photo_img = models.ImageField(upload_to = "static/img/blog/", default='static/img/logo_atsia.jpg')
	video = models.FileField(upload_to = "static/video/blog/", default='static/default/video.mp4')
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
	#id = models.IntegerField(primary_key=True)
	nome = models.CharField(max_length = 50)
	numero_topicos = models.IntegerField(default = '0', editable= True)
	descricao = models.CharField(max_length = 100)

	def __str__(self):
		return self.nome


class Topico(models.Model):
	Forum = models.ForeignKey(CirculoForum)
	Data = models.DateTimeField(auto_now = True)
	Titulo = models.CharField(max_length = 50)
	Descricao = models.TextField()
	Autor = models.ForeignKey(User)
	Autorizado = models.BooleanField()
	Img = models.FileField(upload_to = "static/img/forum/topicos/", default='static/img/logo_atsia.jpg')

	def __str__(self):
		return self.Titulo

class Comentario(models.Model):
	TopicoId = models.ForeignKey(Topico)
	data = models.DateTimeField(auto_now=True)
	comentario = models.CharField(max_length=200)
	autor = models.ForeignKey(User)

	def __str__(self):
		return self.comentario

class Musica(models.Model):
	nome = models.CharField(max_length=200)
	data = models.DateTimeField(auto_now = True)
	descricao = models.TextField()
	ficheiro = models.FileField(upload_to = "static/music/blog/", blank = True)

	def __str__(self):
		return self.nome


class Participante(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    circulo = models.ForeignKey(CirculoForum)


class Mensagem(models.Model):
	Autor = models.ForeignKey(User, related_name='messages_sent')
	Destinatario = models.ForeignKey(User, related_name='messages_received')
	Texto = models.TextField()
	data = models.DateTimeField(auto_now = True)
	Vista = models.BooleanField()

	def __str__(self):
		return self.Texto