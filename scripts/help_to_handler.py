import asyncio

from aiogram import types

from keyboards import where_butt
from keyboards.bt_send_schedule import day_key
from loader import bot
from scripts import check_prepod, take_all_group, take_all_prepod, true_teacher

timetodel = 10 * 60


async def edit_or_answer(message: types.Message, text, buttons=None):
    try:
        await message.edit_text(text, reply_markup=buttons, parse_mode='HTML')
    except Exception:
        await message.answer(text, reply_markup=buttons, parse_mode='HTML')


async def send_info(call: types.CallbackQuery, text: str):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    msg = await call.bot.send_message(
        call.message.chat.id, text, parse_mode='HTML'
    )
    await edit_or_answer(call.message, 'Выберете:', where_butt)
    await asyncio.sleep(timetodel)
    await msg.delete()


async def valid_data(
    id, data=None, today: bool = False, tomorow: bool = False
):
    try:
        if not data[f'name_{id}']:
            return await check_prepod(id=id, today=today, tomorow=tomorow)
        else:
            return await check_prepod(
                name=data[f'name_{id}'], today=today, tomorow=tomorow
            )
    except Exception:
        return await check_prepod(id=id, today=today, tomorow=tomorow)


async def take_g_or_p(res, message: types.Message):
    if not res:
        await message.answer('Выберите день', reply_markup=day_key)
        return True
    else:
        await message.answer(
            f'Похожие варианты:\n{"".join(res)}', parse_mode='HTML'
        )
        if true_teacher(message.from_user.id):
            await message.answer('Отправьте группу')
        else:
            await message.answer('Отправьте фамилию преподавателя')


async def take(data, key, message: types.Message):
    if true_teacher(message.from_user.id):
        return await take_all_group(data[key])
    else:
        return await take_all_prepod(data[key])
