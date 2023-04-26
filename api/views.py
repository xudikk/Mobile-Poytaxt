from base.main import METHODIZM
from django.conf import settings

from api import methods
from api.models.tokens import Token


class PMView(METHODIZM):
    file = methods
    token_key = "Bearer"
    auth_headers = 'Authorization'
    token_class = Token
    not_auth_methods = settings.METHODS


