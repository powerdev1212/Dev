# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from sekizai import context

#####################
from profiles.models import MainUser
from django.contrib.auth.models import check_password

class MainUserAuthBackend(object):
    def authenticate(self, username=None, password=None):
        user = MainUser.objects.get(username=username)
        if user.check_password(password):
            return user
        return None
        #except MainUser.DoesNotExist:
        #    return None

#####################

class LoginView(TemplateView):
    template_name = "others/login.html"
    
    def get_context_data(self, **kw):
        vdata = {}
        return vdata

    def post(self, request, **kw):
        ab = MainUserAuthBackend()
        uname = passw = False
        vdata = {}
        uname = request.POST.get("uname", False)
        passw = request.POST.get("upassw", False)
        user = authenticate(username=uname, password=passw)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse("deseases_index"))
        return render_to_response(
                                  self.template_name,
                                  vdata,
                                  context_instance=RequestContext(request)
                                  )
