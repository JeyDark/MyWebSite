"""
WSGI config for MyWebSite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
sys.path.append('C:/xampp/htdocs/MyWebSite')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyWebSite.settings')

application = get_wsgi_application()
