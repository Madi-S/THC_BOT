from telegram import InlineKeyboardMarkup, InlineKeyboardButton

from callbacks import *


def get_initial_keyboard():
    keyboard = (
        (
            InlineKeyboardButton('Кокшетау', callback_data=KOKSHETAU_CALLBACK)
        ),
        (
            InlineKeyboardButton('Щучинск', callback_data=SHUCHINSK_CALLBACK),
            InlineKeyboardButton('Боровое', callback_data=BOROVOE_CALLBACK)
        ),
        (
            InlineKeyboardButton('😈 Акции', callback_data=SALES_CALLBACK),
        ),
        (
            InlineKeyboardButton(
                'Хочу работать', callback_data=HIRING_CALLBACK),
        )
    )

    return InlineKeyboardMarkup(keyboard)


def get_kokshetau_keyboard():
    keyboard = (
        (
            InlineKeyboardButton('SORT_CALLBACK', callback_data=SORT_CALLBACK)
        ),
        (
            InlineKeyboardButton(
                'INDUS_CALLBACK', callback_data=INDUS_CALLBACK)
        ),
        (
            InlineKeyboardButton('TRIM_CALLBACK', callback_data=TRIM_CALLBACK)
        ),
        (
            InlineKeyboardButton(
                'CENTER_CALLBACK', callback_data=CENTER_CALLBACK)
        ),
        (
            InlineKeyboardButton(
                'SHPEK_CALLBACK', callback_data=SHPEK_CALLBACK)
        ),
        (
            InlineKeyboardButton('GASHISH_CALLBACK',
                                 callback_data=GASHISH_CALLBACK)
        ),
        (
            InlineKeyboardButton(
                'OTHER_CALLBACK', callback_data=OTHER_CALLBACK)
        ),
        (
            InlineKeyboardButton('BACK_CALLBACK', callback_data=BACK_CALLBACK)
        )
    )

    return InlineKeyboardMarkup(keyboard)


def get_shuchinsk_keyboard():
    keyboard = (
        (
            InlineKeyboardButton('SORT_CALLBACK', callback_data=SORT_CALLBACK)
        ),
        (
            InlineKeyboardButton(
                'INDUS_CALLBACK', callback_data=INDUS_CALLBACK)
        ),
        (
            InlineKeyboardButton('TRIM_CALLBACK', callback_data=TRIM_CALLBACK)
        ),
        (
            InlineKeyboardButton(
                'CENTER_CALLBACK', callback_data=CENTER_CALLBACK)
        ),
        (
            InlineKeyboardButton(
                'SHPEK_CALLBACK', callback_data=SHPEK_CALLBACK)
        ),
        (
            InlineKeyboardButton('GASHISH_CALLBACK',
                                 callback_data=GASHISH_CALLBACK)
        ),
        (
            InlineKeyboardButton(
                'OTHER_CALLBACK', callback_data=OTHER_CALLBACK)
        ),
        (
            InlineKeyboardButton('BACK_CALLBACK', callback_data=BACK_CALLBACK)
        )
    )


def get_borovoe_keyboard():
    keyboard = (
        (
            InlineKeyboardButton('SORT_CALLBACK', callback_data=SORT_CALLBACK)
        ),
        (
            InlineKeyboardButton(
                'INDUS_CALLBACK', callback_data=INDUS_CALLBACK)
        ),
        (
            InlineKeyboardButton('TRIM_CALLBACK', callback_data=TRIM_CALLBACK)
        ),
        (
            InlineKeyboardButton(
                'CENTER_CALLBACK', callback_data=CENTER_CALLBACK)
        ),
        (
            InlineKeyboardButton(
                'SHPEK_CALLBACK', callback_data=SHPEK_CALLBACK)
        ),
        (
            InlineKeyboardButton('GASHISH_CALLBACK',
                                 callback_data=GASHISH_CALLBACK)
        ),
        (
            InlineKeyboardButton(
                'OTHER_CALLBACK', callback_data=OTHER_CALLBACK)
        ),
        (
            InlineKeyboardButton('BACK_CALLBACK', callback_data=BACK_CALLBACK)
        )
    )
