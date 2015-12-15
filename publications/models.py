# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _

from assets import models as am


# Create your models here.
class Publication(am.AbstractRankedAPIFeatured):
    """ Publication data model(start structure, needs to be extended). """
    class Meta:
        verbose_name = "publication"
        verbose_name_plural = "publications"
    authors = models.ManyToManyField("experts.Expert",
        blank=True,
        verbose_name="authors of publication",
        related_name="publications")
    topics = models.ManyToManyField("deseases.DeseaseItem",
        blank=True,
        verbose_name="topics",
        related_name="publications")
        
class PublicationImage(am.AbstractRanked):
    """ Publication Image """
    class Meta:
        verbose_name = "Publication Image"
        verbose_name_plural = "Publication Images"
    """
    category = models.ForeignKey("deseases.DeseaseCategory",
        blank=True,
        related_name="publication_images",
        verbose_name="desease category")
    """
    item = models.ForeignKey("deseases.DeseaseItem",
        blank=True,
        related_name="publication_images",
        verbose_name="desease item")
    image = models.ImageField("Image", upload_to="images/publications", blank=True)
    
class PublicationTweetImage(am.AbstractRanked):
    """ Publication Image """
    class Meta:
        verbose_name = "Publication Tweet Image"
        verbose_name_plural = "Publication Tweet Images"
    """
    category = models.ForeignKey("deseases.DeseaseCategory",
        blank=True,
        related_name="tweets",
        verbose_name="desease category")
    """
    item = models.ForeignKey("deseases.DeseaseItem",
        blank=True,
        related_name="tweets",
        verbose_name="desease item")
    image = models.ImageField("Image", upload_to="images/publications/tweets", blank=True)

