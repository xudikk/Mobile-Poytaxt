from methodism.main import METHODISM, SqlAPIMethodism
from django.conf import settings

from api import sql_methods, methods
from api.models.tokens import Token


class PMView(METHODISM):
    file = methods
    token_class = Token
    not_auth_methods = settings.METHODS


class SqlPM(SqlAPIMethodism):
    file = sql_methods
    token_class = Token
    not_auth_methods = settings.METHODS
