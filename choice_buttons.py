from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup


user_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Котировки \U0001F4CA"),
            KeyboardButton(text="Итоги последних сделок \U0001F4DD"),

        ],
        [
            KeyboardButton(text="Индекс и капитализация")

        ],
    ],
    resize_keyboard=True
)

trade_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('По компаниям', callback_data='company')

    ]
])
