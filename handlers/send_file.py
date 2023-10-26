from aiogram import types, filters
from aiogram.types import InputFile
import asyncio
from scripts import msg_text
from loader import bot, dp
from scripts.help_to_handler import edit_or_answer, send_info

@dp.callback_query_handler(lambda c: c.data.startswith('send_file:'))
async def send_doc(call: types.CallbackQuery):
    file = call.data.split(':')[-1]
    with open(f"file/{file}", "rb") as file:
        input_file = InputFile(file)
        await bot.send_document(chat_id=call.message.chat.id, document=input_file)
    await edit_or_answer(call.message, "Меню")
