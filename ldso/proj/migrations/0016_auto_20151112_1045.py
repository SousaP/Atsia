# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0015_auto_20151111_1035'),
    ]

    operations = [
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=200)),
                ('data', models.DateTimeField(auto_now=True)),
                ('descricao', models.TextField()),
                ('ficheiro', models.FileField(blank=True, upload_to='files')),
            ],
        ),
        migrations.RenameField(
            model_name='topico',
            old_name='autor',
            new_name='Autor',
        ),
        migrations.RenameField(
            model_name='topico',
            old_name='data',
            new_name='Data',
        ),
        migrations.RenameField(
            model_name='topico',
            old_name='descricao',
            new_name='Descricao',
        ),
        migrations.RenameField(
            model_name='topico',
            old_name='forum',
            new_name='Forum',
        ),
        migrations.RenameField(
            model_name='topico',
            old_name='titulo',
            new_name='Titulo',
        ),
        migrations.RemoveField(
            model_name='topico',
            name='numero_respostas',
        ),
        migrations.AddField(
            model_name='topico',
            name='Autorizado',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
