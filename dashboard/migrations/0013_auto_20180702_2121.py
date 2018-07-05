# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_auto_20180702_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photogallery',
            name='desc',
            field=models.TextField(max_length=200, verbose_name=b'Brief Description'),
        ),
        migrations.AlterField(
            model_name='photogallery',
            name='image',
            field=models.ImageField(height_field=b'height_field', width_field=b'width_field', null=True, upload_to=b'Select Photo', blank=True),
        ),
    ]
