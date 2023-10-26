from aiogram import types
from keyboards.bt_menu import menu
from loader import dp


@dp.message_handler(text='/start')
async def start(message: types.Message):
    await message.answer('Я бот', reply_markup=menu)
