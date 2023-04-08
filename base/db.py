
#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan

from contextlib import closing

from django.db import models, connection


def dictfetchall(cursor):
    """Return all rows from a cursor as a dict"""
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    return [] if row is None else dict(zip([col[0] for col in cursor.description], row))


class Default(models.Model):
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
        verbose_name = "default_date"


def error(code):
    sql = f"select * from api_error where code={code}"
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        res = dictfetchone(cursor)
        return res


