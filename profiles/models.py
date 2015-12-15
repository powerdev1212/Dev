# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser
from . import fields

class MainUser(AbstractUser):

    is_admin = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)
    is_expert = models.BooleanField(default=False)
    is_physician = models.BooleanField(default=False)
    is_organization = models.BooleanField(default=False)
    timezone = models.CharField(default='', max_length='35', blank=True)
    registered = models.DateTimeField(blank=True, null=True)
    name = models.CharField(default='', max_length=120, blank=True)
#
    patient = models.CharField(max_length=30, default='', blank=True)
    organization = models.CharField(max_length=30, default='', blank=True)
    moderator = models.CharField(max_length=30, default='', blank=True)
    expert = models.CharField(max_length=30, default='', blank=True)
    run_once = models.BooleanField(default=False)
    socket_user_oid = models.CharField(max_length=30, default='', blank=True)
    created_it_id = models.IntegerField(default=0)
    pk_can_edit = fields.ListField(default=[], blank=True)
    pk_can_view = fields.ListField(default=[], blank=True)
    fhir_doc = models.CharField(max_length=30, default='', blank=True)
    paypal_transaction_id_new = fields.ListField(default=[], blank=True)
    paypal_transaction_id_old = fields.ListField(default=[], blank=True)
    #
    sharing_settings_for_coordinator = fields.DictionaryField(default={}, blank=True)
    sharing_settings_for_expert = fields.DictionaryField(default={ }, blank=True)
    sharing_settings_for_care_team = fields.DictionaryField(default={}, blank=True)
    login_failure_attempt = models.IntegerField(default=0)
    class Meta:
        app_label = "profiles"
