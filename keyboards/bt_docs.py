from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

docs_butt = InlineKeyboardMarkup()

norm_act = InlineKeyboardButton(
    'Нормативные акты', url='https://www.rksi.ru/locals#teacher'
)
zapis = InlineKeyboardButton(
    'Пример отправки файла', callback_data='send_file:1.pdf'
)

docs_butt.add(norm_act).add(zapis)
