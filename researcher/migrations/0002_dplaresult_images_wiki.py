# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-16 21:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researcher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DplaResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('subject_heading1', models.CharField(max_length=250)),
                ('subject_heading2', models.CharField(max_length=250)),
                ('subject_heading3', models.CharField(max_length=250)),
                ('summary', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=250)),
                ('date_published', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageURL1', models.URLField()),
                ('imageURL2', models.URLField()),
                ('imageURL3', models.URLField()),
                ('imageURL4', models.URLField()),
                ('imageURL5', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Wiki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=250)),
                ('summary', models.TextField()),
            ],
        ),
    ]
