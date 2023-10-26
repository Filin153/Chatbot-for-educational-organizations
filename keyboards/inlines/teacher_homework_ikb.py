from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

write_homework_ikb = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Добавить/Изменить ДЗ', callback_data='write_homework'
            ),
        ],
        [
            InlineKeyboardButton(
                text='Посмотреть дз', callback_data='check_homework'
            ),
        ],
    ],
    resize_keyboard=True,
)


async def create_lessons_ikb(keys):
    lessons_ikb = InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    for lesson in keys:
        lessons_ikb.add(
            InlineKeyboardButton(text=lesson, callback_data=f'lesson_{lesson}')
        )
    lessons_ikb.add(
        InlineKeyboardButton(text='Отмена❌', callback_data='cancel_homework')
    )
    return lessons_ikb


async def create_groups_ikb(groups):
    groups_ikb = InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    for group in groups:
        groups_ikb.add(
            InlineKeyboardButton(text=group, callback_data=f'group_{group}')
        )
    groups_ikb.add(
        InlineKeyboardButton(text='Отмена❌', callback_data='cancel_homework')
    )
    return groups_ikb


cancel_homework_ikb = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [InlineKeyboardButton(text='Отмена❌', callback_data='cancel_homework')]
    ],
    resize_keyboard=True,
)


async def create_check_lessons_ikb(keys):
    lessons_ikb = InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    for lesson in keys:
        lessons_ikb.add(
            InlineKeyboardButton(
                text=lesson, callback_data=f'checklesson_{lesson}'
            )
        )
    lessons_ikb.add(
        InlineKeyboardButton(text='Отмена❌', callback_data='cancel_homework')
    )
    return lessons_ikb


async def create_check_groups_ikb(groups):
    groups_ikb = InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    for group in groups:
        groups_ikb.add(
            InlineKeyboardButton(
                text=group, callback_data=f'checkgroup_{group}'
            )
        )
    groups_ikb.add(
        InlineKeyboardButton(text='Отмена❌', callback_data='cancel_homework')
    )
    return groups_ikb
