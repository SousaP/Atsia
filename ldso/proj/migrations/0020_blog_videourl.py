# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0019_auto_20151222_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='videourl',
            field=models.CharField(default='videourl', max_length=200),
        ),
    ]
