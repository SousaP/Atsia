# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0018_auto_20151116_1353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='circulos',
            old_name='adress',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='circulos',
            old_name='body',
            new_name='endereco',
        ),
        migrations.RemoveField(
            model_name='circuloforum',
            name='numero_topicos',
        ),
        migrations.AddField(
            model_name='circuloforum',
            name='geral',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='participante',
            name='Img',
            field=models.FileField(upload_to='static/img/participante/avatar/', default='static/img/participante/avatar/default.png'),
        ),
        migrations.AlterField(
            model_name='topico',
            name='Img',
            field=models.FileField(upload_to='static/img/forum/topicos/', default='static/img/logo_atsia.jpg'),
        ),
    ]
