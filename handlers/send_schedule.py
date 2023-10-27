import re
from keyboards import admin_schedule_ikb
from keyboards.bt_send_schedule import schedule_buttons_g, schedule_buttons_p
import asyncio
from aiogram import types, filters
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from datetime import datetime
from keyboards.inlines.start_ikb import start_ikb, cancel_ikb
from loader import dp
from scripts import true_teacher, true_admin
from scripts.help_to_handler import (
    edit_or_answer,
    valid_data,
    take_g_or_p,
    take,
)
from take_schedule_from_RKSI.make_schedule import MakeSchedule



class SendName(StatesGroup):
    last_name = State()


@dp.message_handler(filters.Text(equals='Расписание'))
async def watch_schedule(message: types.Message):
    try:
        if 20 <= datetime.now().time().hour:
            _, msg_schedule = await valid_data(
                id=message.from_user.id, tomorow=True
            )
        else:
            _, msg_schedule = await valid_data(id=message.from_user.id, today=True)
    except Exception:
        pass

    await message.delete()
    if true_admin(message.from_user.id):
        await message.answer('Расписание', reply_markup=admin_schedule_ikb)
    elif true_teacher(message.from_user.id):
        await edit_or_answer(message, msg_schedule, schedule_buttons_p)
    else:
        await edit_or_answer(message, msg_schedule, schedule_buttons_g)


@dp.callback_query_handler(text='week')
async def send_schedule_week(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        try:
            buttons, msg_schedule = await valid_data(
                data=data, admin_key=key, id=call.message.chat.id
            )
        except Exception:
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
            first_text = await call.message.edit_text(
                next(msg), parse_mode='HTML'
            )
            await call.message.answer(
                next(msg), reply_markup=buttons, parse_mode='HTML'
            )
            try:
                del_msg = await first_text.reply(
                    'Слишком большое сообщение было разделенно на 2 части\n'
                    'Первая часть удалится через 2 мин'
                )
                await asyncio.sleep(120)
                await del_msg.delete()
                await first_text.delete()
            except Exception:
                pass


@dp.callback_query_handler(text='today')
async def send_schedule_today(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        try:
            buttons, msg_schedule = await valid_data(
                data=data, admin_key=key,
                id=call.message.chat.id,
                today=True
            )
        except Exception:
            buttons, msg_schedule = await valid_data(
                data=data,
                id=call.message.chat.id,
                today=True
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
        try:
            buttons, msg_schedule = await valid_data(
                data=data, admin_key=key,
                id=call.message.chat.id,
                tomorow=True
            )
        except Exception:
            buttons, msg_schedule = await valid_data(
                data=data,
                id=call.message.chat.id,
                tomorow=True
            )

        try:
            del data[f'name_{call.message.chat.id}']
        except Exception:
            pass

        await call.message.edit_text(
            str(msg_schedule), reply_markup=buttons, parse_mode='HTML'
        )


@dp.callback_query_handler(lambda c: c.data.startswith('prepod'))
async def name_prepod(call: types.CallbackQuery):
    await call.message.delete()
    global key
    key = call.data.split(':')[-1]
    if key == 'g':
        await call.message.answer(
            'Отправьте группу\n\nПример: ИС-28', reply_markup=cancel_ikb
        )
    elif key == 'p':
        await call.message.answer(
            'Отправьте ФИО преподавателя\n\nПример: Каламбет В.Б.',
            reply_markup=cancel_ikb,
        )
    elif true_teacher(call.message.chat.id):
        await call.message.answer(
            'Отправьте группу\n\nПример: ИС-28', reply_markup=cancel_ikb
        )
    else:
        await call.message.answer(
            'Отправьте ФИО преподавателя\n\nПример: Каламбет В.Б.',
            reply_markup=cancel_ikb,
        )
    await SendName.last_name.set()


@dp.message_handler(state=SendName.last_name)
async def take_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if len(message.text.split('.')) > 1:
            data[f'name_{message.from_user.id}'] = message.text
        else:
            data[f'name_{message.from_user.id}'] = message.text.upper()
            if re.sub(r'[\D]', '', data[f'name_{message.from_user.id}'][-2:]):
                data[f'name_{message.from_user.id}'] = (
                        data[f'name_{message.from_user.id}'][:-1]
                        + data[f'name_{message.from_user.id}'][-1].lower()
                )

        try:
            res = await take(
                data,
                f'name_{message.from_user.id}',
                admin_key=key,
                message=message,
            )
        except Exception:
            res = await take(
                data,
                f'name_{message.from_user.id}',
                message=message,
            )
        if await take_g_or_p(res, message):
            await state.finish()


@dp.callback_query_handler(text='cancel', state=SendName)
async def cancel(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer(
        'Привет я бот-помощник для студентов и преподавателей РКСИ'
        'для продолжения необходимо пройти авторизацию',
        reply_markup=start_ikb,
    )
