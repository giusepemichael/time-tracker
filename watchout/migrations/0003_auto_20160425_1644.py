# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 23:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchout', '0002_auto_20160425_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='lname',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='fname',
            field=models.CharField(max_length=300),
        ),
    ]