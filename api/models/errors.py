#  Xudikk  2023/3/29.
#
#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan


from django.db import models
from src import settings


class Error(models.Model):
    code = models.IntegerField('Error code', unique=True)
    alias = models.IntegerField('Alias Code from origin', null=True)
    origin = models.CharField('Origin', max_length=50, default=settings.APP_NAME)
    en = models.CharField("English", max_length=255)
    uz = models.CharField("O'zbekcha", max_length=255, null=True)
    ru = models.CharField("Русский", max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Xatoliklar"

