# -*- coding: utf-8 -*-
import platform
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


def set_socketpath():
    """ Setting correct path for mysql.sock depends on system """

    slack_sockpath = "/var/run/mysql/mysql.sock"
    deb_sockpath = "/var/run/mysqld/mysqld.sock"

    curr_platform = platform.platform()
    if "slackware" in curr_platform.lower():
        return slack_sockpath
    else:
        return deb_sockpath

# DATABASES = {
#    "default": {
#        "ENGINE": "django.db.backends.mysql",
#        "HOST": set_socketpath(),
#        "NAME": "hygeiais_sitedb",
#        "PASSWORD": "hyg$!site",
#        "PORT": "",
#        "USER": "hyg_site",
#    },
#}
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": "",
        "NAME": "hygeiais_sitedb",
        "PASSWORD": "1",
        "PORT": "",
        "USER": "djangouser",
    },
}
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'django.contrib.gis.db.backends.spatialite',  # 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}
"""
