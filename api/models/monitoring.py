#  Xudikk  2023/3/29.
#
#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan
import uuid

import jsonfield
from django.db import models

from api.models import User
from base import helper, transfer_description, transfer_type_description, transfer_type


class Monitoring(models.Model):
    # code
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="monitoring")
    tr_id = models.CharField(max_length=255, null=True, unique=True)
    t_id = models.CharField(max_length=255, null=True)
    type = models.IntegerField(null=True)
    pay_type = models.IntegerField(null=True)
    sender_token = models.CharField(max_length=255, null=True)
    sender_number = models.CharField(max_length=100, null=True)
    sender_expire = models.CharField(max_length=10, null=True)
    sender_mask = models.CharField(max_length=100, null=True)
    receiver_token = models.CharField(max_length=255, null=True)
    receiver_number = models.CharField(max_length=100, null=True)
    receiver_mask = models.CharField(max_length=100, null=True)
    receiver_name = models.CharField(max_length=255, null=True)
    receiver = models.CharField(max_length=255, null=True)
    debit_state = models.CharField(max_length=64, null=True)
    debit_description = models.CharField(max_length=255, null=True)
    debit_amount = models.FloatField(null=True)
    debit_currency = models.CharField(max_length=10, null=True)
    credit_state = models.CharField(max_length=64, null=True)
    credit_description = models.CharField(max_length=255, null=True)
    credit_amount = models.FloatField(null=True)
    credit_currency = models.CharField(max_length=10, null=True)
    rate = models.FloatField(null=True)
    commission = models.FloatField(null=True)
    description = jsonfield.JSONField(null=True)
    type_description = jsonfield.JSONField(null=True)
    merchant = models.CharField(max_length=64, null=True)
    terminal = models.CharField(max_length=64, null=True)
    note = models.CharField(max_length=128, null=True)
    is_credit = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # created_at = models.DateTimeField(auto_now_add=False, null=True, editable=True)
    # updated_at = models.DateTimeField(auto_now_add=False, null=True, editable=True)

    def auto_save(self, user, sender, receiver_data, t_type, pay_type, com_type, amount, currency, note):
        expire = sender['expire']
        if com_type == 'uzcard_to_visa_sum' or com_type == 'humo_to_visa_sum' or com_type == 'visa_sum_to_uzcard' or \
                com_type == 'visa_sum_to_humo' or com_type == 'visa_sum_to_visa_sum':
            expire = expire[2:] + expire[0:2]
        commission = Commission.objects.filter(name=com_type).first()
        com = (commission.percentage * amount) / 100
        is_credit = 1
        if receiver_data['token']:
            is_credit = 2
        self.user = user
        self.tr_id = 'P_M_T_' + f"{uuid.uuid4()}"
        self.t_id = 'P_M_T_' + f"{uuid.uuid4()}"
        self.type = t_type
        self.pay_type = pay_type
        self.sender_token = sender['token']
        self.sender_number = sender['number']
        self.sender_expire = expire
        self.sender_mask = sender['mask']
        self.receiver_token = receiver_data['token']
        self.receiver_number = receiver_data['number']
        self.receiver_mask = helper.card_mask(receiver_data['number'])
        self.receiver = receiver_data['number']
        self.debit_state = transfer_description.CREATED
        self.debit_description = 'Created'
        self.debit_amount = amount
        self.debit_currency = currency
        self.credit_state = transfer_description.CREATED
        self.credit_description = 'Created'
        self.credit_amount = amount
        self.credit_currency = currency
        self.rate = 0
        self.commission = com
        self.description = transfer_description.get_description(transfer_description.CREATED)
        self.type_description = transfer_type_description.get_description(transfer_type.TRANSFER)
        self.merchant = commission.in_merchant
        self.terminal = commission.in_terminal
        self.note = note
        self.is_credit = is_credit
        self.save()

    def res(self):
        is_credit = False
        if self.is_credit == 2:
            is_credit = True
        return {
            'is_credit': is_credit,
            'tr_id': self.tr_id,
            'type': self.type,
            'pay_type': self.pay_type,
            'sender': {
                'token': self.sender_token,
                'number': self.sender_number,
                'expire': self.sender_expire,
                'mask': self.sender_mask,
            },
            'receiver': {
                'token': self.receiver_token,
                'number': self.receiver_number,
                'mask': self.receiver_mask,
                'receiver': self.receiver,
            },
            'debit': {
                'state': self.debit_state,
                'description': self.debit_description,
                'amount': self.debit_amount,
                'currency': self.debit_currency,
            },
            'credit': {
                'state': self.credit_state,
                'description': self.credit_description,
                'amount': self.credit_amount,
                'currency': self.credit_currency,
            },
            'rate': self.rate,
            'commission': self.commission,
            'description': self.description,
            'type_description': self.type_description,
            'merchant': self.merchant,
            'terminal': self.terminal,
            'created_at': self.created_at.strftime("%Y %d, %b %H:%M:%S"),
            'updated_at': self.updated_at.strftime("%Y %d, %b %H:%M:%S"),
        }

    class Meta:
        verbose_name_plural = "12. Monitoring"

    pass


class Commission(models.Model):
    name = models.CharField(max_length=128, null=True)
    in_merchant = models.CharField(max_length=64, null=True)
    in_terminal = models.CharField(max_length=64, null=True)
    in_terminal_account = models.CharField(max_length=128, null=True)
    out_merchant = models.CharField(max_length=64, null=True)
    out_terminal = models.CharField(max_length=64, null=True)
    out_terminal_account = models.CharField(max_length=128, null=True)
    percentage = models.FloatField(max_length=10, null=True, default=0.0)

    def res(self):
        return {
            'name': self.name,
            'percentage': self.percentage,
        }


class TransferSave(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transfer_save")
    sender = models.CharField(max_length=64, null=True)
    receiver = models.CharField(max_length=64, null=True)
    amount = models.FloatField(null=True)
    currency = models.IntegerField(null=True)
    type = models.IntegerField(null=True)
    pay_type = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def res(self):
        return {
            'id': self.id,
            'sender': self.sender,
            'receiver': self.receiver,
            'amount': self.amount,
            'currency': self.currency,
            'type': self.type,
            'pay_type': self.pay_type,
            'created_at': self.created.strftime("%Y %d, %b %H:%M:%S"),
            'updated_at': self.updated.strftime("%Y %d, %b %H:%M:%S")
        }


class PaynetSave(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="paynet_save")
    category_id = models.IntegerField(null=True)
    provider_id = models.IntegerField(null=True)
    service_id = models.IntegerField(null=True)
    fields = models.JSONField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def res(self):
        return {
            'id': self.id,
            'category_id': self.category_id,
            'provider_id': self.provider_id,
            'service_id': self.service_id,
            'fields': self.fields,
            'created_at': self.created.strftime("%Y %d, %b %H:%M:%S"),
            'updated_at': self.updated.strftime("%Y %d, %b %H:%M:%S")
        }
