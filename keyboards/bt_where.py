from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

where_butt = InlineKeyboardMarkup()


tualet_b = InlineKeyboardButton('Tуалеты', callback_data='tualet')
med_b = InlineKeyboardButton('Медкабинет', callback_data='med')
eat_room_b = InlineKeyboardButton('Столовая', callback_data='eat')
actov_zal = InlineKeyboardButton('Актовый зал', callback_data='act')
activ_RKSI = InlineKeyboardButton('Актив РКСИ', callback_data='activ')
sport_zal = InlineKeyboardButton('Спортзал', callback_data='sport')
ycheb_otdel = InlineKeyboardButton('Учебный отдел', callback_data='ycheb')

where_butt.add(tualet_b, med_b, eat_room_b).add(actov_zal, activ_RKSI, sport_zal).add(ycheb_otdel)
