# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_blogcomment_freecounselling'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freecounselling',
            name='email',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='freecounselling',
            name='mobile',
            field=models.CharField(max_length=10),
        ),
    ]
