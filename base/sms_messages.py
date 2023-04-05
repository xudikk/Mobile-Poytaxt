#  Xudikk  2023/3/29.
#
#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan

def auth(code, lang):
    data = {
        'ru': f"Kode: {code}\n\nPoytaxt Mobile\nVnimaniye! Ne soobshyayte etot kod postoronnim.(Sotrudniki Poytaxt "
              f"NIKOGDA ne "
              "zaprashivayut kod) Etim mogut vospolzovatsya moshenniki!",
        'en': f"Code: {code}\n\nPoytaxt Mobile\nAttention! Do not share this code with others.(Poytaxt employees NEVER "
              f"ask for a "
              "code) Scammers can take advantage of this!",
        'uz': f"Kod: {code}\n\nPoytaxt Mobile\nOgoh bo'ling! Ushbu parolni hech kimga bermang.(Poytaxt xodimlari uni "
              f"HECH QACHON "
              "so'ramaydi) Firibgarlar foydalanishiga yo'l qo'ymang! ",
    }
    return data[lang]


def forget(code, lang):
    data = {
        'ru': f"Kode: {code}\n\nPoytaxt Mobile\nVnimaniye! Ne soobshyayte etot kod postoronnim.(Sotrudniki Poytaxt "
              f"NIKOGDA ne "
              "zaprashivayut kod) Etim mogut vospolzovatsya moshenniki!",
        'en': f"Code: {code}\n\nPoytaxt Mobile\nAttention! Do not share this code with others.(Poytaxt employees NEVER "
              f"ask for a "
              "code) Scammers can take advantage of this!",
        'uz': f"Kod: {code}\n\nPoytaxt Mobile\nOgoh bo'ling! Ushbu parolni hech kimga bermang.(Poytaxt xodimlari uni "
              f"HECH QACHON "
              "so'ramaydi) Firibgarlar foydalanishiga yo'l qo'ymang! ",
    }
    return data[lang]


def transfer(code, lang):
    data = {
        'ru': f"Kode: {code}\n\nPoytaxt Mobile\nVnimaniye! Ne soobshyayte etot kod postoronnim.(Sotrudniki Poytaxt "
              f"NIKOGDA ne "
              "zaprashivayut kod) Etim mogut vospolzovatsya moshenniki!",
        'en': f"Code: {code}\n\nPoytaxt Mobile\nAttention! Do not share this code with others.(Poytaxt employees NEVER "
              f"ask for a "
              "code) Scammers can take advantage of this!",
        'uz': f"Kod: {code}\n\nPoytaxt Mobile\nOgoh bo'ling! Ushbu parolni hech kimga bermang.(Poytaxt xodimlari uni "
              f"HECH QACHON "
              "so'ramaydi) Firibgarlar foydalanishiga yo'l qo'ymang! ",
    }
    return data[lang]
