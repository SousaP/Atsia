# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0003_circulos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emails',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Nome', models.TextField()),
                ('Email', models.TextField()),
                ('Telemovel', models.CharField(max_length=12)),
                ('Mensagem', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='circulos',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
