# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-04 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0005_auto_20161204_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Product_Image',
            field=models.ImageField(upload_to=''),
        ),
    ]