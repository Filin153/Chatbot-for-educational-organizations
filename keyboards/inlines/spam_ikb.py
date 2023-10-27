from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

spam_ikb = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Рассылка группе', callback_data='spam_group'
            )
        ],
        [
            InlineKeyboardButton(
                text='Рассылка преподавателям', callback_data='spam_teacher'
            )
        ],
    ],
    resize_keyboard=True,
)

cancel_spam_ikb = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [InlineKeyboardButton(text='Отмена❌', callback_data='cancel_spam')]
    ],
    resize_keyboard=True,
)
