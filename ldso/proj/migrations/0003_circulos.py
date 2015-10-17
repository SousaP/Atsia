# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0002_auto_20151017_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='Circulos',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('adress', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
