# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-04 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20170204_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]