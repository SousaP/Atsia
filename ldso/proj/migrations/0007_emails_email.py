# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0006_auto_20151103_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='emails',
            name='Email',
            field=models.CharField(max_length=25, default='asd'),
            preserve_default=False,
        ),
    ]
