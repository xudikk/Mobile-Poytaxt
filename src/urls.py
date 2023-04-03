#  Xudikk  2023/3/29.
#
#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan

import os

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from dotenv import load_dotenv

load_dotenv()


urlpatterns = [
    path('admin/', admin.site.urls),
    eval(os.getenv("API_URL")),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

