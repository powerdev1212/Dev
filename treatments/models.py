# -*- coding: utf-8 -*-
from lxml import etree
from django.db import models
from django.utils.translation import ugettext as _

from assets import models as am
from deseases.models import DeseaseItem

class TreatmentGuidelineIssuer(am.AbstractRankedAPIFeatured):
    """ Guideline issuer data model. """
    class Meta:
        verbose_name = "treatment guideline issuer"
        verbose_name_plural = "treatment guideline issuers"


class TreatmentGuideline(am.AbstractRankedAPIFeatured):
    """ Treatment Guideline data model. """
    class Meta:
        verbose_name = "treatment guideline"
        verbose_name_plural = "treatment guideline"
    # treatment FK. May be there are reason to found Many-to-many here?
    treatment = models.ForeignKey("Treatment",verbose_name="treatment item",related_name="guidelines")
    # guide issuer is mandatory
    issuer = models.ForeignKey(TreatmentGuidelineIssuer, verbose_name="guideline issuer")
    # url of guideline resource page
    link = models.URLField(max_length=150, blank=True, null=True)
    # xml file source
    xmlfile = models.FileField("XML file",
                               upload_to="xml/treatment",
                               blank=True,
                               null=True)
    # xsl file source
    xslfile = models.FileField("XSL file",
                               upload_to="xsl/treatment",
                               blank=True,
                               null=True)

    def process_data(self):
        """ Processing of xml data of guide """
        if self.xmlfile and self.xslfile:
            xml = etree.parse(self.xmlfile.path)
            xslt = etree.parse(self.xslfile.path)
            transform = etree.XSLT(xslt)
            return transform(xml)
        elif self.link:
            return self.link

    def bind_treatment(self):
        # XPATH selectors
        inner_name_sel = "SummaryTitle/text()"
        treatment_inner_name_sel = "AltTitle/text()"
        link_sel = "SummaryMetaData/SummaryURL/@xref"
        term_sel = "SummaryMetaData/MainTopics/TermRef/text()"
        addterms_sel = "SummarySection/descendant::Para/GlossaryTermRef/text()"
        r = etree.parse(absfpath).getroot()
        
        # get values from selectors
        inner_name = r.xpath(inner_name_sel).pop(0)
        treatment_inner_name = r.xpath(treatment_inner_name_sel).pop(0)
        link = r.xpath(link_sel).pop(0)
        term = r.xpath(term_sel).pop(0).lower()
        addterms = r.xpath(addterms_sel)
        t = Treatment.objects.filter(inner_name=treatment_inner_name)
        if not t.exists():
            t = Treatment()
            t.inner_name = treatment_inner_name
            # this func adds desease item to t.deseases by exact name
            ditem = DeseaseItem.objects.get(inner_name__lower=desease_name)
            if ditem:
                t.deseases.add(ditem)
            t.save()
        return t

    def save(self, *args, **kwargs):
        if not self.inner_name or self.inner_name == "":
            self.inner_name = self.treatment.inner_name
        if not self.treatment:
            self.treatment = self.bind_treatment()
        super(TreatmentGuideline, self).save(*args, **kwargs)


class TreatmentManager(models.Manager):
    def get_by_deseases_mnemo(self, mnemos):
        if isinstance(mnemos,(tuple,list)):
            return super(TreatmentManager, self).get_queryset()\
            .select_related()\
            .filter(deseases__mnemo__in=mnemos, active=True)
        return super(TreatmentManager, self).get_queryset()\
        .select_related()\
        .filter(deseases__mnemo__in=[mnemos], active=True)
        
class Treatment(am.AbstractRankedAPIFeatured):
    """ Deseases treatment data model(start structure, needs to be extended). """
    class Meta:
        verbose_name = "treatment"
        verbose_name_plural = "treatments"
    old_id = models.IntegerField("old_id", blank=True, null=True)
    # theoretically each treatment can have any number of deseases
    deseases = models.ManyToManyField("deseases.DeseaseItem",
        blank=True,
        verbose_name="deseases",
        related_name="treatments")
    mgr = TreatmentManager()
    objects = models.Manager()
