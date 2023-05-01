"""
WSGI config for web_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys

path = '/home/Tweek36/blog'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'blog.settings'


#from django.core.wsgi import get_wsgi_application
#
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_project.settings')

#application = get_wsgi_application()
#app = application

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
