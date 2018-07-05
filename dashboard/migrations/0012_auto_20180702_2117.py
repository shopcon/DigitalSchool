# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_mediagallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photogallery',
            name='desc',
            field=models.TextField(max_length=200),
        ),
    ]
