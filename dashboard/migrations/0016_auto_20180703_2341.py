# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_auto_20180702_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediagallery',
            name='desc',
            field=models.TextField(max_length=200, verbose_name=b'Brief Description:'),
        ),
        migrations.AlterField(
            model_name='mediagallery',
            name='image',
            field=models.ImageField(default=1, height_field=b'height_field', width_field=b'width_field', upload_to=b'mediagallery', verbose_name=b'Select Image'),
            preserve_default=False,
        ),
    ]
