# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0012_participante'),
    ]

    operations = [
        migrations.AddField(
            model_name='participante',
            name='teste',
            field=models.CharField(max_length=200, default='teste'),
            preserve_default=False,
        ),
    ]
