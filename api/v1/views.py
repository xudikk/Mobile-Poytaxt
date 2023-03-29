#  Xudikk Copyright (c) 2023/3/29.
#
#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan
import os

from api.models import Token
from base.costumizing import CustomBasicAuthentication, CustomGenericAPIView, BearerAuth
from base.decors import method_and_params_checker
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.conf import settings
from rest_framework.response import Response

from base.error_messages import MESSAGE
from base.helper import custom_response
from re import compile as re_compile
from api import v1


class PMView(CustomGenericAPIView):

    @method_and_params_checker
    def post(self, requests, *args, **kwargs):
        method = requests.data.get("method")
        params = requests.data.get("params")
        headers = requests.headers
        if method not in settings.METHODS:
            authorization = headers.get('Authorization', '')
            pattern = re_compile(r"Bearer (.+)")

            if not pattern.match(authorization):
                return Response(custom_response(status=False, method=method, message=MESSAGE['NotAuthenticated']))
            input_token = pattern.findall(authorization)[0]

            # Authorize
            try:
                token = Token.objects.get(key=input_token)
                requests.user = token.user
            except Token.DoesNotExist:
                return Response(custom_response(status=False, method=method, message=MESSAGE['AuthToken']))
        try:
            funk = getattr(v1, method.replace('.', '_').replace('-', '_'))
        except AttributeError:
            return Response(custom_response(False, method=method, message=MESSAGE['MethodDoesNotExist']))

        res = map(funk, [requests], [method], [params])
        return Response(list(res)[0])

