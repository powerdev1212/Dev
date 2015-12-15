# -*- coding: utf-8 -*-
import os
from lxml import etree
from django.contrib import admin
from django.db.models import Q

from hygeiais.settings import MEDIA_ROOT
from deseases.models import DeseaseItem
from . import models
from assets import models as am



def get_desease_by_exact_name(desease_name, obj):
    """ Trying get desease item by exact name """
    ditem = DeseaseItem.objects.get(inner_name__lower=desease_name)
    if ditem:
        obj.add(ditem)



class TreatmentGuidelineIssuerAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.TreatmentGuidelineIssuer, TreatmentGuidelineIssuerAdmin)


class TreatmentGuidelineAdmin(am.APIFeaturedModelAdmin):
    actions = ["register_guidelines_loaded"]
    search_fields=("inner_name",)

    def register_guidelines_loaded(self, request, queryset):
        """
        Method for registration loaded xmls in database:
        1. Instantiate values for processing
        2. Collect xml-files
        
        """
        # 1.Instantiate values for processing
        # rel_xml_path
        rel_xml_dir = "xml/treatment"
        # rel_xsl_path
        rel_xsl_dir = "xsl/treatment"
        # xsl file
        xsl_fname = "Treatment.xsl"
        
        # xml dir
        xml_dir = os.path.join(MEDIA_ROOT, rel_xml_dir)
        # xsl dir
        xsl_dir = os.path.join(MEDIA_ROOT, rel_xsl_dir)
        # common xsl filepath
        xsl_fpath = os.path.join(rel_xsl_dir, xsl_fname)

        # XPATH selectors
        inner_name_sel = "SummaryTitle/text()"
        treatment_inner_name_sel = "AltTitle/text()"
        link_sel = "SummaryMetaData/SummaryURL/@xref"
        term_sel = "SummaryMetaData/MainTopics/TermRef/text()"
        addterms_sel = "SummarySection/descendant::Para/GlossaryTermRef/text()"
        
        # opening
        xmls = [i for i in os.listdir(xml_dir) if i.endswith(".xml")]
        # processing
        for fname in xmls:
            # join filename to dirpath
            absfpath = os.path.join(xml_dir, fname)
            # get parsed data from file
            r = etree.parse(absfpath).getroot()
            # set document root
            # r = _data.getroot()
            
            # get values from selectors
            inner_name = r.xpath(inner_name_sel).pop(0)
            treatment_inner_name = r.xpath(treatment_inner_name_sel).pop(0)
            link = r.xpath(link_sel).pop(0)
            term = r.xpath(term_sel).pop(0).lower()
            addterms = r.xpath(addterms_sel)
            issuer = models.TreatmentGuidelineIssuer.objects.get(inner_name__in=("nci", "NCI"))
            # check for presense in DB
            if not models.TreatmentGuideline.objects.filter(inner_name=inner_name).exists():
                # then check for treatment object
                if not models.Treatment.objects.filter(inner_name=treatment_inner_name).exists():
                    t = models.Treatment()
                    t.inner_name = treatment_inner_name
                    # this func adds desease item to t.deseases by exact name
                    #get_desease_by_exact_name(term, t.deseases)
                    t.save()
                # and write new instance
                tg = models.TreatmentGuideline()
                tg.inner_name = inner_name
                tg.issuer = issuer
                tg.link = link
                tg.xmlfile = os.path.join(rel_xml_dir, fname)
                # xsl stylesheet is common for all xmls
                tg.xslfile = xsl_fpath
                tg.treatment = t
                tg.save()
    register_guidelines_loaded.short_description = "Register guidelines loaded"
admin.site.register(models.TreatmentGuideline, TreatmentGuidelineAdmin)


class TreatmentAdmin(am.APIFeaturedModelAdmin):
    actions = ["bind_desease"]
    search_fields=("inner_name",)
    ordering = ("inner_name",)
    def bind_desease(self, request, queryset):
        for q in queryset.all():
            chunked_inner_name = q.inner_name.lower().split(" ")
            for chunk in chunked_inner_name:
                if len(chunk) > 3:
                    try:
                        di = DeseaseItem.objects.get(Q(inner_name__istartswith=chunk)|Q(inner_name__icontains=chunk)|Q(inner_name__iendswith=chunk))
                        if di:
                            q.deseases.add(di)
                            q.save()
                    except:
                        pass
    bind_desease.short_description = "Bind deseases to treatment"
admin.site.register(models.Treatment, TreatmentAdmin)
