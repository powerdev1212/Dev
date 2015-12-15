# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deseases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inner_name', models.CharField(db_index=True, max_length=200, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('rank', models.IntegerField(default=0, verbose_name=b'rank')),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
                ('old_id', models.IntegerField(null=True, verbose_name=b'old_id', blank=True)),
                ('link', models.URLField(max_length=150, null=True, verbose_name=b'URL', blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'images/resources', blank=True)),
                ('topics', models.ManyToManyField(related_name='resources', verbose_name=b'Topics of resource', to='deseases.DeseaseItem', blank=True)),
            ],
            options={
                'verbose_name': 'resource',
                'verbose_name_plural': 'resources',
            },
        ),
    ]
