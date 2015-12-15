# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _

from assets import models as am
from experts import models as exm
###############################################################################
###############################################################################


###############################################################################
class DeseaseTypeManager(models.Manager):
    """ Custom queries manager for DeseaseType model """
    def get_actives(self):
        return super(DeseaseTypeManager, self).get_queryset()\
        .filter(active=True)\
        .order_by("rank")
        
    def get_by_mnemo(self, mnemo):
        """ Get dtype by mnemo. """
        try:
            return super(DeseaseTypeManager, self).get_queryset()\
            .select_related()\
            .get(mnemo=mnemo, active=True)
        except:
            return None
        
class DeseaseType(am.AbstractRankedAPIFeatured):
    class Meta:
        verbose_name = "desease type"
        verbose_name_plural = "desease types"
    mnemo = models.CharField(max_length=150, blank=True,help_text="Mnemo name for type")
    objects = models.Manager()
    mgr = DeseaseTypeManager()
    
    def save(self, *args, **kwargs):
        """
        Custom before save options.
        1. Our lowercased inner_name becomes a mnemo if one is not defined.
        2. Spaces are replaced by dashes if ones there are.
        """
        self.inner_name = self.inner_name.strip()
        if not self.mnemo:
            self.mnemo = self.inner_name.lower()
            try:
                self.mnemo = self.mnemo.replace(" ","-")
            except:
                pass
        super(DeseaseType, self).save(*args, **kwargs)
###############################################################################


###############################################################################
class DeseaseItemManager(models.Manager):


    def get_by_categories_set(self,categs):
        #return super(DeseaseItemManager, self).get_queryset()\
        #.select_related()\
        #.get(active=True)
        if isinstance(categs,(tuple,list)):
            # revert data from view **kw
            categs.reverse()
        try:
            """ Try to get desease item with such type and category(-ies) """
            return super(DeseaseItemManager, self).get_queryset()\
            .select_related()\
            .filter(parent__mnemo__in=categs[1:], mnemo=categs[-1], active=True)[0]
        except:
            """ Try to get desease item with such type only if fails. """
            return super(DeseaseItemManager, self).get_queryset()\
            .select_related()\
            .filter(dtype__mnemo=categs[0], mnemo=categs[-1], active=True)[0]


    def get_uncategorized(self, dtype, not_in_ids):
        """ Get desease items which have no parent except main (desease type) """
        return super(DeseaseItemManager, self).get_queryset()\
        .filter(parent_categories__id__in=[dtype.id])\
        .exclude(parent_categories__id__in=not_in_ids, active=True)


    def get_by_mnemo(self, mnemo):
        """ Get category by mnemo. """
        try:
            return super(DeseaseItemManager, self).get_queryset()\
            .select_related()\
            .get(mnemo=mnemo)
        except:
            return None


    def get_categories_of_dtype(self, dtype):
        """ Getting items with no parent (categories) of exact type """
        return super(DeseaseItemManager, self).get_queryset()\
        .prefetch_related()\
        .filter(dtype__pk=dtype.id, active=True)\
        .filter(parent__isnull=True)\
        .order_by("id")


