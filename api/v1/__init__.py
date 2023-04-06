#  Xudikk 2023/3/29.
#
#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan

""" DIQQAT Bu yerda import qilganda * dan foydalanish mumkin emas """
from base.helper import custom_response as custom_response_for_dirs

from api.v1.services.auth import regis, login, auth_one, auth_two
from api.v1.services.home import home
from api.v1.services.news import single_news, all_news, like_news, view_news
from api.v1.services.setting import user_info, check_pass, change_pass, logout, user_edit
from api.v1.services.monitoring import monitoring_all, monitoring_one

unusable_method = custom_response_for_dirs(True, data=dir())


def method_names(requests, params):
    datas = unusable_method.get('data', []).copy()
    for i in unusable_method.get('data', []):
        if '__' in i:
            datas.remove(i)
    unusable_method.update({'data': datas})
    return unusable_method
