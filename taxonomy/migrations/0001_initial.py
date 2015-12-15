# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inner_name', models.CharField(db_index=True, max_length=200, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('rank', models.IntegerField(default=0, verbose_name=b'rank')),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
                ('old_id', models.IntegerField(null=True, verbose_name=b'old_id', blank=True)),
                ('old_vocab_id', models.IntegerField(null=True, verbose_name=b'old_vocab_id', blank=True)),
                ('description', models.TextField(null=True, verbose_name=b'Description', blank=True)),
                ('weight', models.IntegerField(null=True, verbose_name=b'Weight', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vocabulary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inner_name', models.CharField(db_index=True, max_length=200, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('rank', models.IntegerField(default=0, verbose_name=b'rank')),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
                ('old_id', models.IntegerField(null=True, verbose_name=b'old_id', blank=True)),
                ('mnemo', models.CharField(max_length=200, null=True, verbose_name=b'Machine Name', blank=True)),
                ('description', models.TextField(null=True, verbose_name=b'Descrption', blank=True)),
                ('hierarchy', models.IntegerField(null=True, verbose_name=b'Hierarchy', blank=True)),
                ('module', models.CharField(max_length=255, null=True, verbose_name=b'Module', blank=True)),
            ],
            options={
                'verbose_name': 'Taxonomy vocabulary',
                'verbose_name_plural': 'Taxonomy vocabularies',
            },
        ),
        migrations.AddField(
            model_name='term',
            name='vocab',
            field=models.ForeignKey(related_name='terms', verbose_name=b'Vocabulary', blank=True, to='taxonomy.Vocabulary', null=True),
        ),
    ]
