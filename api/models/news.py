#  Xudikk  2023/3/29.
#
#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan


from django.db import models

from api.models.user import User


class News(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    desc_uz = models.TextField()
    desc_en = models.TextField()
    desc_ru = models.TextField()
    body_uz = models.TextField()
    body_en = models.TextField()
    body_ru = models.TextField()
    image_uz = models.CharField(max_length=255)
    image_en = models.CharField(max_length=255)
    image_ru = models.CharField(max_length=255)
    link = models.CharField(max_length=255, null=True)
    viewed = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name_plural = "News"

    def res(self, user):
        news = NewsRead.objects.filter(user=user, news=self.id).first()
        if news:
            read = True
            liked = news.liked
        else:
            read = False
            liked = False
        return {
            'id': self.id,
            'title_uz': self.title_uz,
            'title_ru': self.title_ru,
            'title_en': self.title_en,
            'desc_uz': self.desc_uz,
            'desc_en': self.desc_en,
            'desc_ru': self.desc_ru,
            'body_uz': self.body_uz,
            'body_en': self.body_en,
            'body_ru': self.body_ru,
            'image_uz': self.image_uz,
            'image_en': self.image_en,
            'image_ru': self.image_ru,
            'link': self.link,
            'is_read': read,
            'is_like': liked,
            'viewed': self.viewed,
            'likes': self.likes,
            'created_at': self.created.strftime("%d %b, %Y"),
            'updated_at': self.updated.strftime("%d %b, %Y"),
        }


class NewsRead(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="news_read")
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="news")
    liked = models.BooleanField(default=False)
