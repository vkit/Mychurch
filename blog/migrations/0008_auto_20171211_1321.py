# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-11 13:21
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20171211_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
