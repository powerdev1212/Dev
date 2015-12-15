# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experts', '0001_initial'),
        ('deseases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inner_name', models.CharField(db_index=True, max_length=200, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('rank', models.IntegerField(default=0, verbose_name=b'rank')),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
                ('authors', models.ManyToManyField(related_name='publications', verbose_name=b'authors of publication', to='experts.Expert', blank=True)),
                ('topics', models.ManyToManyField(related_name='publications', verbose_name=b'topics', to='deseases.DeseaseItem', blank=True)),
            ],
            options={
                'verbose_name': 'publication',
                'verbose_name_plural': 'publications',
            },
        ),
        migrations.CreateModel(
            name='PublicationImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('rank', models.IntegerField(default=0, verbose_name=b'rank')),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
                ('image', models.ImageField(upload_to=b'images/publications', verbose_name=b'Image', blank=True)),
                ('item', models.ForeignKey(related_name='publication_images', verbose_name=b'desease item', blank=True, to='deseases.DeseaseItem')),
            ],
            options={
                'verbose_name': 'Publication Image',
                'verbose_name_plural': 'Publication Images',
            },
        ),
        migrations.CreateModel(
            name='PublicationTweetImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('rank', models.IntegerField(default=0, verbose_name=b'rank')),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
                ('image', models.ImageField(upload_to=b'images/publications/tweets', verbose_name=b'Image', blank=True)),
                ('item', models.ForeignKey(related_name='tweets', verbose_name=b'desease item', blank=True, to='deseases.DeseaseItem')),
            ],
            options={
                'verbose_name': 'Publication Tweet Image',
                'verbose_name_plural': 'Publication Tweet Images',
            },
        ),
    ]
