# -*- coding: utf-8 -*-

from django.contrib import admin
from assets import models as am
from . import models


class VocabularyAdmin(am.APIFeaturedModelAdmin):
    list_display = ("__str__", "active")
admin.site.register(models.Vocabulary, VocabularyAdmin)


class TermAdmin(am.APIFeaturedModelAdmin):
    list_display = "__str__", "old_id", "vocab_id", \
                   "has_experts_bound", "active"
    list_filter = "vocab_id",
    search_fields = "inner_name", "id", "old_id"
    ordering = "inner_name",
admin.site.register(models.Term, TermAdmin)
