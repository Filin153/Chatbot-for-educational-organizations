from aiogram import filters, types

from keyboards import where_butt
from loader import dp
from scripts import msg_text
from scripts.help_to_handler import edit_or_answer, send_info


@dp.message_handler(filters.Text(equals='Инфо'))
async def info(message: types.Message):
    await message.delete()
    await edit_or_answer(message, 'Выберете:', where_butt)


@dp.callback_query_handler(text='priem_d')
async def med(call: types.CallbackQuery):
    await send_info(call, msg_text.PRIEM_D)


@dp.callback_query_handler(text='priem_kam')
async def kam(call: types.CallbackQuery):
    await send_info(call, msg_text.PRIEM_KAM)


@dp.callback_query_handler(text='tualet')
async def tualet(call: types.CallbackQuery):
    await send_info(call, msg_text.TUELET)


@dp.callback_query_handler(text='med')
async def med_punkt(call: types.CallbackQuery):
    await send_info(call, msg_text.MED)


@dp.callback_query_handler(text='eat')
async def eat(call: types.CallbackQuery):
    await send_info(call, msg_text.DININD_ROOM)


@dp.callback_query_handler(text='act')
async def act(call: types.CallbackQuery):
    await send_info(call, msg_text.ACT)


@dp.callback_query_handler(text='activ')
async def activ(call: types.CallbackQuery):
    await send_info(call, msg_text.ACTIV)


@dp.callback_query_handler(text='sport')
async def sport(call: types.CallbackQuery):
    await send_info(call, msg_text.SPORT)


@dp.callback_query_handler(text='ycheb')
async def ycheb(call: types.CallbackQuery):
    await send_info(call, msg_text.YCHEB)


@dp.callback_query_handler(text='tea')
async def tea(call: types.CallbackQuery):
    await send_info(call, msg_text.TEA)


@dp.callback_query_handler(text='smenka')
async def smenka(call: types.CallbackQuery):
    await send_info(call, msg_text.SMENKA)
