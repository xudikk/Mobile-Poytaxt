
#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan

from itertools import chain

from django.core.paginator import Paginator
from django.db.models import Q

from api.models import Monitoring
from base.error_messages import MESSAGE
from base.helper import custom_response


def monitoring_all(requests, params):
    count = params.get('count', 10)
    page = params.get('page', 1)
    monitoring_out = Monitoring.objects.filter(user=requests.user).all()
    monitoring_in = Monitoring.objects.filter(user=requests.user, is_credit=2).all()
    monitorings = list(chain(monitoring_out, monitoring_in))
    paginator = Paginator(monitorings, count)
    data = {
        "data": [x.collection() for x in list(paginator.page(page))],
        "per_page": paginator.per_page,
        "pages": paginator.num_pages,
        "total": paginator.count,
    }
    return custom_response(True, data=data)


def monitoring_one(requests, params):
    if 'token' not in params: return custom_response(False, message=MESSAGE['ParamsNotFull'])
    count = params.get('count', 10)
    page = params.get('page', 1)
    token = params['token']
    monitorings = Monitoring.objects.filter(sender_token=token)
    start = params.get('start', None)
    end = params.get('end', None)
    if not monitorings: return custom_response(False, message=MESSAGE['NotData'])
    if not start and not end: monitorings = Monitoring.objects.filter(Q(sender_token=token) | Q(receiver_token=token))
    if start and not end:
        monitorings = Monitoring.objects.filter(Q(sender_token=token) | Q(receiver_token=token), created_at__gte=start)
    if not start and end:
        monitorings = Monitoring.objects.filter(Q(sender_token=token) | Q(receiver_token=token), created_at__lte=end)
    if start and end:
        monitorings = Monitoring.objects.filter(Q(sender_token=token) | Q(receiver_token=token), created_at__gte=start,
                                                created_at__lte=end)

    paginator = Paginator(monitorings, count)
    data = {
        "data": [x.collection() for x in list(paginator.page(page))],
        "per_page": paginator.per_page,
        "pages": paginator.num_pages,
        "total": paginator.count,
    }
    return custom_response(True, data=data)

