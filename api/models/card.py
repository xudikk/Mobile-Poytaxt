#  Xudikk  2023/3/29.
#
#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan
from django.db import models
from django_softdelete.models import SoftDeleteModel

from api.models.user import User


class Card(SoftDeleteModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cards")
    name = models.CharField(max_length=128)
    balance = models.FloatField(max_length=128)
    number = models.CharField(max_length=128, default=0)
    expire = models.CharField(max_length=10)
    mask = models.CharField(max_length=128)
    token = models.CharField(max_length=128, null=True)
    card_owner = models.CharField(max_length=256, null=True)
    card_logo = models.CharField(max_length=128)
    bank_logo = models.CharField(max_length=128, null=True, blank=True)
    is_unired = models.IntegerField()
    is_primary = models.IntegerField()
    is_verified = models.IntegerField(default=0)
    card_registered_phone = models.CharField(max_length=50, null=True)
    is_salary = models.IntegerField()
    type = models.IntegerField()  # ?!  0-UZCARD  1-HUMO  2-VISA  3-TCB
    blocked = models.IntegerField(null=True)  # ?
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name_plural = "Cards"

    def res(self):
        return {
            'id': self.id,
            'user': self.user_id,
            'name': self.name,
            'balance': self.balance,
            'mask': self.mask,
            'number': self.number,
            'token': self.token,
            'expire_date': self.expire,
            'card_owner': self.card_owner,
            'card_logo': self.card_logo,
            'bank_logo': self.bank_logo,
            'is_unired': self.is_unired,
            'is_primary': self.is_primary,
            'is_verified': self.is_verified,
            'card_registered_phone': self.card_registered_phone,
            'is_salary': self.is_salary,
            'type': self.type,
            'blocked': self.blocked,
            'created_at': self.created.strftime("%d %b, %Y"),
            'updated_at': self.updated.strftime("%d %b, %Y"),
        }


class Form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="form")
    ext_id = models.CharField(max_length=128)
    status = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Form"
