from aiogram import types
from aiogram.types import MediaGroup

from keyboards.inlines import create_date_ikb
from loader import db, dp
from models import Homework, Student


@dp.callback_query_handler(lambda call: call.data.startswith('st_'))
async def check_homework_student(call: types.CallbackQuery):
    student_group = (
        db.query(Student)
        .filter(Student.tg_user_id == call.from_user.id)
        .first()
        .group
    )
    subject = call.data.split('_')[1]
    all_date = (
        db.query(Homework)
        .filter(
            Homework.group == student_group, Homework.name_lesson == subject
        )
        .all()
    )
    dates = list(map(lambda x: str(x.made_date), set(all_date)))
    dates_ikb = await create_date_ikb(set(dates), subject)
    await call.message.edit_text('Выберите дату')
    await call.message.edit_reply_markup(dates_ikb)


@dp.callback_query_handler(lambda call: call.data.startswith('_'))
async def check_date_student(call: types.CallbackQuery):
    student_group = (
        db.query(Student)
        .filter(Student.tg_user_id == call.from_user.id)
        .first()
        .group
    )
    date = call.data.split('_')[1]
    subject = call.data.split('_')[2]
    homework = (
        db.query(Homework)
        .filter(
            Homework.group == student_group,
            Homework.name_lesson == subject,
            Homework.made_date == date,
        )
        .all()[-1]
    )
    photos = homework.photos_name
    documents = homework.documents_name
    text = homework.text
    if photos != 'Нет фото':
        album = MediaGroup()
        files = photos.split()
        for i in range(len(files)):
            if i == 0:
                album.attach_photo(
                    photo=files[i],
                    caption=f'Текст домашнего задания:\n\n{text}',
                )
            else:
                album.attach_photo(photo=files[i])
        await call.message.answer_media_group(media=album)
    elif documents != 'Нет файлов':
        album = MediaGroup()
        files = documents.split()
        for i in range(len(files)):
            if i == 0:
                album.attach_document(
                    document=files[i],
                    caption=f'Текст домашнего задания:\n\n{text}',
                )
            else:
                album.attach_document(document=files[i])
        await call.message.answer_media_group(media=album)
    else:
        await call.message.answer(f'Текст домашнего задания:\n\n{text}')
