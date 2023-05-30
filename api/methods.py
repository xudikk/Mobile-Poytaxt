
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
from api.v1.services.monitoring import monitoring_all, monitoring_one, sql_monitoring


""" Method Names Getter """

unusable_method = dir()


def method_names(requests, params):
    return cr(True, data=[x.replace('_', '.') for x in unusable_method if '__' not in x and x != 'cr'])
