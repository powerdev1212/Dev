# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _

from assets import models as am

class Patient(am.AbstractRankedAPIFeatured):
    """ Patient data model(start structure, needs to be extended). """
    class Meta:
        verbose_name = "patient"
        verbose_name_plural = "patients"
    # each patient can have any number of deseases
    deseases = models.ManyToManyField("deseases.DeseaseItem",
        blank=True,
        verbose_name="deseases",
        related_name="patients")


