#  Xudikk Copyright (c) 2023/3/29.
#
#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan


import requests
import json
from django.conf import settings


def post(mobile, text):
    payload = json.dumps({
        "method": "send",
        "params": [
            {
                "phone": mobile,
                "content": text
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + settings.EXTERNAL_TOKENS['sms']
    }

    response = requests.post(settings.EXTERNAL_URLS['sms'], headers=headers, data=payload)
    return response.json()