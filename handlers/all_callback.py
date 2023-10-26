from aiogram import types, Dispatcher
import asyncio
from scripts import msg_text

timetodel = 10*60

# @dp.callback_query_handler(text='where')
async def call_all(call: types.CallbackQuery):
    await call.message.edit_text('Выбери', reply_markup=where_main)

# @dp.callback_query_handler(text='tualet')
async def tualet(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    msg = await call.bot.send_message(call.message.chat.id, msg_text.TUELET, parse_mode='HTML')
    await rm(call)
    await asyncio.sleep(timetodel)
    await msg.delete()


# @dp.callback_query_handler(text='med')
async def med(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    msg = await call.bot.send_message(call.message.chat.id, msg_text.MED, parse_mode='HTML')
    await rm(call)
    await asyncio.sleep(timetodel)
    await msg.delete()

# @dp.callback_query_handler(text='eat')
async def eat(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    msg = await call.bot.send_message(call.message.chat.id, msg_text.DININD_ROOM, parse_mode='HTML')
    await rm(call)
    await asyncio.sleep(timetodel)
    await msg.delete()

# @dp.callback_query_handler(text='act')
async def act(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    msg = await call.bot.send_message(call.message.chat.id, msg_text.ACT, parse_mode='HTML')
    await rm(call)
    await asyncio.sleep(timetodel)
    await msg.delete()

# @dp.callback_query_handler(text='activ')
async def activ(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    msg = await call.bot.send_message(call.message.chat.id, msg_text.ACTIV, parse_mode='HTML')
    await rm(call)
    await asyncio.sleep(timetodel)
    await msg.delete()

# @dp.callback_query_handler(text='sport')
async def sport(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    msg = await call.bot.send_message(call.message.chat.id, msg_text.SPORT, parse_mode='HTML')
    await rm(call)
    await asyncio.sleep(timetodel)
    await msg.delete()

# @dp.callback_query_handler(text='ycheb')
async def ycheb(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    msg = await call.bot.send_message(call.message.chat.id, msg_text.YCHEB, parse_mode='HTML')
    await rm(call)
    await asyncio.sleep(timetodel)
    await msg.delete()

# @dp.callback_query_handler(text='tea')
async def tea(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    msg = await call.bot.send_message(call.message.chat.id, msg_text.TEA, parse_mode='HTML')
    await rm(call)
    await asyncio.sleep(timetodel)
    await msg.delete()

# @dp.callback_query_handler(text='smenka')
async def smenka(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    msg = await call.bot.send_message(call.message.chat.id, msg_text.SMENKA, parse_mode='HTML')
    await rm(call)
    await asyncio.sleep(timetodel)
    await msg.delete()

# @dp.callback_query_handler(text='where_sit')
async def call_where_sit(call: types.CallbackQuery):
    await call.message.edit_text('Выбери:', reply_markup=where_sit)

# @dp.callback_query_handler(text='komova')
async def komova(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    msg = await call.bot.send_message(call.message.chat.id, msg_text.KOMOVA, parse_mode='HTML')
    await rm(call)
    await asyncio.sleep(timetodel)
    await msg.delete()

# @dp.callback_query_handler(text='chlupkina')
async def chlupkina(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    msg = await call.bot.send_message(call.message.chat.id, msg_text.CHLUPKINA, parse_mode='HTML')
    await rm(call)
    await asyncio.sleep(timetodel)
    await msg.delete()


def reg_callback(dp: Dispatcher):
    dp.register_callback_query_handler(call_all, text='who')
    dp.register_callback_query_handler(call_where, text='where')
    dp.register_callback_query_handler(tualet, text='tualet')
    dp.register_callback_query_handler(med, text='med')
    dp.register_callback_query_handler(eat, text='eat')
    dp.register_callback_query_handler(act, text='act')
    dp.register_callback_query_handler(activ, text='activ')
    dp.register_callback_query_handler(sport, text='sport')
    dp.register_callback_query_handler(ycheb, text='ycheb')
    dp.register_callback_query_handler(tea, text='tea')
    dp.register_callback_query_handler(smenka, text='smenka')
    dp.register_callback_query_handler(call_where_sit, text='where_sit')
    dp.register_callback_query_handler(komova, text='komova')
    dp.register_callback_query_handler(chlupkina, text='chlupkina')