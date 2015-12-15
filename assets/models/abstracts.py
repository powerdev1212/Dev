# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _

""" Abstract DB Model classes. """


class AbstractMini(models.Model):

    """ Abstract minimal. """
    created = models.DateTimeField(
        'created', auto_now_add=True, auto_now=False,
        blank=True, null=True)
    updated = models.DateTimeField('updated', auto_now=True,
                                   auto_now_add=False, blank=True, null=True)

    class Meta:
        abstract = True


class AbstractStandard(models.Model):

    """ Abstract standard (no 'rank' field) """
    created = models.DateTimeField('created',
                                   auto_now_add=True, auto_now=False,
                                   blank=True, null=True)
    updated = models.DateTimeField('updated',
                                   auto_now=True, auto_now_add=False,
                                   blank=True, null=True)
    active = models.BooleanField('in use',
                                 default=True)

    class Meta:
        abstract = True


# AbstractRanked
class AbstractRanked(models.Model):

    """ Abstract ranked """
    created = models.DateTimeField('created',
                                   auto_now_add=True, auto_now=False,
                                   blank=True, null=True)
    updated = models.DateTimeField('updated',
                                   auto_now=True, auto_now_add=False,
                                   blank=True, null=True)
    rank = models.IntegerField('rank', default=0)
    active = models.BooleanField('in use', default=True)

    class Meta:
        abstract = True


class AbstractStandardAPIFeatured(models.Model):

    """ Model with 'rank' field and set of common methods. """
    inner_name = models.CharField(max_length=200,
                                  blank=True,
                                  null=True,
                                  db_index=True)
    created = models.DateTimeField('created',
                                   auto_now_add=True, auto_now=False,
                                   blank=True, null=True)
    updated = models.DateTimeField('updated',
                                   auto_now=True, auto_now_add=False,
                                   blank=True, null=True)
    active = models.BooleanField('in use', default=True)

    def __unicode__(self):
        """ Better for Django if it works on Python 2.X """
        return _(self.inner_name)

    def __str__(self):
        """ For Python 2.X only """
        return self.__unicode__()

    def get_localized(self, lang_id=False):
        """ Get localized name of model. """
        if hasattr(self, "locales"):
            # custom localization issue(related <Locale> models)
            if lang_id:
                try:
                    return self.locales.get(lang__id=int(lang_id)).text
                except:
                    return self.__str__()
            return self.__str__()
        return self.__str__()

    @classmethod
    def get_by_parameters(cls, **kwargs):
        """ Get all model items have the **kwargs set of parameters. """
        try:
            return cls.objects.filter(**kwargs)
        except:
            return None

    def set_mnemo(self):
        """
        1. Our lowercased inner_name becomes a mnemo if one is not defined.
        2. Spaces are replaced by dashes if ones there are.
        """
        self.inner_name = self.inner_name.strip()
        if not self.mnemo:
            self.mnemo = self.inner_name.lower()
            try:
                self.mnemo = self.mnemo.replace(" ", "-")
            except:
                pass

    class Meta:
        abstract = True


class AbstractRankedAPIFeatured(models.Model):

    """ Model with 'rank' field and set of common methods. """
    inner_name = models.CharField(max_length=200,
                                  blank=True,
                                  null=True,
                                  db_index=True)
    created = models.DateTimeField(
        'created', auto_now_add=True, auto_now=False,
        blank=True, null=True)
    updated = models.DateTimeField('updated', auto_now=True,
                                   auto_now_add=False, blank=True, null=True)
    rank = models.IntegerField('rank', default=0)
    active = models.BooleanField('in use', default=True)

    def __unicode__(self):
        """ Better for Django if it works on Python 2.X """
        return _(self.inner_name)

    def __str__(self):
        """ For Python 2.X only """
        return self.__unicode__()

    def get_localized(self, lang_id=False):
        """ Get localized name of model. """
        if hasattr(self, "locales"):
            # custom localization issue(related <Locale> models)
            if lang_id:
                try:
                    return self.locales.get(lang__id=int(lang_id)).text
                except:
                    return self.__str__()
            return self.__str__()
        return self.__str__()

    @classmethod
    def get_by_parameters(cls, **kwargs):
        """ Get all model items have the **kwargs set of parameters. """
        try:
            return cls.objects.filter(**kwargs)
        except:
            return None

    def set_mnemo(self):
        """
        1. Our lowercased inner_name becomes a mnemo if one is not defined.
        2. Spaces are replaced by dashes if ones there are.
        """
        self.inner_name = self.inner_name.strip()
        if not self.mnemo:
            self.mnemo = self.inner_name.lower()
            try:
                self.mnemo = self.mnemo.replace(" ", "-")
            except:
                pass

    class Meta:
        abstract = True


