#  Xudikk Copyright (c) 2023/3/29.
#
#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan


from rest_framework.authtoken import models as authtoken
from django.db import models
from django.utils.translation import gettext_lazy as _
from base.helper import generate_key


class Token(authtoken.Token):
    key = models.CharField(_("Key"), primary_key=True, max_length=512)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = generate_key(100)
        return super(Token, self).save(*args, **kwargs)


class Otp(models.Model):
    key = models.CharField(max_length=512)
    mobile = models.CharField(max_length=20)
    is_expired = models.BooleanField(default=False)
    tries = models.SmallIntegerField(default=0)
    extra = models.JSONField(default={})
    is_verified = models.BooleanField(default=False)
    step = models.CharField(max_length=25)

    created = models.DateTimeField(auto_now=False, auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def save(self, *args, **kwargs):
        if self.tries >= 3:
            self.is_expired = True
        return super(Otp, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.key}-{self.mobile}"
