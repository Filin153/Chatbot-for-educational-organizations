from aiogram import types, filters
import asyncio
from scripts import msg_text
from keyboards.bt_docs import docs_butt
from loader import bot, dp
from scripts.help_to_handler import edit_or_answer, send_info

@dp.message_handler(filters.Text(equals="Документы"))
async def docs(message: types.Message):
    await message.delete()
    await edit_or_answer(message, "Выберете:", docs_butt)
