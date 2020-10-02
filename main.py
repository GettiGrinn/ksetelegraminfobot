from aiogram.dispatcher.filters import Command, Text
from handlers import get_quontation, get_index, get_trade_results, get_company_trade_results, get_listing_result
from aiogram.types import Message, CallbackQuery
from choice_buttons import user_menu, trade_button
from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN
from telegram_bot_pagination import InlineKeyboardPaginator
from db_handlers import init_db, add_message

init_db()
bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)


@dp.message_handler(Command("start"))
async def show_menu(message: Message):
    await message.answer(text="Выберите из списка необходимую опцию\n", reply_markup=user_menu)
    add_message(message.from_user.id, message.text, message.date)


@dp.message_handler(Command("update"))
async def show_menu(message: Message):
    await message.answer(text="Выберите из списка необходимую опцию \n", reply_markup=user_menu)
    add_message(message.from_user.id, message.text, message.date)


@dp.message_handler(Text(equals=["Котировки \U0001F4CA", "Итоги последних сделок \U0001F4DD",
                    "Индекс и капитализация", "Ценные бумаги"]))
async def show_menu(message: Message):

    if message.text == 'Котировки \U0001F4CA':
        await send_character_page(message)
    elif message.text == 'Индекс и капитализация':
        await message.answer(get_index())
    elif message.text == 'Итоги последних сделок \U0001F4DD':
        await message.answer(get_trade_results(), reply_markup=trade_button)
    elif message.text == 'Ценные бумаги':
        await message.answer("Введите код ценной бумаги, для которой необходимо получить информацию. "
                             "Например,KENB,ZLKR или AYLB")

    else:
        await message.answer("Опция находится в разработке")

    add_message(message.from_user.id, message.text, message.date)


@dp.message_handler()
async def echo_message(message: Message):
    await message.answer(get_listing_result(message.text))
    add_message(message.from_user.id, message.text, message.date)


@dp.callback_query_handler(text_contains="company")
async def get_company_trade_info(callback_query: CallbackQuery):
    await callback_query.answer(cache_time=20)
    await callback_query.message.answer(get_company_trade_results())


@dp.callback_query_handler(text_contains="character")
async def process_callback_button1(callback_query: CallbackQuery):
    page = int(callback_query.data.split('#')[1])
    await bot.delete_message(
        callback_query.message.chat.id,
        callback_query.message.message_id
    )
    await send_character_page(callback_query.message, page)


async def send_character_page(message, page=1):
    paginator = InlineKeyboardPaginator(
        len(get_quontation()),
        current_page=page,
        data_pattern='character#{page}'
    )

    await bot.send_message(
        message.chat.id,
        get_quontation()[page-1],
        reply_markup=paginator.markup,
        parse_mode='Markdown'
    )

if __name__ == '__main__':
    executor.start_polling(dp)
