# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 01:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('home', '0005_auto_20170730_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPageGalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('caption', models.CharField(blank=True, max_length=250)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.Image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='home.BlogPage')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
        ),
    ]
