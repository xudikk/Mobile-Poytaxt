#  Xudikk  2023/3/29.
#
#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan

from rest_framework.response import Response

from base.error_messages import MESSAGE
from base.helper import custom_response


def method_and_params_checker(funk):
    def wrapper(self, requests, *args, **kwargs):
        params = requests.data.get('params')
        method = requests.data.get("method")

        if method is None:
            return Response(custom_response(status=False, message=MESSAGE['MethodMust']))

        if params is None:
            return Response(custom_response(status=False, message=MESSAGE['ParamsMust']))
        res = funk(self, requests, *args, **kwargs)
        return res
    return wrapper



