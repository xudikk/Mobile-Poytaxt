
#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan

from helpbase import transfer_type


def get_description(state):
    if state == transfer_type.TRANSFER or state == transfer_type.COIN_TRANSFER:
        return {
            "uz": "O'tkazma",
            "ru": "Перевод денег",
            "en": "Transfer"
        }
    if state == transfer_type.PAYMENT:
        return {
            "uz": "To'lov",
            "ru": "Оплата",
            "en": "Payment"
        }
    if state == transfer_type.MTS_TRANSFER or state == transfer_type.TCB_TRANSFER or state == transfer_type.ARMENIA_TRANSFER or transfer_type.TURKEY_TRANSFER or transfer_type.KAZAKH_TRANSFER:
        return {
            "uz": "Xalqaro O'tkazma",
            "ru": "Международный перевод",
            "en": "International Transfer"
        }
    if state == transfer_type.MTS_PAYMENT:
        return {
            "uz": "Xalqaro To'lov",
            "ru": "Международный Оплата",
            "en": "International Payment"
        }
    if state == transfer_type.CONVERSION:
        return {
            "uz": "Valyuta ayriboshlash",
            "ru": "Kонвертация",
            "en": "Conversion"
        }
    return {
        "uz": "O'tkazma",
        "ru": "Перевод денег",
        "en": "Transfer"
    }
