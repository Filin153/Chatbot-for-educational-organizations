from aiogram import types, Dispatcher
import requests
from loader import dp
from utils.check import chech_prepod
from keyboards.dt_send_schedule import schedule_buttons_g, schedule_buttons_p
import asyncio
from take_schedule_from_RKSI.make_schedule import GroupSchedule, PrepodSchedule, MakeSchedule


@dp.callback_query_handler(text='schedule')
async def watch_schedule(call: types.CallbackQuery):
    await call.message.edit_text('<b>Расписание берётся с планшетки, но если что-то пойдет не так то выдаст расписание с сайта об это будет уведомлениие в самом верху.</b>\n\nВыбирите день:', reply_markup=schedule_buttons_g, parse_mode="HTML")

@dp.callback_query_handler(text='week')
async def send_schedule_week(call: types.CallbackQuery):
    buttons, msg_schedule = await chech_prepod(call)
    try:
        await call.message.edit_text(str(msg_schedule), reply_markup=buttons, parse_mode="HTML")
    except:
        msg = MakeSchedule().share_msg(msg_schedule)
        firstText = await call.message.edit_text(next(msg), parse_mode="HTML")
        await call.message.answer(next(msg), reply_markup=buttons, parse_mode="HTML")
        try:
            delMsg = await firstText.reply('Удалится через 2 мин')
            await asyncio.sleep(120)
            await delMsg.delete()
            await firstText.delete()
        except:
            pass

@dp.callback_query_handler(text='today')
async def send_schedule_today(call: types.CallbackQuery):
    buttons, msg_schedule = await chech_prepod(call, today=True)
    await call.message.edit_text(str(msg_schedule), reply_markup=buttons, parse_mode="HTML")

@dp.callback_query_handler(text='tomorrow')
async def send_schedule_tomorrow(call: types.CallbackQuery):
    buttons, msg_schedule = await chech_prepod(call, tomorow=True)
    await call.message.edit_text(str(msg_schedule), reply_markup=buttons, parse_mode="HTML")