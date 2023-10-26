from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Инфо'),
            KeyboardButton(text='Документы'),
        ],
        [KeyboardButton(text='Расписание')],
        [KeyboardButton(text='Домашнее задание')],
    ],
    resize_keyboard=True,
)
