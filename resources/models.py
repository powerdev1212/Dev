# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _

from assets import models as am


class Resource(am.AbstractRankedAPIFeatured):
    """ Resource data model. """
    class Meta:
        verbose_name = "resource"
        verbose_name_plural = "resources"
    old_id = models.IntegerField("old_id", blank=True, null=True)
    link = models.URLField("URL", max_length=150, blank=True, null=True)
    image = models.ImageField(upload_to="images/resources",
                              blank=True,
                              null=True)
    topics = models.ManyToManyField("deseases.DeseaseItem",
                                    blank=True,
                                    verbose_name="Topics of resource",
                                    related_name="resources")
