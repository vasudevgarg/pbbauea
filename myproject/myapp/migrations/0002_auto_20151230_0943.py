# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('to_user', models.ManyToManyField(related_name='from_user', through='myapp.Event', to='myapp.Person')),
            ],
        ),
        migrations.RenameField(
            model_name='document',
            old_name='uploaded_by',
            new_name='user',
        ),
        migrations.AddField(
            model_name='event',
            name='from_user',
            field=models.ForeignKey(related_name='event_as_giver', to='myapp.Person'),
        ),
        migrations.AddField(
            model_name='event',
            name='shared_file',
            field=models.ForeignKey(to='myapp.Document'),
        ),
        migrations.AddField(
            model_name='event',
            name='to_user',
            field=models.ForeignKey(related_name='event_as_received', to='myapp.Person'),
        ),
    ]
