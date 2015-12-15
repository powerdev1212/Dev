# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _

from assets import models as am

class ClinicalTrial(am.AbstractRankedAPIFeatured):
    """ ClinicalTrial data model(start structure, needs to be extended). """
    class Meta:
        verbose_name = "clinical trial"
        verbose_name_plural = "clinical trials"
    issues = models.ManyToManyField("deseases.DeseaseItem",
        blank=True,
        verbose_name="Issues of clinical trials",
        related_name="clinical_trials")
        
class ClinicalTrialImage(am.AbstractRanked):
    """ Clinical Trial Image """
    class Meta:
        verbose_name = "Clinical Trial Image"
        verbose_name_plural = "Clinical Trial Images"
    '''
    category = models.ForeignKey("deseases.DeseaseCategory",
        blank=True,
        related_name="clinical_trials_images", 
        verbose_name="desease category")
    '''
    item = models.ForeignKey("deseases.DeseaseItem",
        blank=True,
        related_name="clinical_trials_images", 
        verbose_name="desease item")
    image = models.ImageField("URL", upload_to="images/ctrials", blank=True)
