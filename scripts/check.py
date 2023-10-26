import requests
from keyboards.bt_send_schedule import schedule_buttons_g, schedule_buttons_p
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz, process
from loader import db
from models import Teacher, Student
from take_schedule_from_RKSI.make_schedule import GroupSchedule, PrepodSchedule


async def check_prepod(
    id=None, name: str = None, today: bool = False, tomorow: bool = False
):
    if id:
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


# def true_moder(id): # Поменять таблицу
#     account = (
#         db.query(Teacher)
#         .filter(Teacher.tg_user_id == id)
#         .first()
#     )
#     if account:
#         return True


def take_all_stud(group):
    account = db.query(Student).filter(Student.group == group).all()
    if account:
        return account


async def take_all_prepod(name):
    all_prepod = []
    similarity = []

    r = requests.get('https://rksi.ru/mobile_schedule')
    soup = BeautifulSoup(r.text, 'lxml')
    pr_tb_soup = soup.find('select', {'name': 'teacher'})
    all_prepod_soup = pr_tb_soup.find_all(
        'option',
    )

    for i in all_prepod_soup:
        all_prepod.append(str(i.text))

    if all_prepod.count(name) == 0:
        matching_strings = process.extract(
            name, all_prepod, scorer=fuzz.partial_token_sort_ratio, limit=3
        )

        for string, score in matching_strings:
            similarity.append(f'<code>{string}</code>\n')

        return similarity


async def take_all_group(name):
    all_group = []
    similarity = []

    r = requests.get('https://rksi.ru/mobile_schedule')
    soup = BeautifulSoup(r.text, 'lxml')

    pr_tb_soup = soup.find('select', {'name': 'group'})
    all_group_soup = pr_tb_soup.find_all(
        'option',
    )

    for i in all_group_soup:
        all_group.append(str(i.text))

    if all_group.count(name) == 0:
        matching_strings = process.extract(
            name, all_group, scorer=fuzz.partial_token_sort_ratio, limit=8
        )

        for string, score in matching_strings:
            similarity.append(f'<code>{string}</code>\n')

        return similarity
