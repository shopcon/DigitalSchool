# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_auto_20180702_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediagallery',
            name='desc',
            field=models.TextField(max_length=200),
        ),
    ]
