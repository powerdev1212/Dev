# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deseases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CancerStudyLoadedStorage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inner_name', models.CharField(db_index=True, max_length=200, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
                ('mnemo', models.CharField(max_length=100, null=True, verbose_name=b'type_of_cancer_id', blank=True)),
                ('description', models.TextField(null=True, verbose_name=b'description', blank=True)),
                ('link', models.URLField(null=True, verbose_name=b'link', blank=True)),
                ('desease', models.ForeignKey(related_name='genomic_studies', verbose_name=b'Desease', blank=True, to='deseases.DeseaseItem', null=True)),
            ],
            options={
                'verbose_name': 'loaded cancer type (www.cbioportal.org)',
                'verbose_name_plural': 'loaded cancer types (www.cbioportal.org)',
            },
        ),
        migrations.CreateModel(
            name='ExpertsLoadedStorage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inner_name', models.CharField(db_index=True, max_length=200, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
                ('first_name', models.CharField(max_length=150, verbose_name=b'First Name', blank=True)),
                ('last_name', models.CharField(max_length=150, verbose_name=b'Last Name', blank=True)),
                ('degrees', models.CharField(max_length=150, verbose_name=b'Degrees', blank=True)),
                ('bio', models.TextField(max_length=1000, null=True, verbose_name=b'Bio Statement', blank=True)),
                ('specialities', models.TextField(null=True, verbose_name=b'Speciality', blank=True)),
                ('clinical_expertises', models.TextField(null=True, verbose_name=b'Clinical Expertises', blank=True)),
                ('research_interests', models.TextField(null=True, verbose_name=b'Research Interests', blank=True)),
                ('publications', models.TextField(null=True, verbose_name=b'Publications', blank=True)),
                ('appointment', models.CharField(max_length=200, null=True, verbose_name=b'Appointment', blank=True)),
                ('medical_educations', models.TextField(null=True, verbose_name=b'Medical Education', blank=True)),
                ('training_new', models.TextField(null=True, verbose_name=b'Trainings', blank=True)),
                ('trainings', models.TextField(null=True, verbose_name=b'Trainings', blank=True)),
                ('board_certifications', models.TextField(null=True, verbose_name=b'Board Sertifications', blank=True)),
                ('experiences', models.TextField(null=True, verbose_name=b'Experience', blank=True)),
                ('awards', models.TextField(null=True, verbose_name=b'Honors & Awards', blank=True)),
                ('seniority', models.IntegerField(default=0, verbose_name=b'Seniority')),
                ('country', models.CharField(max_length=150, verbose_name=b'Country', blank=True)),
                ('state', models.CharField(max_length=150, verbose_name=b'State', blank=True)),
                ('phone', models.CharField(max_length=150, verbose_name=b'Phone', blank=True)),
                ('email', models.EmailField(max_length=150, verbose_name=b'Email', blank=True)),
                ('profile_picture', models.URLField(null=True, verbose_name=b'Expert`s Photo', blank=True)),
            ],
            options={
                'verbose_name': 'loaded expert',
                'verbose_name_plural': 'loaded experts',
            },
        ),
        migrations.CreateModel(
            name='LoaderEngine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inner_name', models.CharField(db_index=True, max_length=200, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('rank', models.IntegerField(default=0, verbose_name=b'rank')),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
                ('mnemo', models.CharField(max_length=200, null=True, verbose_name=b'mnemo', blank=True)),
            ],
            options={
                'verbose_name': 'loader engine',
                'verbose_name_plural': 'loader engines',
            },
        ),
        migrations.CreateModel(
            name='LoaderEngineConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
                ('datatype', models.CharField(default=b'xml', max_length=10, verbose_name=b'Type of source data', choices=[(b'json', b'JSON'), (b'xml', b'XML'), (b'csv', b'CSV'), (b'text', b'TEXT')])),
                ('url', models.TextField(help_text=b'\n                           Change this value if you exactly \n                           know what you do only:)\n                           ', verbose_name=b'Target site URL')),
                ('url2', models.TextField(help_text=b'\n                           Change this value if you exactly \n                           know what you do only:)\n                           ', null=True, verbose_name=b'Target site URL(2)', blank=True)),
                ('search_values', models.TextField(help_text=b'\n                                     All values should be \n                                     comma-separated\n                                     ', max_length=2000, null=True, verbose_name=b'Values for search', blank=True)),
                ('paginator_start', models.IntegerField(default=0, help_text=b'\n                                          Start page number \n                                          (paginated search)\n                                          ', verbose_name=b'Start page')),
                ('paginator_end', models.IntegerField(default=1, help_text=b'\n                                          Finish page number \n                                          (paginated search)\n                                          ', verbose_name=b'Finish page')),
                ('period_type', models.CharField(default=b'WE', max_length=10, verbose_name=b'Update Period Type', choices=[(b'HO', b'Hours'), (b'DA', b'Days'), (b'WE', b'Weeks'), (b'MO', b'Months')])),
                ('value', models.IntegerField(default=1, help_text=b'\n                                Data update will be performed\n                                once a \n                                (VALUE) Hours, Days, Weeks, Months (depends on Update Period Type)\n                                ', verbose_name=b'Update Period Value')),
                ('engine', models.OneToOneField(related_name='config', null=True, blank=True, to='loaders.LoaderEngine', verbose_name=b'Loader Engine')),
            ],
            options={
                'verbose_name': 'loader engine config',
                'verbose_name_plural': 'loader engine configs',
            },
        ),
        migrations.CreateModel(
            name='LoaderEngineSelector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('rank', models.IntegerField(default=0, verbose_name=b'rank')),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
                ('inner_name', models.CharField(help_text=b'Name of field for usability', max_length=200, null=True, blank=True)),
                ('mnemo', models.CharField(help_text=b'Name of field in proper storage', max_length=200, verbose_name=b'mnemo')),
                ('value', models.CharField(help_text=b'\n                             Selector for retrieve proper \n                             data for the field from source\n                             ', max_length=200, verbose_name=b'expression')),
                ('engine', models.ForeignKey(related_name='selectors', verbose_name=b'parent loader engine', blank=True, to='loaders.LoaderEngine', null=True)),
            ],
            options={
                'verbose_name': 'selector expression',
                'verbose_name_plural': 'selector expressions',
            },
        ),
        migrations.AddField(
            model_name='expertsloadedstorage',
            name='engine',
            field=models.ManyToManyField(related_name='experts_loaded', to='loaders.LoaderEngine', blank=True),
        ),
        migrations.AddField(
            model_name='cancerstudyloadedstorage',
            name='engine',
            field=models.ManyToManyField(related_name='cancerstudies_loaded', to='loaders.LoaderEngine', blank=True),
        ),
    ]
