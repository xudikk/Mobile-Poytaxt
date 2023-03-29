#  Xudikk Copyright (c) 2023/3/29.
#
#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan
from dotenv import load_dotenv
import os
from .views import PMView
from django.urls import path, include

load_dotenv()

urlpatterns = [
    eval(os.getenv('UNIQUE')),
]