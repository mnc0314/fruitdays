# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-28 01:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20180328_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='alive',
            field=models.BooleanField(verbose_name=True),
        ),
    ]
