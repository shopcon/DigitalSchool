# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20180622_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='para2',
            field=models.TextField(null=True, verbose_name=b'2nd Paragraph', blank=True),
        ),
    ]
