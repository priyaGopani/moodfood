# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-02-12 00:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mood_name', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=100, null=True)),
                ('restaurant_address', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='restaurant',
            name='restaurant_type',
            field=models.ManyToManyField(to='moods.Type'),
        ),
        migrations.AddField(
            model_name='mood',
            name='restaurant_list',
            field=models.ManyToManyField(to='moods.Restaurant'),
        ),
    ]
