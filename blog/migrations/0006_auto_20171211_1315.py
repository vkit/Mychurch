# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-11 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20171127_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
