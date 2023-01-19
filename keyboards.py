from telegram import InlineKeyboardMarkup, InlineKeyboardButton

from callbacks import *


def get_initial_keyboard():
    keyboard = (
        (
            InlineKeyboardButton('Кокшетау', callback_data=KOKSHETAU_CALLBACK)
        ),
        (
            InlineKeyboardButton('Щучинск', callback_data=KOKSHETAU_CALLBACK),
            InlineKeyboardButton('Боровое', callback_data=BOROVOE_CALLBACK)
        ),
        (
            InlineKeyboardButton('😈 Акции', callback_data=SALES_CALLBACK),
        ),
        (
            InlineKeyboardButton('Хочу работать', callback_data=HIRING_CALLBACK),
        ),
    )

    return InlineKeyboardMarkup(keyboard)
