from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


menu = InlineKeyboardMarkup()
red_menu = InlineKeyboardMarkup()


supports_b = InlineKeyboardButton('Тех.поддержка бота', callback_data='supports')
open_map_b = InlineKeyboardButton('Открыть карту', callback_data='open_map')
schedule = InlineKeyboardButton('Расписание', callback_data='schedule')
spam = InlineKeyboardButton('Рассылка', callback_data='spam')
who = InlineKeyboardButton('Кто где когда', callback_data='who')


menu.add(schedule).add(open_map_b).add(who).add(supports_b)
red_menu.add(schedule).add(open_map_b).add(who).add(supports_b).add(spam)