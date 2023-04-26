
#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan


from rest_framework.authtoken import models as authtoken
from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.user import User
from helpbase.helper import generate_key


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
    extra = models.JSONField(default=dict({}))
    is_verified = models.BooleanField(default=False)
    step = models.CharField(max_length=25)

    created = models.DateTimeField(auto_now=False, auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def save(self, *args, **kwargs):
        if self.tries >= 3:
            self.is_expired = True
        if self.is_verified:
            self.is_expired = True
        return super(Otp, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.mobile} -> {self.key}"


class ExpiredToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="expired_access_token")
    key = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now=False, auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)



