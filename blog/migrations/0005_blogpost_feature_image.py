# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 11:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170819_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='feature_image',
            field=models.FileField(default='default value', upload_to=''),
            preserve_default=False,
        ),
    ]
