
#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan
import os
from api.views import PMView, SqlPM
from django.urls import path

urlpatterns = [
    path('', PMView.as_view(), name='PM'),
    path('sql/', SqlPM.as_view(), name='SqlPM'),
]