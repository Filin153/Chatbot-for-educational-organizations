from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

departament_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Инфо'),
            KeyboardButton(text='Документы'),
        ],
        [KeyboardButton(text='Рассылка')],
        [
            KeyboardButton(text='Домашнее задание'),
            KeyboardButton(text='Расписание'),
        ],
    ],
    resize_keyboard=True,
)
