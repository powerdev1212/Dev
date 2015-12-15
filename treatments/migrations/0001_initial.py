# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deseases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inner_name', models.CharField(db_index=True, max_length=200, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('rank', models.IntegerField(default=0, verbose_name=b'rank')),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
                ('old_id', models.IntegerField(null=True, verbose_name=b'old_id', blank=True)),
                ('deseases', models.ManyToManyField(related_name='treatments', verbose_name=b'deseases', to='deseases.DeseaseItem', blank=True)),
            ],
            options={
                'verbose_name': 'treatment',
                'verbose_name_plural': 'treatments',
            },
        ),
        migrations.CreateModel(
            name='TreatmentGuideline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inner_name', models.CharField(db_index=True, max_length=200, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('rank', models.IntegerField(default=0, verbose_name=b'rank')),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
                ('link', models.URLField(max_length=150, null=True, blank=True)),
                ('xmlfile', models.FileField(upload_to=b'xml/treatment', null=True, verbose_name=b'XML file', blank=True)),
                ('xslfile', models.FileField(upload_to=b'xsl/treatment', null=True, verbose_name=b'XSL file', blank=True)),
            ],
            options={
                'verbose_name': 'treatment guideline',
                'verbose_name_plural': 'treatment guideline',
            },
        ),
        migrations.CreateModel(
            name='TreatmentGuidelineIssuer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inner_name', models.CharField(db_index=True, max_length=200, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('rank', models.IntegerField(default=0, verbose_name=b'rank')),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
            ],
            options={
                'verbose_name': 'treatment guideline issuer',
                'verbose_name_plural': 'treatment guideline issuers',
            },
        ),
        migrations.AddField(
            model_name='treatmentguideline',
            name='issuer',
            field=models.ForeignKey(verbose_name=b'guideline issuer', to='treatments.TreatmentGuidelineIssuer'),
        ),
        migrations.AddField(
            model_name='treatmentguideline',
            name='treatment',
            field=models.ForeignKey(related_name='guidelines', verbose_name=b'treatment item', to='treatments.Treatment'),
        ),
    ]
