# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0017_mensagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='topico',
            name='Img',
            field=models.ImageField(default='static/img/logo_atsia.jpg', upload_to='static/img/forum/topicos/'),
        ),
        migrations.AlterField(
            model_name='musica',
            name='ficheiro',
            field=models.FileField(blank=True, upload_to='static/music/blog/'),
        ),
    ]
