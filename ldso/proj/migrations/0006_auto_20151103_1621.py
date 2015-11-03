# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0005_auto_20151103_1058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emails',
            name='Email',
        ),
        migrations.AlterField(
            model_name='blog',
            name='photo_img',
            field=models.ImageField(default='static/img/logo_atsia.jpg', upload_to='static/img/blog/'),
        ),
    ]
