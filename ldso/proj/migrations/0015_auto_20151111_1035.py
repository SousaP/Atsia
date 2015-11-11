# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0014_auto_20151111_1034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participante',
            name='department',
        ),
        migrations.AddField(
            model_name='participante',
            name='circulo',
            field=models.ForeignKey(to='proj.CirculoForum', default='1'),
            preserve_default=False,
        ),
    ]
