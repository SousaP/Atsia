from django import forms
from .models import Emails
from django.contrib.auth.models import User

class EmailForm(forms.ModelForm):

	class Meta:
		model = Emails
		fields = ('Nome', 'Contacto', 'Telemovel', 'Mensagem',)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']