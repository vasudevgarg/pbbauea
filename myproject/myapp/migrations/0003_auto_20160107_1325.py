# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import myproject.myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20151230_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to=myproject.myapp.models.upload_function),
        ),
    ]
