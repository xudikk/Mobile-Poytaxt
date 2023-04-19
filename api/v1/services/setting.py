#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan

from api.models import Session, ExpiredToken, Token, User
from base.error_messages import MESSAGE
from base.helper import custom_response, exception_data
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


def check_pass(requests, params):
    if 'password' not in params or 'uuid' not in params:
        return custom_response(False, message=MESSAGE['ParamsNotFull'])

    if not requests.user.check_password(params['password']):
        return custom_response(False, message=MESSAGE['PasswordError'])
    session = Session.objects.filter(uuid=params['uuid']).first()
    if not session or session.block or session.revoke:
        return custom_response(False, message=MESSAGE['UUIDNotOrBlocked'])
    return custom_response(True, data={'access': True})


def user_info(requests, params):
    return custom_response(True, data=requests.user.personal())


def change_pass(requests, params):
    if 'password' not in params:
        return custom_response(False, message=MESSAGE['ParamsNotFull'])
    requests.user.set_password(params['password'])
    requests.user.save()
    return custom_response(True, data={'success': True})


def logout(requests, params):
    exp = ExpiredToken()
    tokens = Token.objects.filter(user=requests.user)
    if tokens:
        for x in tokens:
            exp.key, exp.user = x.key, x.user
            exp.save()
        tokens.delete()
        return custom_response(True, data={'success': True})
    return custom_response(False, message=MESSAGE['user_not'])


def remove_session(requests, params):
    if 'session_id' not in params: return custom_response(False, message=MESSAGE['ParamsNotFull'])
    session = Session.objects.filter(id=params['session_id'], revoke=0, block=0).first()
    if not session: return custom_response(False, message=MESSAGE['NotData'])
    if params.get('revoke', 0): session.revoke = 1
    if params.get('block', 0): session.block = 1
    session.save()
    return custom_response(True, data={'success': True})


def user_edit(request, params):
    try:
        ser = UserSerializer(data=params, instance=request.user, partial=True)
        ser.is_valid()
        user = ser.save()
        return custom_response(True, data=user.personal())
    except Exception as e:
        return custom_response(False, data=exception_data(e), message=MESSAGE['UndefinedError'])
