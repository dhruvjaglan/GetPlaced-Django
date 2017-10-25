# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_backend', '0015_auto_20171024_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_offer',
            name='interested_students',
            field=models.ManyToManyField(blank=True, related_name='interested', to='my_backend.applicant_detail'),
        ),
        migrations.AlterField(
            model_name='company_offer',
            name='shortlisted_students',
            field=models.ManyToManyField(blank=True, related_name='shortlist', to='my_backend.applicant_detail'),
        ),
    ]