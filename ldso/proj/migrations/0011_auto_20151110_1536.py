# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0010_auto_20151104_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='video',
            field=models.FileField(default='static/default/video.mp4', upload_to='static/video/blog/'),
        ),
        migrations.AlterField(
            model_name='circuloforum',
            name='numero_topicos',
            field=models.IntegerField(default='0'),
        ),
    ]
