#  Xudikk  2023/3/29.
#
#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan

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
    if state == 1 or state == 2:
        return {
            "color": "#4eac5b",
            "message": {
                "uz": "Jarayonda",
                "ru": "В ходе выполнения",
                "en": "In progress"
            }
        }
    if state == 3:
        return {
            "color": "#1a69f5",
            "message": {
                "uz": "Karta chiqish jarayonida",
                "ru": "Карта находится в процессе оформления",
                "en": "The card is in the process of registration"
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
    if state == -1 or state == -2 or state == -3:
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
