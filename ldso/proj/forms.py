from django import forms
from django.contrib.auth.models import User
from .models import Emails, Topico, Comentario

class EmailForm(forms.ModelForm):

	class Meta:
		model = Emails
		fields = ('Nome', 'Contacto', 'Telemovel', 'Mensagem',)



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class TopicoForm(forms.ModelForm):

	class Meta:
		model = Topico
		exclude = ['Forum','Autor','Autorizado']
		#fields = ('Forum', 'Titulo', 'Descricao', 'Autor', 'Autorizado',)



class NovoComentario(forms.ModelForm):
	
	class Meta:
		model = Comentario      
		exclude = ['TopicoId', 'autor']        