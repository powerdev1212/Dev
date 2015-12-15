# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expertinstitution',
            name='experts',
            field=models.ManyToManyField(related_name='institutions', verbose_name=b'Experts in this institution', to='experts.Expert'),
        ),
        migrations.AddField(
            model_name='expertinstitution',
            name='old_expert_id',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='expertinstitution',
            name='old_id',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='expertdepartment',
            name='institution',
            field=models.ForeignKey(related_name='departments', verbose_name=b'Expert`s institution', blank=True, to='experts.ExpertInstitution', null=True),
        ),
    ]
