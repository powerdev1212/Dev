# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deseases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicalTrial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inner_name', models.CharField(db_index=True, max_length=200, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('rank', models.IntegerField(default=0, verbose_name=b'rank')),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
                ('issues', models.ManyToManyField(related_name='clinical_trials', verbose_name=b'Issues of clinical trials', to='deseases.DeseaseItem', blank=True)),
            ],
            options={
                'verbose_name': 'clinical trial',
                'verbose_name_plural': 'clinical trials',
            },
        ),
        migrations.CreateModel(
            name='ClinicalTrialImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('rank', models.IntegerField(default=0, verbose_name=b'rank')),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
                ('image', models.ImageField(upload_to=b'images/ctrials', verbose_name=b'URL', blank=True)),
                ('item', models.ForeignKey(related_name='clinical_trials_images', verbose_name=b'desease item', blank=True, to='deseases.DeseaseItem')),
            ],
            options={
                'verbose_name': 'Clinical Trial Image',
                'verbose_name_plural': 'Clinical Trial Images',
            },
        ),
    ]
