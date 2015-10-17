from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length = 200)
	body = models.TextField()
	date = models.DateTimeField()

	def __unicode__(self):
	    return self.title


class Circulos(models.Model):
	title = models.CharField(max_length = 100)
	body = models.TextField()
	adress = models.TextField()
	date = models.DateTimeField()

	def __unicode__(self):
	    return self.title

