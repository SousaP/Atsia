from django import forms
from .models import Emails, Topico

class EmailForm(forms.ModelForm):

	class Meta:
		model = Emails
		fields = ('Nome', 'Contacto', 'Telemovel', 'Mensagem',)
		


class TopicoForm(forms.ModelForm):

	class Meta:
		model = Topico
		exclude = ['Forum','Autor','Autorizado']
		#fields = ('Forum', 'Titulo', 'Descricao', 'Autor', 'Autorizado',)
