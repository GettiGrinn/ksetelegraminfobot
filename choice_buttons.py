from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup


user_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Котировки \U0001F4CA"),
            KeyboardButton(text="Итоги последних сделок \U0001F4DD"),

        ],
        [
            KeyboardButton(text="Индекс и капитализация"),
            KeyboardButton(text="Ценные бумаги"),
        ],
        [
            KeyboardButton(text="Уведомления")
        ],
    ],
    resize_keyboard=True
)

trade_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('\U0001F4CE Посмотреть торги по компаниям', callback_data='company')

    ]
])

notification_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Ценные бумаги', callback_data='notification_securities')


    ],
    [
        InlineKeyboardButton('Отключить уведомления', callback_data='notification_disable')
    ]
])
