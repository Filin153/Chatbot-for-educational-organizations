from keyboards import where_butt
from keyboards.inlines.start_ikb import cancel_ikb
from loader import bot
import asyncio
from aiogram import types
from keyboards.bt_send_schedule import day_key
from scripts import check_prepod, take_all_prepod, true_teacher, take_all_group

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
    await edit_or_answer(call.message, '📖Выберете:', where_butt)
    await asyncio.sleep(timetodel)
    await msg.delete()


async def valid_data(
    id, data=None, admin_key=None, today: bool = False, tomorow: bool = False
):
    try:
        if not data[f'name_{id}']:
            return await check_prepod(
                id=id, admin_key=admin_key, today=today, tomorow=tomorow
            )
        else:
            return await check_prepod(
                name=data[f'name_{id}'],
                admin_key=admin_key,
                today=today,
                tomorow=tomorow,
            )
    except Exception:
        return await check_prepod(
            id=id, admin_key=admin_key, today=today, tomorow=tomorow
        )


async def take_g_or_p(res, message: types.Message):
    if not res:
        await message.answer('Выберите день', reply_markup=day_key)
        return True
    else:
        await message.answer(
            f'Доступные варианты:\n{"".join(res)}', parse_mode='HTML'
        )
        if true_teacher(message.from_user.id):
            await message.answer(
                'Отправьте группу\n\nПример: ИС-28', reply_markup=cancel_ikb
            )
        else:
            await message.answer(
                'Отправьте ФИО преподавателя\n\nПример: Каламбет В.Б.',
                reply_markup=cancel_ikb,
            )


async def take(data, key, message: types.Message, admin_key=None):
    if admin_key == 'g':
        return await take_all_group(data[key])
    elif admin_key == 'p':
        return await take_all_prepod(data[key])
    elif true_teacher(message.from_user.id):
        return await take_all_group(data[key])
    else:
        return await take_all_prepod(data[key])