class DeseaseItem(am.AbstractRankedAPIFeatured):
    
    def __unicode__(self):
        return "{0} ({1})".decode("UTF-8").format(self.inner_name, str(self.id))

    """ DeseaseItem data model. """
    class Meta:
        verbose_name = _("desease")
        verbose_name_plural = _("deseases")
        permissions = (
                       ("can_view_hs_info","Can view info for health specialist"),
                       ("can_view_patient_info","Can view info for patient"),
                       )

    dtype = models.ForeignKey(DeseaseType,
        null=True,
        verbose_name="desease type",
        related_name="items",
        )
    mnemo = models.CharField(
        db_index=True,
        max_length=150,
        blank=True,
        help_text="Mnemo name for item")
    # search terms
    pubmed_terms = models.ManyToManyField("taxonomy.Term",
        related_name="in_terms_for_items",
        blank=True)
    # shot text data
    definition = models.TextField("definition",
        max_length=500,
        blank=True)
    # synonym terms
    synonyms = models.ManyToManyField("self",
        related_name="in_synonyms_for_items",
        blank=True)
    icd0_codes = models.CharField("ICD-O codes",max_length=150, blank=True)
    icd10_codes = models.CharField("ICD-10 Code",max_length=150, blank=True)
    omim_number = models.TextField("OMIM number", blank=True)
    mesh = models.TextField("MESH", blank=True)
    umls = models.TextField("UMLS", blank=True)
    med_dpa = models.TextField("MedDRA", blank=True)
    parent = models.ForeignKey("self",
        verbose_name="parent items",
        related_name="children",
        blank=True,
        null=True
        )
    old_id = models.IntegerField("old_id",blank=True,null=True)
    old_parent = models.IntegerField("old_parent",blank=True,null=True)
    patient_version = models.TextField("Patient Version", blank=True)
    genes_and_protiens = models.TextField("Genes involved and protiens", blank=True)
    detailed_definition = models.TextField("Detailed Definition", blank=True)
    risk_of_progression = models.TextField("Risk of progression", blank=True)
    epidemiology = models.TextField("Epidemiology", blank=True)
    sites = models.TextField("Sites of involvement", blank=True)
    clinical_features = models.TextField("Clinical Features", blank=True)
    grading = models.TextField("Grading", blank=True)
    etiology = models.TextField("Aetiology", blank=True)
    macroscopy = models.TextField("Macroscopy", blank=True)
    histopathology = models.TextField("Histopathology", blank=True)
    immunoprofile = models.TextField("Immunoprofile", blank=True)
    immunophenotype = models.TextField("Immunophenotype", blank=True)
    histogenesis = models.TextField("Histogenesis", blank=True)
    ultrastructure = models.TextField("Ultrastructure", blank=True)
    genetics = models.TextField("Genetics", blank=True)
    cytogenetics = models.TextField("Cytogenetics", blank=True)
    prognostic_factors = models.TextField("Prognostic and predictive Factors", blank=True)
    differential_diagnosis = models.TextField("Differential Diagnosis", blank=True)
    genetic_alterations = models.TextField("Genetic alterations", blank=True)
    # specialties
    # expert_reference = models.ManyToManyField("experts.Expert",
    #    blank=True,
    #    verbose_name="Experts",
    #    related_name="specialities")
    related_items = models.ManyToManyField("self", verbose_name="Related Items")
    hp_reference_file = models.FileField("References", upload_to="files/hp_reference", blank=True)
    nccn_treatment_patient = models.CharField("NCCN Treatment Patient", max_length=150, blank=True)
    nccn_treatment_hp = models.CharField("NCCN Treatment HP", max_length=150, blank=True)
    nccn_treatment = models.CharField("NCCN Treatment", max_length=150, blank=True)
    slideshow_field = models.CharField("Slideshow Field", max_length=150, blank=True)
    hp_slideshow = models.CharField("HP Slideshow", max_length=150, blank=True)
    # custom manager
    mgr = DeseaseItemManager()
    objects = models.Manager()
    
    def has_taxonomy_terms(self):
        """ Test if item has taxonomy terms. """
        terms = [t.inner_name for t in self.pubmed_terms.all()]
        return ", ".join(terms) if terms else "No terms"
    has_taxonomy_terms.short_description="Taxon. terms"
    
    def has_synonyms(self):
        """ Show synonyms of the desease item """
        synonyms = [i.inner_name for i in self.synonyms.all()]
        return ", ".join(synonyms) or "No synonyms"
    has_synonyms.short_description="Synonyms"
    
    def count_experts(self):
        c = 0
        # only current node synonyms
        for synonym in self.synonyms.filter(active=True):
            for term in synonym.pubmed_terms.filter(active=True):
                c += term.experts_researching_this.filter(active=True).count()
        def _count_experts(node, c):
            for term in node.pubmed_terms.filter(active=True):
                c += term.experts_researching_this.filter(active=True).count()
            #node parent
            if node.parent:
                _count_experts(node.parent, c)
        _count_experts(self, c)
        return c
    count_experts.short_description = "Experts for topic (num.)"
    
    @property
    def get_children(self):
        """ Returns all active children by its rank or [] """
        return DeseaseItem.objects.select_related().filter(parents__pk=self.id, active=True)
    
    def get_path(self):
        paths = []
        def _get_path(node, arr):
            arr.append(node.mnemo)
            if not node.parent is None:
                _get_path(node.parent, arr)
        _get_path(self, paths)
        paths.append(self.dtype.mnemo)
        paths.reverse()
        return "/".join(["/browse"] + paths)
        
    def get_bcrs(self):
        bcrs = []
        def _get_bcr(node, arr):
            arr.append([node.inner_name, node.get_path()])
            if node.parent:
                _get_bcr(node.parent, arr)
        _get_bcr(self, bcrs)
        bcrs.reverse()
        return bcrs

    def get_experts(self, **kw):
        """ Retrieve experts for the desease """
        experts = []
        synonyms = []
        # only current node synonyms
        #for synonym in self.synonyms.filter(active=True):
        #    synonyms.append(synonym.id)
        #    for term in synonym.pubmed_terms.filter(active=True):
        #        experts.extend([i for i in term.experts_researching_this\
        #                        .filter(active=True) if not i in experts])
            
        def _get_experts(node, stack, synonyms, **kw):
            """ recursive function for search in parents """
            # node itself
            for term in node.pubmed_terms.filter(active=True):
                experts_by_term = \
                term.experts_researching_this\
                .filter(active=True)\
                .order_by("seniority", "rank")
                if kw:
                    experts_by_term.filter(**kw)
                stack.extend([i for i in experts_by_term if not i in stack])
            synsQ = node.synonyms.filter(active=True).exclude(pk__in=synonyms)
            if synsQ.exists():
                for synonym in synsQ:
                    synonyms.append(synonym.id)
                    for term in synonym.pubmed_terms.filter(active=True):
                        experts_by_term = \
                        term.experts_researching_this\
                        .filter(active=True)\
                        .order_by("seniority", "rank")
                        if kw:
                            experts_by_term.filter(**kw)
                        experts.extend([i for i in experts_by_term if not i in experts])
                
            #node parent
            if node.parent:
                _get_experts(node.parent, stack, synonyms, **kw)
        _get_experts(self, experts, synonyms, **kw)
        
        # self.pubmed_terms
        # for term in self.pubmed_terms.filter(active=True):
        #    for i in term.experts_researching_this.filter(active=True):
        #        experts.append(i)
        # self.synonym
        # experts with empty speciality
        
        #experts.extend([i for i in exm.Expert.objects.filter(clinical_expertises__isnull=True, active=True, **kw).order_by("seniority", "rank")])
        return experts

    def get_related_items(self):
        """ Get self.related_items + self.parent(recursively) """
        related_items = []
        excluded_ids = []
        def _get_related_items(node, related_items, excluded_ids):
            excluded_ids.append(node.id)
            
            def _get_parents(node,related_items,excluded_ids):
                related_items.append(node)
                excluded_ids.append(node.id)
                if node.parent:
                    _get_parents(node.parent, related_items, excluded_ids)
            
            # siblings for node with parent
            siblings = \
            DeseaseItem.objects\
            .filter(parent_id=node.parent_id)\
            .exclude(pk__in=excluded_ids)
            for s in siblings:
                related_items.append(s)
                excluded_ids.append(s.id)
            if node.parent:
                _get_parents(node.parent, related_items, excluded_ids)
                # recursion for parent
                #_get_related_items(node.parent, related_items, excluded_ids)
                
            # node children
            #if node.children:
            #    for child in node.children.filter(active=True)\
            #    .exclude(pk__in=excluded_ids):
            #        # recursion for children
            #        _get_related_items(child, related_items, excluded_ids)
            # node itself
            #for i in node.related_items.filter(active=True)\
            #.exclude(pk__in=excluded_ids):
            #    # item itself
            #    related_items.append(i)

            #    # siblings for item with parent
            #    if i.parent:
            #        siblings = \
            #        DeseaseItem.objects\
            #        .filter(parent_id=i.parent_id)\
            #        .exclude(pk__in=excluded_ids)
            #        for s in siblings:
            #            related_items.append(s)
            #            excluded_ids.append(s.id)
            #        
            #        # recursion for parent
            #        _get_related_items(i.parent, related_items, excluded_ids)

            #    # item children
            #    if i.children:
            #        for child in i.children.filter(active=True)\
            #        .exclude(pk__in=excluded_ids):
            #            # recursion for children
            #            _get_related_items(child, related_items, excluded_ids)

        _get_related_items(self, related_items, excluded_ids)

        related_items = sorted(set(related_items), key=lambda i:i.inner_name)
        return related_items

    def get_support_groups(self):
        """ Get support groups for item """
        support_groups = []
        excluded_ids = []
        def _get_support_groups(node, support_groups, excluded_ids):
            excluded_ids.append(node.id)
                
            # node itself
            for sgroup in node.resources.filter(active=True):
                support_groups.append(sgroup)

            # node parent
            if node.parent:
                # recursion for parent
                _get_support_groups(node.parent, support_groups, excluded_ids)
        _get_support_groups(self, support_groups, excluded_ids)
        
        support_groups = sorted(set(support_groups), key=lambda i:i.inner_name)
        return support_groups

    def save(self, *args, **kwargs):
        """
        Custom before save options.
        1. Our lowercased inner_name becomes a mnemo if one is not defined.
        2. Spaces are replaced by dashes if ones there are.
        """
        """
        self.inner_name = self.inner_name.strip()
        if not self.mnemo:
            self.mnemo = self.inner_name.lower()
            try:
                self.mnemo = self.mnemo.replace(" ","-")
            except:
                pass
        """
        self.set_mnemo()
        super(DeseaseItem, self).save(*args, **kwargs)
