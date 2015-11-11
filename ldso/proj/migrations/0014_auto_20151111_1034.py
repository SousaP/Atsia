# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0013_participante_teste'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participante',
            name='teste',
        ),
        migrations.AddField(
            model_name='participante',
            name='department',
            field=models.CharField(max_length=100, default='Porto'),
            preserve_default=False,
        ),
    ]
