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

from api.models import Otp, User, Token, Device, Session
from base.error_messages import MESSAGE
from base.helper import generate_key, custom_response, code_decoder
import uuid
from django.conf import settings

"""
    DIQQAT!!
        Bu yerda hech qaysi o'zgaruvchini va
        hech qaysi funksiyani o'zgartirish mumkin emas
"""


def auth_one(requests, params):
    if 'phone' not in params:
        return custom_response(False, message=MESSAGE['ParamsNotFull'])
    if len(str(params['phone'])) != 12:
        return custom_response(False, message=MESSAGE['LENPHONE'])

    otp = random.randint(int(f'1{"0" * (settings.RANGE - 1)}'), int('9' * settings.RANGE))
    # sms chiqib ketadi
    code = eval(settings.CUSTOM_HASHING)
    hash = code_decoder(code, l=settings.RANGE)
    token = Otp.objects.create(key=hash, mobile=params['phone'], step='one')

    return custom_response(True, data={
        "otp": otp,
        "token": token.key
    })


def auth_two(requests, params):
    if 'otp' not in params or 'token' not in params:
        return custom_response(False, message=MESSAGE['ParamsNotFull'])
    otp = Otp.objects.filter(key=params['token']).first()
    if not otp: return custom_response(False, message=MESSAGE['OTPTokenError'])
    if otp.is_expired: return custom_response(False, message=MESSAGE['OTPExpired'])
    if (datetime.datetime.now() - otp.created).total_seconds() > 120:
        otp.step, otp.is_expired = 'two', True
        otp.save()
        return custom_response(False, message=MESSAGE['OTPExpired'])
    unhashed = code_decoder(otp.key, decode=True, l=settings.RANGE)
    code = eval(settings.UNHASH)
    if str(code) != str(params['otp']):
        otp.step, otp.tries = 'two', otp.tries + 1
        otp.save()
        return custom_response(False, message=MESSAGE['OtpError'])
    otp.is_verified = True
    user = User.objects.filter(phone=otp.mobile).first()
    otp.step = 'login' if user else 'regis'
    otp.save()

    return custom_response(True, data={'is_registered': user is not None})


def regis(requests, params):
    if 'phone' not in params or 'password' not in params or "token" not in params or 'details' not in params:
        return custom_response(False, message=MESSAGE['ParamsNotFull'])
    otp = Otp.objects.filter(key=params['token']).first()
    if not otp: return custom_response(False, message=MESSAGE['OTPTokenError'])
    if not otp.step != 'regis': return custom_response(False, message=MESSAGE['TokenUnUsable'])
    if not otp.is_verified: return custom_response(False, message=MESSAGE['TokenUnUsable'])

    user = User.objects.create_user(phone=params['phone'], password=params['password'],
                                    first_name=params.get('first_name', ''), last_name=params.get('last_name', ''),
                                    email=params.get('email', ''), avatar='avatar', is_sms=False)
    token = Token.objects.create(user=user)
    device = Device.objects.create(
        user=user, ip=params['details'].get('ip', None), imei=params['details'].get('imei', None),
        mac=params['details'].get('mac', None), name=params['details'].get('name', None),
        uuid=params['details'].get('uuid', None), version=params['details'].get('version', None),
        firebase_reg_id=params['details'].get('firebase_reg_id', None),
    )
    session = Session.objects.create(user=user, name=device.name, uuid=device.uuid, primary=1)
    otp.step = 'registered'
    otp.save()
    return custom_response(status=True, data={'access_token': token.key, 'mobile': user.phone})


def login(requests, params):
    if 'phone' not in params or 'password' not in params or "token" not in params or 'details' not in params:
        return custom_response(False, message=MESSAGE['ParamsNotFull'])
    # otp check
    otp = Otp.objects.filter(key=params['token']).first()
    if not otp: return custom_response(False, message=MESSAGE['OTPTokenError'])
    if not otp.step != 'login': return custom_response(False, message=MESSAGE['TokenUnUsable'])

    if not otp.is_verified: return custom_response(False, message=MESSAGE['TokenUnUsable'])
    if otp.mobile != str(params['phone']): return custom_response(False, message=MESSAGE['OTPPhoneAndPhoneNotMatch'])
    # user check
    user = User.objects.filter(phone=params['phone']).first()
    if not user: return custom_response(False, message=MESSAGE['UserNot'])
    if not user.is_active: return custom_response(False, message=MESSAGE['UserDeleted'])
    if not user.check_password(params['password']): return custom_response(False, message=MESSAGE['PasswordError'])
    # create fixtures
    token = Token.objects.get_or_create(user=user)[0]
    device = Device.objects.create(
        user=user,
        ip=params['details'].get('ip', None),
        imei=params['details'].get('imei', None),
        mac=params['details'].get('mac', None),
        name=params['details'].get('name', None),
        uuid=params['details'].get('uuid', None),
        version=params['details'].get('version', None),
        firebase_reg_id=params['details'].get('firebase_reg_id', None),
    )
    session = Session.objects.filter(user=user, uuid=params['details'].get('uuid', '')).first()
    if session:
        session.user = user
        session.name = device.name
        session.save()
    else:
        Session.objects.create(user=user, name=device.name, uuid=device.uuid)
    otp.step = 'logged'
    otp.save()
    return custom_response(status=True, data={'access_token': token.key, 'mobile': user.phone})

