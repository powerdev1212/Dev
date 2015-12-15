# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeseaseImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('rank', models.IntegerField(default=0, verbose_name=b'rank')),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
                ('image', models.ImageField(upload_to=b'images/deseases', verbose_name=b'Image', blank=True)),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='DeseaseItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inner_name', models.CharField(db_index=True, max_length=200, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('rank', models.IntegerField(default=0, verbose_name=b'rank')),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
                ('mnemo', models.CharField(help_text=b'Mnemo name for item', max_length=150, db_index=True, blank=True)),
                ('definition', models.TextField(max_length=500, verbose_name=b'definition', blank=True)),
                ('icd0_codes', models.CharField(max_length=150, verbose_name=b'ICD-O codes', blank=True)),
                ('icd10_codes', models.CharField(max_length=150, verbose_name=b'ICD-10 Code', blank=True)),
                ('omim_number', models.TextField(verbose_name=b'OMIM number', blank=True)),
                ('mesh', models.TextField(verbose_name=b'MESH', blank=True)),
                ('umls', models.TextField(verbose_name=b'UMLS', blank=True)),
                ('med_dpa', models.TextField(verbose_name=b'MedDRA', blank=True)),
                ('old_id', models.IntegerField(null=True, verbose_name=b'old_id', blank=True)),
                ('old_parent', models.IntegerField(null=True, verbose_name=b'old_parent', blank=True)),
                ('patient_version', models.TextField(verbose_name=b'Patient Version', blank=True)),
                ('genes_and_protiens', models.TextField(verbose_name=b'Genes involved and protiens', blank=True)),
                ('detailed_definition', models.TextField(verbose_name=b'Detailed Definition', blank=True)),
                ('risk_of_progression', models.TextField(verbose_name=b'Risk of progression', blank=True)),
                ('epidemiology', models.TextField(verbose_name=b'Epidemiology', blank=True)),
                ('sites', models.TextField(verbose_name=b'Sites of involvement', blank=True)),
                ('clinical_features', models.TextField(verbose_name=b'Clinical Features', blank=True)),
                ('grading', models.TextField(verbose_name=b'Grading', blank=True)),
                ('etiology', models.TextField(verbose_name=b'Aetiology', blank=True)),
                ('macroscopy', models.TextField(verbose_name=b'Macroscopy', blank=True)),
                ('histopathology', models.TextField(verbose_name=b'Histopathology', blank=True)),
                ('immunoprofile', models.TextField(verbose_name=b'Immunoprofile', blank=True)),
                ('immunophenotype', models.TextField(verbose_name=b'Immunophenotype', blank=True)),
                ('histogenesis', models.TextField(verbose_name=b'Histogenesis', blank=True)),
                ('ultrastructure', models.TextField(verbose_name=b'Ultrastructure', blank=True)),
                ('genetics', models.TextField(verbose_name=b'Genetics', blank=True)),
                ('cytogenetics', models.TextField(verbose_name=b'Cytogenetics', blank=True)),
                ('prognostic_factors', models.TextField(verbose_name=b'Prognostic and predictive Factors', blank=True)),
                ('differential_diagnosis', models.TextField(verbose_name=b'Differential Diagnosis', blank=True)),
                ('genetic_alterations', models.TextField(verbose_name=b'Genetic alterations', blank=True)),
                ('hp_reference_file', models.FileField(upload_to=b'files/hp_reference', verbose_name=b'References', blank=True)),
                ('nccn_treatment_patient', models.CharField(max_length=150, verbose_name=b'NCCN Treatment Patient', blank=True)),
                ('nccn_treatment_hp', models.CharField(max_length=150, verbose_name=b'NCCN Treatment HP', blank=True)),
                ('nccn_treatment', models.CharField(max_length=150, verbose_name=b'NCCN Treatment', blank=True)),
                ('slideshow_field', models.CharField(max_length=150, verbose_name=b'Slideshow Field', blank=True)),
                ('hp_slideshow', models.CharField(max_length=150, verbose_name=b'HP Slideshow', blank=True)),
            ],
            options={
                'verbose_name': 'desease',
                'verbose_name_plural': 'deseases',
                'permissions': (('can_view_hs_info', 'Can view info for health specialist'), ('can_view_patient_info', 'Can view info for patient')),
            },
        ),
        migrations.CreateModel(
            name='DeseaseSynonym',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inner_name', models.CharField(db_index=True, max_length=200, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
            ],
            options={
                'verbose_name': 'synonym',
                'verbose_name_plural': 'synonyms',
            },
        ),
        migrations.CreateModel(
            name='DeseaseType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inner_name', models.CharField(db_index=True, max_length=200, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('rank', models.IntegerField(default=0, verbose_name=b'rank')),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
                ('mnemo', models.CharField(help_text=b'Mnemo name for type', max_length=150, blank=True)),
            ],
            options={
                'verbose_name': 'desease type',
                'verbose_name_plural': 'desease types',
            },
        ),
        migrations.CreateModel(
            name='PatientVersionImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('rank', models.IntegerField(default=0, verbose_name=b'rank')),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
                ('image', models.ImageField(upload_to=b'images/patients/versions', verbose_name=b'Image', blank=True)),
                ('item', models.ForeignKey(related_name='patient_version_images', verbose_name=b'desease item', blank=True, to='deseases.DeseaseItem')),
            ],
            options={
                'verbose_name': 'Patient_Version_Image',
                'verbose_name_plural': 'Patient_Version_Images',
            },
        ),
        migrations.CreateModel(
            name='PatientVersionUrl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
                ('link', models.URLField(max_length=150, null=True, verbose_name=b'URL', blank=True)),
                ('item', models.ForeignKey(related_name='patient_version_url', verbose_name=b'desease item', blank=True, to='deseases.DeseaseItem')),
            ],
            options={
                'verbose_name': 'Patient_Version_URL',
                'verbose_name_plural': 'Patient_Version_URLs',
            },
        ),
        migrations.AddField(
            model_name='deseaseitem',
            name='dtype',
            field=models.ForeignKey(related_name='items', verbose_name=b'desease type', to='deseases.DeseaseType', null=True),
        ),
        migrations.AddField(
            model_name='deseaseitem',
            name='parent',
            field=models.ForeignKey(related_name='children', verbose_name=b'parent items', blank=True, to='deseases.DeseaseItem', null=True),
        ),
        migrations.AddField(
            model_name='deseaseitem',
            name='pubmed_terms',
            field=models.ManyToManyField(related_name='in_terms_for_items', to='taxonomy.Term', blank=True),
        ),
        migrations.AddField(
            model_name='deseaseitem',
            name='related_items',
            field=models.ManyToManyField(related_name='related_items_rel_+', verbose_name=b'Related Items', to='deseases.DeseaseItem'),
        ),
        migrations.AddField(
            model_name='deseaseitem',
            name='synonyms',
            field=models.ManyToManyField(related_name='synonyms_rel_+', to='deseases.DeseaseItem', blank=True),
        ),
        migrations.AddField(
            model_name='deseaseimage',
            name='item',
            field=models.ForeignKey(related_name='images', verbose_name=b'desease item', blank=True, to='deseases.DeseaseItem'),
        ),
    ]
