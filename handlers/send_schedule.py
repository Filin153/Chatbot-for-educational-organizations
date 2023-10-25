from aiogram import types, Dispatcher
import requests
from buttons.dt_send_schedule import schedule_buttons
import asyncio
from take_schedule_from_RKSI.make_schedule import GroupSchedule, MakeSchedule


async def watch_schedule(call: types.CallbackQuery):
    await call.message.edit_text('<b>Расписание берётся с планшетки, но если что-то пойдет не так то выдаст расписание с сайта об это будет уведомлениие в самом верху.</b>\n\nВыбирите день:', reply_markup=schedule_buttons, parse_mode="HTML")


# async def send_schedule_today(call: types.CallbackQuery):
#     msg = await send_schedule_group(True, str(send_user_group(call.message.chat.id)))
#     await call.message.edit_text(msg, reply_markup=schedule_buttons)
#
# async def send_schedule_tomorrow(call: types.CallbackQuery):
#     msg = await send_schedule_group(False, str(send_user_group(call.message.chat.id)))
#     await call.message.edit_text(msg, reply_markup=schedule_buttons)

async def send_schedule_week(call: types.CallbackQuery):
    groups_chedule = GroupSchedule(today=False, group=str(send_user_group(call.message.chat.id)), week=True)
    schedule_info = await groups_chedule.run()
    msg_schedule = schedule_info.schedule
    try:
        await call.message.edit_text(str(msg_schedule), reply_markup=schedule_buttons, parse_mode="HTML")
    except:
        msg = MakeSchedule().share_msg(msg_schedule)
        firstText = await call.message.edit_text(next(msg), parse_mode="HTML")
        await call.message.answer(next(msg), reply_markup=schedule_buttons, parse_mode="HTML")
        try:
            delMsg = await firstText.reply('Удалится через 2 мин')
            await asyncio.sleep(120)
            await delMsg.delete()
            await firstText.delete()
        except:
            pass

async def send_schedule_today(call: types.CallbackQuery):
    group = send_user_group(call.message.chat.id)
    r = requests.get(f'http://load_schedule_api:{PORT}/getschedule/{group}/today')
    if r.status_code == 200:
        if str(r.text) == "0":
            groups_chedule = GroupSchedule(today=True, group=str(send_user_group(call.message.chat.id)))
            schedule_info = await groups_chedule.run()
            msg_schedule = schedule_info.schedule
            await call.message.edit_text(str(msg_schedule), reply_markup=schedule_buttons, parse_mode="HTML")
        else:
            await call.message.edit_text(r.text.replace(r'\n', '\n')[1:-1], reply_markup=schedule_buttons)
    else:
        await call.message.edit_text('🥲Расписания нету', reply_markup=schedule_buttons)

async def send_schedule_tomorrow(call: types.CallbackQuery):
    group = send_user_group(call.message.chat.id)
    r = requests.get(f'http://load_schedule_api:{PORT}/getschedule/{group}/tomorrow')
    if r.status_code == 200:
        if str(r.text) == "0":
            groups_chedule = GroupSchedule(today=False, group=str(send_user_group(call.message.chat.id)))
            schedule_info = await groups_chedule.run()
            msg_schedule = schedule_info.schedule
            await call.message.edit_text(str(msg_schedule), reply_markup=schedule_buttons, parse_mode="HTML")
        else:
            await call.message.edit_text(r.text.replace(r'\n', '\n')[1:-1], reply_markup=schedule_buttons)
    else:
        await call.message.edit_text('🥲Расписания нету', reply_markup=schedule_buttons)


def reg_hand_send_schedule(dp: Dispatcher):
    dp.register_callback_query_handler(watch_schedule, text='schedule')
    dp.register_callback_query_handler(send_schedule_today, text='today')
    dp.register_callback_query_handler(send_schedule_tomorrow, text='tomorrow')
    dp.register_callback_query_handler(send_schedule_week, text='week')