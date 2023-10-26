from aiogram import types, filters
import asyncio
from scripts import msg_text
from loader import bot, dp
from scripts.help_to_handler import edit_or_answer, send_info

@dp.callback_query_handler(text="send_file")
async def send_file(call: types.CallbackQuery, file):
    await bot.send_file(file=f"file/{file}")
    await edit_or_answer(call.message, "Выберете:")
