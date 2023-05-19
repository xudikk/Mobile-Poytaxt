
#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan

from django.db.models import Sum, Q

from api.models import PaynetSave, TransferSave, Card
from api.models.news import NewsRead, News
from helpbase.helper import custom_response


def home(requests, params):
    user = requests.user
    sum_card = Card.objects.filter(~Q(type=3), ~Q(type=2), user=user).aggregate(Sum('balance'))
    usd_card = Card.objects.filter(type=2, user=user).aggregate(Sum('balance'))
    # identification = Identification.objects.filter(user=user).count()
    news_read = NewsRead.objects.filter(user=user).count()
    news = News.objects.all().count()

    transfer = TransferSave.objects.filter(user=user).order_by('-pk')[:3]
    paynet = PaynetSave.objects.filter(user=user).order_by('-pk')[:3]

    data = {'balance_sum': sum_card['balance__sum'] or 0,
            'balance_usd': usd_card['balance__sum'] or 0,
            # 'identification': bool(identification),
            'have_news': news > news_read,
            'transfer': [x.res() for x in transfer],
            'paynet': [x.res() for x in paynet],
            }
    return custom_response(status=True, data=data)