###############################################################################


class DeseaseSynonym(am.AbstractStandardAPIFeatured):
    """ Synonyms for DeseaseItems. """
    class Meta:
        verbose_name = "synonym"
        verbose_name_plural = "synonyms"


class PatientVersionUrl(am.AbstractStandard):
    """ Patient versions URL """
    class Meta:
        verbose_name = "Patient_Version_URL"
        verbose_name_plural = "Patient_Version_URLs"
    '''
    category = models.ForeignKey(DeseaseCategory,
        null=True,
        blank=True,
        related_name="patient_version_url",
        verbose_name="desease item")
    '''
    item = models.ForeignKey(DeseaseItem,
                             blank=True,
                             related_name="patient_version_url",
                             verbose_name="desease item")
    link = models.URLField("URL", max_length=150, blank=True, null=True)


class PatientVersionImage(am.AbstractRanked):
    """ Patient versions Image """
    class Meta:
        verbose_name = "Patient_Version_Image"
        verbose_name_plural = "Patient_Version_Images"
    '''
    category = models.ForeignKey(DeseaseCategory,
        null=True,
        blank=True,
        related_name="patient_version_images",
        verbose_name="desease item")
    '''
    item = models.ForeignKey(DeseaseItem,
                             blank=True,
                             related_name="patient_version_images",
                             verbose_name="desease item")
    image = models.ImageField("Image",
                              upload_to="images/patients/versions",
                              blank=True)


class DeseaseImage(am.AbstractRanked):
    """ Desease Image """
    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
    '''
    category = models.ForeignKey(DeseaseCategory,
        null=True,
        blank=True,
        related_name="images",
        verbose_name="desease item")
    '''
    item = models.ForeignKey(DeseaseItem,
                             blank=True,
                             related_name="images",
                             verbose_name="desease item")
    image = models.ImageField("Image", upload_to="images/deseases", blank=True)
