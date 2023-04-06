#  Xudikk  2023/3/29.
#
#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan


from api.models.news import News, NewsRead
from base.error_messages import MESSAGE
from base.helper import custom_response


def all_news(requests, params):
    news = [x.res() for x in News.objects.all().order_by('-pk')]
    return custom_response(True, data=news)


def single_news(requests, params):
    new = News.objects.filter(params.get('news_id', 0)).first()
    if not new: return custom_response(False, message=MESSAGE['NotData'])
    return custom_response(True, data=new.res())


def view_news(requests, params):
    new = News.objects.filter(id=params.get('news_id', 0)).first()
    if not new: return custom_response(False, message=MESSAGE['NotData'])
    new.viewed += 1
    new.save()
    NewsRead.objects.get_or_create(news=new, user=requests.user)
    return custom_response(True, data=new.res())


def like_news(requests, params):
    new = News.objects.filter(id=params.get('news_id', 0)).first()
    if not new: return custom_response(False, message=MESSAGE['NotData'])
    news_read = NewsRead.objects.get_or_create(news=new, user=requests.user)[0]
    if not news_read.liked:
        new.likes += 1
        news_read.liked = True
    else:
        new.likes -= 1
        news_read.liked = False

    new.save()
    news_read.save()
    return custom_response(True, data=new.res())



