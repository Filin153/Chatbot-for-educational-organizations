from aiogram import types
from aiogram.types import InputFile
from loader import bot, dp
import os


@dp.callback_query_handler(lambda c: c.data.startswith('send_file:'))
async def send_doc(call: types.CallbackQuery):
    file = os.listdir('file')[int(call.data.split(':')[-1])]
    with open(f'file/{file}', 'rb') as file:
        input_file = InputFile(file)
        await bot.send_document(
            chat_id=call.message.chat.id, document=input_file
        )
    await bot.delete_message(call.from_user.id, call.message.message_id)
