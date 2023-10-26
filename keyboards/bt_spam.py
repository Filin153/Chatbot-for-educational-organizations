from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


spam_butt = InlineKeyboardMarkup()

today = InlineKeyboardButton('Группа', callback_data='group_spam')
tomorrow = InlineKeyboardButton('Преподаватель', callback_data='prepod_spam')
week = InlineKeyboardButton('Личное', callback_data='int_spam')
prepod = InlineKeyboardButton('Всем', callback_data='all_spam')
spam_butt.add(today, tomorrow).add(week).add(prepod)

