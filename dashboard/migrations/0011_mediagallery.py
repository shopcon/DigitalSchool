# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_photogallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaGallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=200)),
                ('image', models.ImageField(height_field=b'height_field', width_field=b'width_field', null=True, upload_to=b'mediagallery', blank=True)),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
            ],
        ),
    ]
