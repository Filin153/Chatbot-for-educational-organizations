from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

where_butt = InlineKeyboardMarkup()


tualet_b = InlineKeyboardButton('Tуалеты', callback_data='tualet')
med_b = InlineKeyboardButton('Медкабинет', callback_data='med')
eat_room_b = InlineKeyboardButton('Столовая', callback_data='eat')
actov_zal = InlineKeyboardButton('Актовый зал', callback_data='act')
activ_RKSI = InlineKeyboardButton('Актив РКСИ', callback_data='activ')
sport_zal = InlineKeyboardButton('Спортзал', callback_data='sport')
priem_d = InlineKeyboardButton('Приемная директора', callback_data='priem_d')
priem_kam = InlineKeyboardButton('Приемная камисия', callback_data='priem_kam')
ycheb_otdel = InlineKeyboardButton('Учебный отдел', callback_data='ycheb')
local_norm = InlineKeyboardButton(
    'Локально нормативные акты', url='https://www.rksi.ru/locals#teacher'
)

where_butt.add(priem_d, priem_kam).add(activ_RKSI, ycheb_otdel).add(
    med_b, local_norm
).add(actov_zal, eat_room_b).add(tualet_b, sport_zal)
