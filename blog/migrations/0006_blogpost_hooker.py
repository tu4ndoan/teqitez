# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogpost_feature_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='hooker',
            field=models.TextField(default='hooker'),
            preserve_default=False,
        ),
    ]
