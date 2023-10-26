from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup


menu = ReplyKeyboardMarkup(resize_keyboard=True)
# red_menu = InlineKeyboardMarkup()


supports_b = KeyboardButton('Тех.поддержка бота')
open_map_b = KeyboardButton('Открыть карту')
schedule = KeyboardButton('Расписание')
info = KeyboardButton("Инфо")
doc = KeyboardButton("Документы")
spam = KeyboardButton("Рассылка")
# spam = InlineKeyboardButton('Рассылка', callback_data='spam')
who = InlineKeyboardButton('Кто где когда')


menu.add(schedule).add(info).add(doc).add(spam)
# red_menu.add(schedule).add(open_map_b).add(who).add(supports_b).add(spam)