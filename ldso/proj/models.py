from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length = 140)
	body = models.TextField()
	date = models.DateTimeField()

	def _unicode_(self):
		return self.title