# AbstractStringSlot
class AbstractStringSlot(models.Model):

    """ Abstract slot for string data. """
    text = models.CharField(
        max_length=150,
        blank=True,
        null=True)

    created = models.DateTimeField('created',
                                   auto_now_add=True,
                                   auto_now=False,
                                   blank=True,
                                   null=True)

    updated = models.DateTimeField('updated',
                                   auto_now=True,
                                   auto_now_add=False,
                                   blank=True,
                                   null=True)

    active = models.BooleanField('in use',
                                 default=True)

    class Meta:
        abstract = True

# AbstractTextSlot


class AbstractTextSlot(models.Model):

    """ Abstarct slot for text data. """
    text = models.TextField(
        max_length=10000,
        blank=True,
        null=True)

    created = models.DateTimeField('created',
                                   auto_now_add=True,
                                   auto_now=False,
                                   blank=True,
                                   null=True)

    updated = models.DateTimeField('updated',
                                   auto_now=True,
                                   auto_now_add=False,
                                   blank=True,
                                   null=True)

    active = models.BooleanField('in use',
                                 default=True)

    class Meta:
        abstract = True


# AbstractSmallTextSlot
class AbstractSmallTextSlot(models.Model):

    """ Abstract small slot for text data. """
    text = models.TextField(
        max_length=3000,
        blank=True,
        null=True)

    created = models.DateTimeField('created',
                                   auto_now_add=True,
                                   auto_now=False,
                                   blank=True,
                                   null=True)

    updated = models.DateTimeField('updated',
                                   auto_now=True,
                                   auto_now_add=False,
                                   blank=True,
                                   null=True)

    active = models.BooleanField('in use',
                                 default=True)

    class Meta:
        abstract = True


""" If django-ckeditor-updated is importable only."""
try:
    try:
        from ckeditor.fields import RichTextField
    except:
        raise ImportError('RichTextField was not imported!')

    class AbstractRichTextSlot(models.Model):

        """ Standard richtext slot. """
        text = RichTextField(
            config_name='standard_field',
            max_length=10000,
            blank=True,
            null=True)

        created = models.DateTimeField('created',
                                       auto_now_add=True,
                                       auto_now=False,
                                       blank=True,
                                       null=True)

        updated = models.DateTimeField('updated',
                                       auto_now=True,
                                       auto_now_add=False,
                                       blank=True,
                                       null=True)

        active = models.BooleanField('in use',
                                     default=True)

        class Meta:
            abstract = True

    # Текстовий слот для невеликих блоків тексту
    class AbstractSmallRichTextSlot(models.Model):

        """ Small richtext slot. """
        text = RichTextField(
            config_name='small_field',
            max_length=3000,
            blank=True,
            null=True)

        created = models.DateTimeField('created',
                                       auto_now_add=True,
                                       auto_now=False,
                                       blank=True,
                                       null=True)

        updated = models.DateTimeField('updated',
                                       auto_now=True,
                                       auto_now_add=False,
                                       blank=True,
                                       null=True)

        active = models.BooleanField('in use',
                                     default=True)

        class Meta:
            abstract = True
except:
    pass
