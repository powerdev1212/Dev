# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _

from assets import models as am


class Discussion(am.AbstractRankedAPIFeatured):
    """ Discussion data model(start structure, needs to be extended). """
    class Meta:
        verbose_name = "discussion"
        verbose_name_plural = "discussions"
    topics = models.ManyToManyField("deseases.DeseaseItem",
        blank=True,
        verbose_name="Topics of discussion",
        related_name="discussions")
        
class DiscussionImage(am.AbstractRanked):
    """ Discussion Image """
    class Meta:
        verbose_name = "Discussion Image"
        verbose_name_plural = "Discussion Images"
    '''
    category = models.ForeignKey("deseases.DeseaseCategory",
        blank=True,
        related_name="discussions_images",
        verbose_name="desease category")
    '''
    item = models.ForeignKey("deseases.DeseaseItem",
        blank=True,
        related_name="discussions_images",
        verbose_name="desease item")
    image = models.ImageField("Image", upload_to="images/discussions")
