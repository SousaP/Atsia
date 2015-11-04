from django import forms
from .models import Emails

class EmailForm(forms.ModelForm):

	class Meta:
		model = Emails
		fields = ('Nome', 'Contacto', 'Telemovel', 'Mensagem',)
		