from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup


schedule_buttons_g = InlineKeyboardMarkup()
today = InlineKeyboardButton('На сегодня', callback_data='today')
tomorrow = InlineKeyboardButton('На завтра', callback_data='tomorrow')
week = InlineKeyboardButton('На неделю', callback_data='week')
prepod = InlineKeyboardButton('Расписание преподавателя', callback_data='prepod')
schedule_buttons_g.add(today, tomorrow).add(week).add(prepod)


schedule_buttons_p = InlineKeyboardMarkup()
prepod_schedule_buttons = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
group = InlineKeyboardButton('Расписание группы', callback_data='prepod')
schedule_buttons_p.add(today, tomorrow).add(week).add(group)

day_key = InlineKeyboardMarkup()
day_key.add(today).add(tomorrow).add(week)

