# -*- coding: utf-8 -*-
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

def logoutview(request):
    logout(request)
    return redirect(reverse("deseases_index"))
