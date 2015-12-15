# -*- coding: utf-8 -*-

from django.db import models
from assets import models as am


class Vocabulary(am.AbstractRankedAPIFeatured):
    """ Taxonomy vocabularies registry. """
    old_id = models.IntegerField("old_id", blank=True, null=True)
    mnemo = models.CharField("Machine Name", max_length=200,
                             blank=True, null=True)
    description = models.TextField("Descrption", blank=True, null=True)
    hierarchy = models.IntegerField("Hierarchy", blank=True, null=True)
    module = models.CharField("Module", max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Taxonomy vocabulary"
        verbose_name_plural = "Taxonomy vocabularies"


class Term(am.AbstractRankedAPIFeatured):
    
    def __unicode__(self):
        return "{0} (id: {1})".decode("UTF-8").format(self.inner_name,
                                                      str(self.id))
    """ Taxonomy term. """
    old_id = models.IntegerField("old_id", blank=True, null=True)
    old_vocab_id = models.IntegerField("old_vocab_id", blank=True, null=True)
    vocab = models.ForeignKey(Vocabulary,
                              verbose_name="Vocabulary",
                              related_name="terms",
                              blank=True,
                              null=True
                              )
    description = models.TextField("Description", blank=True, null=True)
    weight = models.IntegerField("Weight", blank=True, null=True)
    
    def has_experts_bound(self):
        return self.experts_researching_this.filter(active=True).count()
    has_experts_bound.short_description = "Experts bound"
