from keyboards.inlines.admin_ikb import admin_schedule_ikb
from keyboards.bt_send_schedule import schedule_buttons_g, schedule_buttons_p
from loader import db
from models import Teacher, Student, Admin
from take_schedule_from_RKSI.make_schedule import GroupSchedule, PrepodSchedule


async def check_prepod(
    id=None,
    admin_key=None,
    name: str = None,
    today: bool = False,
    tomorow: bool = False,
):
    if admin_key == 'g':
        buttons = admin_schedule_ikb
        chedule = await GroupSchedule(
            group=name, today=today, tomorow=tomorow
        ).run()
        msg_schedule = chedule.schedule
    elif admin_key == 'p':
        buttons = admin_schedule_ikb
        chedule = await PrepodSchedule(
            group=name, today=today, tomorow=tomorow
        ).run()
        msg_schedule = chedule.schedule
    elif true_admin(id) and name:
        buttons = admin_schedule_ikb
        if len(name.split('.')) > 1:
            chedule = await PrepodSchedule(
                group=name, today=today, tomorow=tomorow
            ).run()
            msg_schedule = chedule.schedule
        else:
            chedule = await GroupSchedule(
                group=name, today=today, tomorow=tomorow
            ).run()
            msg_schedule = chedule.schedule
        return buttons, msg_schedule
    elif id:
        account = db.query(Student).filter(Student.tg_user_id == id).first()
        if account is None:
            account = (
                db.query(Teacher).filter(Teacher.tg_user_id == id).first()
            )
            buttons = schedule_buttons_p
            chedule = await PrepodSchedule(
                group=account.full_name, today=today, tomorow=tomorow
            ).run()
            msg_schedule = chedule.schedule
        else:
            buttons = schedule_buttons_g
            chedule = await GroupSchedule(
                group=account.group, today=today, tomorow=tomorow
            ).run()
            msg_schedule = chedule.schedule
        return buttons, msg_schedule
    elif len(name.split('.')) > 1:
        buttons = schedule_buttons_g
        chedule = await PrepodSchedule(
            group=name, today=today, tomorow=tomorow
        ).run()
        msg_schedule = chedule.schedule
    else:
        buttons = schedule_buttons_p
        chedule = await GroupSchedule(
            group=name, today=today, tomorow=tomorow
        ).run()
        msg_schedule = chedule.schedule

    return buttons, msg_schedule


def true_teacher(id):
    account = db.query(Teacher).filter(Teacher.tg_user_id == id).first()
    if account:
        return True


def true_stud(id):
    account = db.query(Student).filter(Student.tg_user_id == id).first()
    if account:
        return True


def true_admin(id):
    account = db.query(Admin).filter(Admin.tg_user_id == id).first()
    if account:
        return True


def take_all_stud(group):
    account = db.query(Student).filter(Student.group == group).all()
    if account:
        return account
