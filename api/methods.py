
#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan


""" DIQQAT Bu yerda import qilganda * dan foydalanish mumkin emas
    Shunchaki yaratilgan funksiyani chaqirib qo'yishning o'zi yetadi. U ishlatilishi shart emas!
"""
from helpbase.helper import custom_response as cr

from api.v1.services.auth import regis, login, auth_one, auth_two, resent_otp
from api.v1.services.home import home
from api.v1.services.news import single_news, all_news, like_news, view_news
from api.v1.services.setting import user_info, check_pass, change_pass, logout, user_edit
from api.v1.services.monitoring import monitoring_all, monitoring_one


""" Method Names Getter """

unusable_method = cr(True, data=dir())


def method_names(requests, params):
    datas = []
    for i in unusable_method.get('data', []):
        if '__' not in i and i != 'cr':
            datas.append(i.replace('_', '.'))

    unusable_method.update({'data': datas})
    return unusable_method
