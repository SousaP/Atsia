# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0007_emails_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emails',
            old_name='Email',
            new_name='Contacto',
        ),
    ]
