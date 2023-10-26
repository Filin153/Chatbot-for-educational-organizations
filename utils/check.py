from aiogram import types
import requests
from keyboards.dt_send_schedule import schedule_buttons_g, schedule_buttons_p
import asyncio

from loader import db
from models import Teacher, Student
from take_schedule_from_RKSI.make_schedule import GroupSchedule, PrepodSchedule, MakeSchedule

async def chech_prepod(call: types.CallbackQuery, today: bool = False, tomorow: bool = False):
    account = (
        db.query(Student)
        .filter(Student.tg_user_id == call.message.chat.id)
        .first()
    )
    if account is None:
        account = (
            db.query(Teacher)
            .filter(Teacher.tg_user_id == call.message.chat.id)
            .first()
        )
        buttons = schedule_buttons_p
        chedule = await PrepodSchedule(group=account.full_name, today=today, tomorow=tomorow).run()
        msg_schedule = chedule.schedule
    else:
        buttons = schedule_buttons_g
        chedule = await GroupSchedule(group=account.group, today=today, tomorow=tomorow).run()
        msg_schedule = chedule.schedule

    return buttons, msg_schedule