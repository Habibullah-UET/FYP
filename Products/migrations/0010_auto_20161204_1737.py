# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-04 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0009_product_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Product_Description',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
