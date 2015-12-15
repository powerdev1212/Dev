# -*- coding: utf-8 -*-
import os
from django.contrib import admin
from hygeiais.settings import MEDIA_ROOT


class APIFeaturedModelAdmin(admin.ModelAdmin):
    """ Each admin model is supposed to have a set of additional functional. """
    actions = [
        "activate_items",
        "deactivate_items",
        "update_parent_id",
        "add_to_taxonomy_terms",
        "add_taxonomy_terms_to_item",
        "bind_nci_treatment_file",
        ]

    def activate_items(self, request, queryset):
        """ Mark all items as active """
        queryset.update(active=True)
    activate_items.short_description = "Mark items as active"

    def deactivate_items(self, request, queryset):
        """ Mark all items as non-active """
        queryset.update(active=False)
    deactivate_items.short_description = "Mark items as non-active"

    def update_parent_id(self, request, queryset):
        """ Update parent_id column """
        for i in queryset:
            try:
                i.parent_id = queryset.filter(old_id=i.old_parent)[0].id
            except:
                pass
            i.save()
    update_parent_id.short_description = "Update parent_id column"

    def add_to_taxonomy_terms(self, request, queryset):
        from deseases.models import DeseaseItem
        from taxonomy.models import Term
        """ Add item name to taxonomy terms """
        for i in queryset:
            if not Term.objects\
                    .filter(inner_name__icontains=i.inner_name).exists():
                t = Term()
                t.inner_name = i.inner_name
                t.save()
                if isinstance(i, (DeseaseItem)):
                    i.pubmed_terms.add(t)
    add_to_taxonomy_terms.short_description = "Add item to taxonomy terms"

    def add_taxonomy_terms_to_item(self, request, queryset):
        from deseases.models import DeseaseItem
        from taxonomy.models import Term
        """ Add taxonomy term to item terms """
        for i in queryset:
            for t in Term.objects.filter(inner_name__icontains=i.inner_name):
                if isinstance(i, (DeseaseItem)):
                    if t not in i.pubmed_terms.all():
                        i.pubmed_terms.add(t)
    add_taxonomy_terms_to_item.short_description = "Add taxonomy terms to item"

    def bind_nci_treatment_file(self, request, queryset):
        """ Bind NCI treatment guideline file to item """
        import lxml
        from treatment.models import TreatmentGuideline
        xmlfiles_path = os.path.join(MEDIA_ROOT, "xml/treatment")
        for i in queryset:
            if isinstance(i, (TreatmentGuideline)):
                pass
    bind_nci_treatment_file.short_description = \
        "Bind proper NCI Guideline file to selected items"
