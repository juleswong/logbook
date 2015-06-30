# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=2000)),
                ('address', models.CharField(max_length=1000, blank=True)),
                ('city', models.CharField(max_length=1000, blank=True)),
                ('state', models.CharField(max_length=20, blank=True)),
                ('zipcode', models.CharField(max_length=200, blank=True)),
                ('telephone', models.CharField(max_length=1000, blank=True)),
                ('fax_number', models.CharField(max_length=500, blank=True)),
                ('email', models.CharField(max_length=500, blank=True)),
                ('contact_customer', models.CharField(max_length=2000, blank=True)),
                ('comments', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SampleLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_order', models.CharField(max_length=500, blank=True)),
                ('date_received', models.DateField()),
                ('lab_number', models.IntegerField(unique=True)),
                ('invoice_number', models.IntegerField(unique=True)),
                ('product_name', models.CharField(max_length=2000)),
                ('lot_number', models.CharField(max_length=2000, blank=True)),
                ('item_number', models.CharField(max_length=2000, blank=True)),
                ('test_request', models.TextField()),
                ('notes', models.TextField(blank=True)),
                ('customer', models.ForeignKey(to='info.Customer')),
            ],
        ),
    ]
