#!/usr/bin/env python
# coding: utf-8

import os
import sys
from django.core.handlers.wsgi import WSGIHandler


# 将系统的编码设置为UTF8
reload(sys)
sys.setdefaultencoding('utf8')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = WSGIHandler()
# uwsgi --http :80 --chdir /var/www/mysite --module django_wsgi
