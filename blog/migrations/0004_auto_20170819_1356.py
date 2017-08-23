# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170819_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=150),
        ),
    ]
