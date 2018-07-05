# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_auto_20180702_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photogallery',
            name='desc',
            field=models.TextField(max_length=200, verbose_name=b'Brief Description:'),
        ),
        migrations.AlterField(
            model_name='photogallery',
            name='image',
            field=models.ImageField(upload_to=b'photogallery', width_field=b'width_field', height_field=b'height_field', blank=True, null=True, verbose_name=b'Select Photo:'),
        ),
    ]
