# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0004_auto_20151022_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='photo_img',
            field=models.ImageField(default='img/logo_atsia.jpg', upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='emails',
            name='Email',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='emails',
            name='Mensagem',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='emails',
            name='Nome',
            field=models.CharField(max_length=50),
        ),
    ]
