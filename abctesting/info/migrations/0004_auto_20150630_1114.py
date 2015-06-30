# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_samplelog_rush'),
    ]

    operations = [
        migrations.AlterField(
            model_name='samplelog',
            name='rush',
            field=models.CharField(blank=True, choices=[('3 Day', '3 day rush'), ('2 Day', '2 day rush'), ('1 Day', '1 day rush'), ('Same Day', 'same day rush')], max_length=10),
        ),
    ]
