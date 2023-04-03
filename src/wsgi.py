"""
WSGI config for src project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""
#  Xudikk 2023/3/29.
#
#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan


import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

application = get_wsgi_application()
