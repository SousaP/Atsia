from django.contrib import admin
# adicionar post no blog

from proj.models import Blog, Circulos, Emails, CirculoForum, Topico, Musica, Mensagem, Comentario, Musica

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Blog)
admin.site.register(Circulos)
admin.site.register(Emails)
admin.site.register(CirculoForum)
admin.site.register(Topico)
admin.site.register(Mensagem)
admin.site.register(Comentario)
admin.site.register(Musica)
from proj.models import Participante

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class ParticipanteInline(admin.StackedInline):
    model = Participante
    can_delete = False
    verbose_name_plural = 'participante'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ParticipanteInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
