from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def create_subjects_ikb(subjects):
    subjects_ikb = InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    for subject in subjects:
        subjects_ikb.add(
            InlineKeyboardButton(
                text=subject, callback_data=f'st_{subject}'
            )
        )
    return subjects_ikb


async def create_date_ikb(dates, subject):
    date_ikb = InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    for date in dates:
        date_ikb.add(
            InlineKeyboardButton(
                text=date, callback_data=f'_{date}_{subject}'
            )
        )
    return date_ikb
