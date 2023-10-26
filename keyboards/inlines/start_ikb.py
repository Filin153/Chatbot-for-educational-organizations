from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_ikb = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Студент', callback_data='study'),
            InlineKeyboardButton(
                text='Преподаватель', callback_data='teacher'
            ),
        ],
        [InlineKeyboardButton(text='Учебный отдел', callback_data='training_departament')]
    ],
    resize_keyboard=True,
)

cancel_ikb = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [InlineKeyboardButton(text='Отмена❌', callback_data='cancel')]
    ],
    resize_keyboard=True,
)
