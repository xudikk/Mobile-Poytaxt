#  Xudikk  2023/3/29.
#
#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan


from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, phone, password, is_active=True, is_staff=False, is_superuser=False, **extra_fields):
        user = self.model(phone=phone, is_active=is_active, is_staff=is_staff, is_superuser=is_superuser,
                          **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password, **extra_fields):
        return self.create_user(phone, password, is_active=True, is_staff=True, is_superuser=True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(_('Phone'), unique=True, max_length=50)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    avatar = models.CharField(max_length=255, null=True)
    is_sms = models.BooleanField(default=False)

    is_test = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    identity = models.CharField(max_length=3, default='TT')
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name_plural = "1. Users"

    def personal(self):
        root = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'mobile': self.phone
        }
        sessions = Session.objects.filter(user=self, revoke=0, block=0)
        return {
            'user': root,
            "sessions": [x.res() for x in sessions]
        }


class Device(models.Model):
    # code
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="device")
    ip = models.CharField('Device ip', max_length=30, null=True)
    imei = models.CharField('Device imei', max_length=50, null=True)
    mac = models.CharField('Device mac', max_length=30, null=True)
    name = models.CharField('Device name', max_length=100, null=True)
    firebase_reg_id = models.CharField('Device firebase_reg_id', max_length=255, null=True)
    uuid = models.CharField('Device uuid', max_length=50)
    version = models.CharField('Device version', max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "10. Device"


class Session(models.Model):
    # code
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="session")
    name = models.CharField('Device name', max_length=100, null=True)
    uuid = models.CharField('Device uuid', max_length=128)
    revoke = models.IntegerField('Revoke', default=0)
    block = models.IntegerField('Block', default=0)
    primary = models.IntegerField('Primary', default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def res(self):
        return {
            'id': self.id,
            'name': self.name,
            'uuid': self.uuid
        }

    class Meta:
        verbose_name_plural = "11. Session"
