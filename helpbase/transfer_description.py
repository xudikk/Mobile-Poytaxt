
#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan

CREATED = 0
SUCCESS = 4
CANCELLED = 21


def get_description(state):
    if state == 0:
        return {
            "color": "#1976D2",
            "message": {
                "uz": "Yaratildi",
                "ru": "Создано",
                "en": "Created"
            }
        }
    if state == 4:
        return {
            "color": "#388E3C",
            "message": {
                "uz": "Muvaffaqiyatli",
                "ru": "Успех",
                "en": "Success"
            }
        }
    if state == 21:
        return {
            "color": "#d32f2f",
            "message": {
                "uz": "Bekor qilingan",
                "ru": "Отменено",
                "en": "Cancelled"
            }
        }
    return {
        "color": "#d32f2f",
        "message": {
            "uz": "Bekor qilingan",
            "ru": "Отменено",
            "en": "Cancelled"
        }
    }