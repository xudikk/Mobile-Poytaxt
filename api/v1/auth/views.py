#  Xudikk Copyright (c) 2023/3/29.
#
#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan
import random

from base.error_messages import MESSAGE
from base.helper import generate_key, custom_response, code_decoder
import uuid
from rest_framework.response import Response
from django.conf import settings


def auth_one(requests, method, params):
    if 'phone' not in params:
        return custom_response(False, method=method, message=MESSAGE['ParamsNotFull'])

    code = random.randint(int(f'1{"0"*(settings.RANGE-1)}'), int('9'*settings.RANGE))
    # sms chiqib ketadi
    hash = code_decoder(code, l=settings.RANGE)

    return custom_response(True, data={
        "otp": code,
        "otp_token": hash
    }, method=method)


def auth_two(requests, method, params):
    pass


def login(requests, method, params):
    pass


def regis(requests, method, params):
    pass
