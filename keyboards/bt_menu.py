from aiogram.types import (
    InlineKeyboardButton,
    KeyboardButton,
    ReplyKeyboardMarkup,
)


menu = ReplyKeyboardMarkup(resize_keyboard=True)


supports_b = KeyboardButton('Тех.поддержка бота')
open_map_b = KeyboardButton('Открыть карту')
schedule = KeyboardButton('Расписание')
info = KeyboardButton('Инфо')
doc = KeyboardButton('Документы')
spam = KeyboardButton('Рассылка')
who = InlineKeyboardButton('Кто где когда')


menu.add(schedule).add(info).add(doc).add(spam)
