# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-09 19:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0004_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Rating',
            field=models.CharField(default=django.utils.timezone.now, max_length=3),
            preserve_default=False,
        ),
    ]
