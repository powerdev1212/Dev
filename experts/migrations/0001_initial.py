# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inner_name', models.CharField(db_index=True, max_length=200, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('rank', models.IntegerField(default=0, verbose_name=b'rank')),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
                ('old_id', models.IntegerField(null=True, verbose_name=b'old_id', blank=True)),
                ('first_name', models.CharField(max_length=150, verbose_name=b'First Name', blank=True)),
                ('last_name', models.CharField(max_length=150, verbose_name=b'Last Name', blank=True)),
                ('so_agreement', models.BooleanField(default=False, help_text=b'Agreed to consult', verbose_name=b'SO Argeement')),
                ('degrees', models.CharField(max_length=150, verbose_name=b'Degrees', blank=True)),
                ('bio', models.TextField(max_length=1000, null=True, verbose_name=b'Bio Statement', blank=True)),
                ('research_interests', models.TextField(verbose_name=b'Research Interests', blank=True)),
                ('training_new', models.TextField(null=True, verbose_name=b'Trainings', blank=True)),
                ('seniority', models.IntegerField(default=0, verbose_name=b'Seniority')),
                ('phone', models.CharField(max_length=150, verbose_name=b'Phone', blank=True)),
                ('email', models.EmailField(max_length=150, verbose_name=b'Email', blank=True)),
                ('profile_picture', models.ImageField(upload_to=b'images/experts', null=True, verbose_name=b'', blank=True)),
            ],
            options={
                'verbose_name': 'expert',
                'verbose_name_plural': 'experts',
            },
        ),
        migrations.CreateModel(
            name='ExpertAppointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inner_name', models.CharField(db_index=True, max_length=200, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('rank', models.IntegerField(default=0, verbose_name=b'rank')),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
                ('old_expert_id', models.IntegerField(null=True, verbose_name=b'old_expert_id', blank=True)),
            ],
            options={
                'verbose_name': 'expert appointment',
                'verbose_name_plural': 'expert appointments',
            },
        ),
        migrations.CreateModel(
            name='ExpertAward',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inner_name', models.CharField(db_index=True, max_length=200, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
                ('old_expert_id', models.IntegerField(null=True, verbose_name=b'old_expert_id', blank=True)),
            ],
            options={
                'verbose_name': 'expert`s award',
                'verbose_name_plural': 'experts` awards',
            },
        ),
        migrations.CreateModel(
            name='ExpertBoardSertification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inner_name', models.CharField(db_index=True, max_length=200, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
                ('old_expert_id', models.IntegerField(null=True, verbose_name=b'old_expert_id', blank=True)),
            ],
            options={
                'verbose_name': 'expert sertification',
                'verbose_name_plural': 'expert sertifications',
            },
        ),
        migrations.CreateModel(
            name='ExpertDepartment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inner_name', models.CharField(db_index=True, max_length=200, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('rank', models.IntegerField(default=0, verbose_name=b'rank')),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
            ],
            options={
                'verbose_name': 'department',
                'verbose_name_plural': 'departments',
            },
        ),
        migrations.CreateModel(
            name='ExpertEducation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inner_name', models.CharField(db_index=True, max_length=200, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
                ('old_expert_id', models.IntegerField(null=True, verbose_name=b'old_expert_id', blank=True)),
            ],
            options={
                'verbose_name': 'expert education',
                'verbose_name_plural': 'expert educations',
            },
        ),
        migrations.CreateModel(
            name='ExpertExperience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inner_name', models.CharField(db_index=True, max_length=200, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
                ('old_expert_id', models.IntegerField(null=True, verbose_name=b'old_expert_id', blank=True)),
            ],
            options={
                'verbose_name': 'expert`s experience',
                'verbose_name_plural': 'experts` experience',
            },
        ),
        migrations.CreateModel(
            name='ExpertInstitution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inner_name', models.CharField(db_index=True, max_length=200, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('rank', models.IntegerField(default=0, verbose_name=b'rank')),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
            ],
            options={
                'verbose_name': 'institution',
                'verbose_name_plural': 'institutions',
            },
        ),
        migrations.CreateModel(
            name='ExpertLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inner_name', models.CharField(db_index=True, max_length=200, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
                ('old_expert_id', models.IntegerField(null=True, verbose_name=b'old_expert_id', blank=True)),
            ],
            options={
                'verbose_name': 'expert location',
                'verbose_name_plural': 'expert locations',
            },
        ),
        migrations.CreateModel(
            name='ExpertTraining',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inner_name', models.CharField(db_index=True, max_length=200, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated', null=True)),
                ('active', models.BooleanField(default=True, verbose_name=b'in use')),
                ('old_expert_id', models.IntegerField(null=True, verbose_name=b'old_expert_id', blank=True)),
            ],
            options={
                'verbose_name': 'expert training',
                'verbose_name_plural': 'expert trainings',
            },
        ),
        migrations.AddField(
            model_name='expertdepartment',
            name='institution',
            field=models.ForeignKey(related_name='experts', verbose_name=b'Expert`s institution', blank=True, to='experts.ExpertInstitution', null=True),
        ),
        migrations.AddField(
            model_name='expertappointment',
            name='department',
            field=models.ForeignKey(related_name='experts', verbose_name=b'expert`s department', blank=True, to='experts.ExpertDepartment', null=True),
        ),
        migrations.AddField(
            model_name='expert',
            name='appointment',
            field=models.ForeignKey(related_name='experts_appointed', verbose_name=b'Appointment', blank=True, to='experts.ExpertAppointment', null=True),
        ),
        migrations.AddField(
            model_name='expert',
            name='awards',
            field=models.ManyToManyField(related_name='experts_awarded', verbose_name=b'Honors and Awards', to='experts.ExpertAward', blank=True),
        ),
        migrations.AddField(
            model_name='expert',
            name='board_certifications',
            field=models.ManyToManyField(related_name='experts_sertified', verbose_name=b'Board Certifications', to='experts.ExpertBoardSertification', blank=True),
        ),
        migrations.AddField(
            model_name='expert',
            name='clinical_expertises',
            field=models.ManyToManyField(related_name='experts_researching_this', verbose_name=b'Clinical Expertises', to='taxonomy.Term', blank=True),
        ),
        migrations.AddField(
            model_name='expert',
            name='experiences',
            field=models.ManyToManyField(related_name='Experience', verbose_name=b'Experience', to='experts.ExpertExperience', blank=True),
        ),
        migrations.AddField(
            model_name='expert',
            name='location',
            field=models.ForeignKey(related_name='experts_located', verbose_name=b'Location', blank=True, to='experts.ExpertLocation', null=True),
        ),
        migrations.AddField(
            model_name='expert',
            name='medical_educations',
            field=models.ManyToManyField(related_name='experts_has_such_education', verbose_name=b'Medical Education', to='experts.ExpertEducation', blank=True),
        ),
        migrations.AddField(
            model_name='expert',
            name='specialities',
            field=models.ManyToManyField(related_name='experts_of_this_speciality', verbose_name=b'Specialities', to='taxonomy.Term', blank=True),
        ),
        migrations.AddField(
            model_name='expert',
            name='trainings',
            field=models.ManyToManyField(related_name='experts_trained', verbose_name=b'Trainings', to='experts.ExpertTraining', blank=True),
        ),
    ]
