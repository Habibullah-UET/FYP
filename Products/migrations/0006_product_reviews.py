# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-09 21:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0005_product_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Reviews',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]