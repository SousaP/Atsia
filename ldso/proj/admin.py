from django.contrib import admin
# adicionar post no blog
from proj.models import Blog, Circulos, Emails

# Register your models here.
admin.site.register(Blog)
admin.site.register(Circulos)
admin.site.register(Emails)

