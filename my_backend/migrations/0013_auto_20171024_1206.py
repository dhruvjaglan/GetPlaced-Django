# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_backend', '0012_auto_20171024_0930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='gender',
        ),
        migrations.AlterField(
            model_name='student',
            name='offers',
            field=models.ManyToManyField(blank=True, to='my_backend.company_offer'),
        ),
    ]