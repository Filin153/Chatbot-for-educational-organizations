from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

do_teacher_ikb = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Добавить преподавателя', callback_data='add_teacher'
            )
        ],
        [
            InlineKeyboardButton(
                text='Удалить преподавателя', callback_data='delete_teacher'
            )
        ],
    ],
    resize_keyboard=True,
)

admin_schedule_ikb = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                'Расписание преподавателя', callback_data='prepod:p'
            ),
            InlineKeyboardButton(
                'Расписание группы', callback_data='prepod:g'
            ),
        ]
    ],
    resize_keyboard=True,
)

cancel_teacher_ikb = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [InlineKeyboardButton(text='Отмена❌', callback_data='cancel_teacher')]
    ],
    resize_keyboard=True,
)


async def create_for_delete_teachers(teachers):
    delete_teacher = InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    for teacher in teachers:
        delete_teacher.add(
            InlineKeyboardButton(text=teacher, callback_data=f'dt_{teacher}')
        )
    return delete_teacher


reset_password_ikb = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Сменить пароль', callback_data='reset_password'
            )
        ]
    ],
    resize_keyboard=True,
)

cancel_password_ikb = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [InlineKeyboardButton(text='Отмена❌', callback_data='cancel_password')]
    ],
    resize_keyboard=True,
)
