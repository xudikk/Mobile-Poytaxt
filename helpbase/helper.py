#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan
import binascii
import os
import base64
from django.conf import settings


def custom_response(status, data=None, message=None, method=None):
    if type(status) is not bool:
        status = False
    return {
        "Origin": settings.APP_NAME,
        "method": method,
        "status": status,
        "data": data,
        "message": message
    }


def exception_data(e):
    return {
        "value": f"""{str(type(e)).strip("<class '").strip("'>")} => {str(e.__str__())}""",
        "line": str(e.__traceback__.tb_lineno),
        "frame": str(e.__traceback__.tb_frame),
    }


def generate_key(rg=50):
    return binascii.hexlify(os.urandom(rg)).decode()


def code_decoder(code, decode=False, l=1):
    if decode:
        for i in range(l):
            code = base64.b64decode(code).decode()
        return code
    else:
        for i in range(l):
            code = base64.b64encode(str(code).encode()).decode()
        return code


def card_mask(number):
    return number[0:4] + ' **** **** ' + number[12:16]
