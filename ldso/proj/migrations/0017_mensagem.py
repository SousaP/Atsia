# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proj', '0016_auto_20151112_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('Texto', models.TextField()),
                ('data', models.DateTimeField(auto_now=True)),
                ('Vista', models.BooleanField()),
                ('Autor', models.ForeignKey(related_name='messages_sent', to=settings.AUTH_USER_MODEL)),
                ('Destinatario', models.ForeignKey(related_name='messages_received', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
