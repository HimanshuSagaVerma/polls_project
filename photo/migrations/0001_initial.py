# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-23 08:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='photodate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo.PhotoDate'),
        ),
    ]