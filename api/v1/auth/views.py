#  Xudikk  2023/3/29.
#
#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan
import datetime
import random

from dotenv import load_dotenv

from api.models import Otp, User, Token
from base.error_messages import MESSAGE
from base.helper import generate_key, custom_response, code_decoder
import uuid
from django.conf import settings

"""
    DIQQAT!!
        Bu yerda hech qaysi o'zgaruvchini va
        hech qaysi funksiyani o'zgartirish mumkin emas
"""


def auth_one(requests, method, params):
    if 'phone' not in params:
        return custom_response(False, method=method, message=MESSAGE['ParamsNotFull'])
    if len(str(params['phone'])) != 12:
        return custom_response(False, method=method, message=MESSAGE['LENPHONE'])

    otp = random.randint(int(f'1{"0" * (settings.RANGE - 1)}'), int('9' * settings.RANGE))
    # sms chiqib ketadi
    code = eval(settings.CUSTOM_HASHING)
    hash = code_decoder(code, l=settings.RANGE)
    token = Otp.objects.create(key=hash, mobile=params['phone'], step='one')

    return custom_response(True, data={
        "otp": otp,
        "token": token.key
    }, method=method)


def auth_two(requests, method, params):
    if 'otp' not in params or 'token' not in params:
        return custom_response(False, method=method, message=MESSAGE['ParamsNotFull'])
    otp = Otp.objects.filter(key=params['token']).first()
    if not otp:
        return custom_response(False, method=method, message=MESSAGE['OTPTokenError'])
    if otp.is_expired:
        return custom_response(False, method=method, message=MESSAGE['OTPExpired'])
    if (datetime.datetime.now() - otp.created).total_seconds() > 120:
        otp.step = 'two'
        otp.is_expired = True
        otp.save()
        return custom_response(False, method=method, message=MESSAGE['OTPExpired'])
    unhashed = code_decoder(otp.key, decode=True, l=settings.RANGE)
    code = eval(settings.UNHASH)
    if str(code) != str(params['otp']):
        otp.step = 'two'
        otp.tries += 1
        otp.save()
        return custom_response(False, method=method, message=MESSAGE['OtpError'])
    otp.is_verified = True
    otp.save()
    user = User.objects.filter(phone=otp.mobile).first()
    return custom_response(True, method=method, data={'is_registered': user is not None})


def login(requests, method, params):
    if 'phone' not in params or 'password' not in params or "token" not in params:
        return custom_response(False, method=method, message=MESSAGE['ParamsNotFull'])
    otp = Otp.objects.filter(key=params['token']).first()
    if not otp:
        return custom_response(False, method=method, message=MESSAGE['OTPTokenError'])
    user = User.objects.filter(phone=params['phone']).first()
    if not user:
        return custom_response(False, method=method, message=MESSAGE['UserNot'])
    check = {
        not user.is_active: custom_response(False, method=method, message=MESSAGE['UserDeleted']),
        not user.check_password(params['password']): custom_response(False, method=method,
                                                                     message=MESSAGE['PasswordError']),
        otp.mobile != str(params['phone']): custom_response(False, method=method,
                                                            message=MESSAGE['OTPPhoneAndPhoneNotMatch']),
        not otp.is_verified: custom_response(False, method=method, message=MESSAGE['TokenUnUsable']),

    }

    token = Token.objects.get_or_create(user=user)[0]

    return check.get(True, None) or custom_response(status=True, data={'access_token': token.key}, method=method)


def regis(requests, method, params):
    if 'phone' not in params or 'password' not in params or "token" not in params:
        return custom_response(False, method=method, message=MESSAGE['ParamsNotFull'])
    otp = Otp.objects.filter(key=params['token']).first()
    if not otp:
        return custom_response(False, method=method, message=MESSAGE['OTPTokenError'])
    









