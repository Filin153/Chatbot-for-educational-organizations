import asyncio

from aiogram import filters, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from keyboards.bt_send_schedule import schedule_buttons_g, schedule_buttons_p
from loader import dp
from scripts import true_teacher
from scripts.help_to_handler import (
    edit_or_answer,
    take,
    take_g_or_p,
    valid_data,
)
from take_schedule_from_RKSI.make_schedule import MakeSchedule


class SendName(StatesGroup):
    last_name = State()


@dp.message_handler(filters.Text(equals='Расписание'))
async def watch_schedule(message: types.Message):
    _, msg_schedule = await valid_data(id=message.from_user.id, today=True)

    await message.delete()
    if true_teacher(message.from_user.id):
        await edit_or_answer(message, msg_schedule, schedule_buttons_p)
    else:
        await edit_or_answer(message, msg_schedule, schedule_buttons_g)


@dp.callback_query_handler(text='week')
async def send_schedule_week(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        buttons, msg_schedule = await valid_data(
            data=data, id=call.message.chat.id
        )

        try:
            del data[f'name_{call.message.chat.id}']
        except Exception:
            pass

        try:
            await call.message.edit_text(
                str(msg_schedule), reply_markup=buttons, parse_mode='HTML'
            )
        except Exception:
            msg = MakeSchedule().share_msg(msg_schedule)
            firsttext = await call.message.edit_text(
                next(msg), parse_mode='HTML'
            )
            await call.message.answer(
                next(msg), reply_markup=buttons, parse_mode='HTML'
            )
            try:
                delmsg = await firsttext.reply('Удалится через 2 мин')
                await asyncio.sleep(120)
                await delmsg.delete()
                await firsttext.delete()
            except Exception:
                pass


@dp.callback_query_handler(text='today')
async def send_schedule_today(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        buttons, msg_schedule = await valid_data(
            data=data, id=call.message.chat.id, today=True
        )

        try:
            del data[f'name_{call.message.chat.id}']
        except Exception:
            pass

        await call.message.edit_text(
            str(msg_schedule), reply_markup=buttons, parse_mode='HTML'
        )


@dp.callback_query_handler(text='tomorrow')
async def send_schedule_tomorrow(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        buttons, msg_schedule = await valid_data(
            data=data, id=call.message.chat.id, tomorow=True
        )

        try:
            del data[f'name_{call.message.chat.id}']
        except Exception:
            pass

        await call.message.edit_text(
            str(msg_schedule), reply_markup=buttons, parse_mode='HTML'
        )


@dp.callback_query_handler(text='prepod')
async def name_prepod(call: types.CallbackQuery):
    await call.message.delete()
    if true_teacher(call.message.chat.id):
        await call.message.answer('Отправьте группу')
    else:
        await call.message.answer('Отправьте фамилию преподавателя')
    await SendName.last_name.set()


@dp.message_handler(state=SendName.last_name)
async def take_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if len(message.text.split('.')) > 1:
            data[f'name_{message.from_user.id}'] = message.text
        else:
            data[f'name_{message.from_user.id}'] = message.text.upper()

        res = await take(data, f'name_{message.from_user.id}', message)
        if await take_g_or_p(res, message):
            await state.finish()
