# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-20 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='age',
            field=models.CharField(default='', max_length=5),
            preserve_default=False,
        ),
    ]
