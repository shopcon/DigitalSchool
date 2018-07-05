# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_auto_20180703_2341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='freecounselling',
            name='updated',
        ),
    ]
