#  Xudikk  2023/3/29.
#
#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan

from django.db.models import Sum, Q

from api.models import PaynetSave, TransferSave, Card
from api.models.news import NewsRead, News
from base.helper import custom_response


def home(requests, params):
    user = requests.user
    sum_card = Card.objects.filter(~Q(type=3), ~Q(type=2), user=user).aggregate(Sum('balance'))
    usd_card = Card.objects.filter(type=2, user=user).aggregate(Sum('balance'))
    unired_card = Card.objects.filter(is_unired=2, user=user).aggregate(Sum('balance'))
    mko_card = Card.objects.filter(type=29, user=user).aggregate(Sum('balance'))
    # identification = Identification.objects.filter(user=user).count()
    news_read = NewsRead.objects.filter(user=user)
    news = News.objects.all()
    new = False
    if news.count() > news_read.count():
        new = True

    transfer = TransferSave.objects.filter(user=user).order_by('-pk')[:3]
    paynet = PaynetSave.objects.filter(user=user).order_by('-pk')[:3]

    data = {'balance_sum': sum_card['balance__sum'],
            'balance_usd': usd_card['balance__sum'],
            'unired': unired_card['balance__sum'],
            'mko': mko_card['balance__sum'],
            # 'identification': bool(identification),
            'news': new,
            'transfer': [x.res() for x in transfer],
            'paynet': [x.res() for x in paynet],
            }
    return custom_response(status=True, data=data)
