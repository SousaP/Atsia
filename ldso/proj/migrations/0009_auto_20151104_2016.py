# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proj', '0008_auto_20151103_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='CirculoForum',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
                ('numero_topicos', models.IntegerField(default=b'0')),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateTimeField(auto_now=True)),
                ('comentario', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Topico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateTimeField(auto_now=True)),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
                ('numero_respostas', models.IntegerField()),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('forum', models.ForeignKey(to='proj.CirculoForum')),
            ],
        ),
        migrations.AddField(
            model_name='comentario',
            name='TopicoId',
            field=models.ForeignKey(to='proj.Topico'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='autor',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
