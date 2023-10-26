import datetime

from loader import bot, db
from models import Homework, Student, Teacher
from take_schedule_from_RKSI.main import prepod_pars


async def help_write(
        name: str, today: bool = False, tomorrow: bool = False
) -> dict:  # Если всё False то выводит за неделю
    newdict = {}
    result = await prepod_pars(name, today=today, tomorrow=tomorrow)
    try:
        for i in result:
            try:
                newdict[i['name']].add(i['prepod'])
            except Exception:
                newdict[i['name']] = set()
                newdict[i['name']].add(i['prepod'])
    except Exception:
        for day in result.keys():
            for i in result[day]:
                try:
                    newdict[i['name']].add(i['prepod'])
                except Exception:
                    newdict[i['name']] = set()
                    newdict[i['name']].add(i['prepod'])

    return newdict


async def get_lesson_dict(call):
    teacher = (
        db.query(Teacher)
        .filter(Teacher.tg_user_id == call.from_user.id)
        .first()
    )
    full_name = teacher.full_name
    lesson_dict = await help_write(full_name)
    if len(lesson_dict) == 0:
        full_name = full_name.split()
        full_name = full_name[0] + '  ' + full_name[1]
        lesson_dict = await help_write(full_name)
    return lesson_dict


async def update_homework(message, data, text, file_names):
    teacher_name = (
        db.query(Teacher)
        .filter(Teacher.tg_user_id == message.from_user.id)
        .first()
        .full_name
    )
    subject, group = data['name_lesson'], data['group']
    homework = Homework()
    homework.group = group
    homework.name_lesson = subject
    homework.teacher_name = teacher_name
    homework.text = text
    if message.content_type == 'photo':
        homework.photos_name = file_names
        homework.documents_name = 'Нет файлов'
    elif message.content_type == 'document':
        homework.photos_name = 'Нет фото'
        homework.documents_name = file_names
    else:
        homework.photos_name = 'Нет фото'
        homework.documents_name = 'Нет файлов'
    homework.edit_date = datetime.datetime.now()
    db.add(homework)
    db.commit()
    await notifications_user(group, subject)
    await message.answer('Домашнее задание успешно записано')


async def notifications_user(group, subject):
    users = db.query(Student).filter(Student.group == group).all()
    for user in users:
        tg_id = user.tg_user_id
        await bot.send_message(
            tg_id, text=f'У вас новое домашнее задание по предмету {subject}'
        )
