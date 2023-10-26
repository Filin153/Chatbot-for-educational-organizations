from aiogram import types
import asyncio
from keyboards import menu
from loader import bot
from scripts import msg_text
from aiogram import types, filters
import asyncio
from scripts import msg_text
from keyboards import where_butt, menu
from loader import bot, dp

timetodel = 10*60

async def edit_or_answer(message: types.Message, text, buttons = None):
    try:
        await message.edit_text(text, reply_markup=buttons, parse_mode="HTML")
    except:
        await message.answer(text, reply_markup=buttons, parse_mode="HTML")

async def send_info(call: types.CallbackQuery, text: str):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    msg = await call.bot.send_message(call.message.chat.id, text, parse_mode='HTML')
    await edit_or_answer(call.message, "Выберете:", where_butt)
    await asyncio.sleep(timetodel)
    await msg.delete()
