from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def create_subjects_ikb(subjects):
    subjects_ikb = InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    for subject in subjects:
        subjects_ikb.add(
            InlineKeyboardButton(
                text=subject, callback_data=f'subject_{subject}'
            )
        )
    return subjects_ikb
