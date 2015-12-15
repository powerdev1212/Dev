# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deseases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inner_name', models.CharField(db_index=True, max_length=200, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('rank', models.IntegerField(default=0, verbose_name=b'rank')),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
                ('topics', models.ManyToManyField(related_name='discussions', verbose_name=b'Topics of discussion', to='deseases.DeseaseItem', blank=True)),
            ],
            options={
                'verbose_name': 'discussion',
                'verbose_name_plural': 'discussions',
            },
        ),
        migrations.CreateModel(
            name='DiscussionImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('rank', models.IntegerField(default=0, verbose_name=b'rank')),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
                ('image', models.ImageField(upload_to=b'images/discussions', verbose_name=b'Image')),
                ('item', models.ForeignKey(related_name='discussions_images', verbose_name=b'desease item', blank=True, to='deseases.DeseaseItem')),
            ],
            options={
                'verbose_name': 'Discussion Image',
                'verbose_name_plural': 'Discussion Images',
            },
        ),
    ]
