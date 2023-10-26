from aiogram import types, filters

from keyboards.bt_docs import docs_butt
from loader import dp
from scripts.help_to_handler import edit_or_answer


@dp.message_handler(filters.Text(equals="Документы"))
async def docs(message: types.Message):
    await message.delete()
    await edit_or_answer(message, "Выберете:", docs_butt)
