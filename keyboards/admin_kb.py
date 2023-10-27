from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

admin_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассылка')],
        [KeyboardButton(text='Расписание')],
        [
            KeyboardButton(text='Преподаватели'),
            KeyboardButton(text='Учебный отдел'),
        ],
        [KeyboardButton(text='Инфо'), KeyboardButton(text='Документы')],
    ],
    resize_keyboard=True,
)
