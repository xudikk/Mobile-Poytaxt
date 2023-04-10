
#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan

from api.models import Token
from base.costumizing import CustomGenericAPIView
from base.decors import method_and_params_checker
from django.conf import settings
from rest_framework.response import Response

from base.error_messages import MESSAGE
from base.helper import custom_response, exception_data
from re import compile as re_compile
from api import v1


class PMView(CustomGenericAPIView):
    """ Main Class | METHODIZM """
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
        except Exception as e:
            return Response(custom_response(False, method=method, message=MESSAGE['UndefinedError'],
                                            data=exception_data(e)))
        res = map(funk, [requests], [params])
        try:
            response = Response(list(res)[0])
            response.data.update({'method': method})
        except Exception as e:
            response = Response(custom_response(False, method=method, message=MESSAGE['UndefinedError'],
                                                data=exception_data(e)))
        return response

