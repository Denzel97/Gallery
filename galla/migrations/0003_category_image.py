# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-03-04 09:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galla', '0002_auto_20190304_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('image_name', models.ImageField(null=True, upload_to='images/')),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galla.Category')),
                ('location_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galla.Location')),
            ],
        ),
    ]
