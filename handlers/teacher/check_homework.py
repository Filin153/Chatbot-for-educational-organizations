from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import MediaGroup

from keyboards.inlines import (
    create_check_groups_ikb,
    create_check_lessons_ikb,
    create_check_date_ikb,
)
from loader import db, dp
from models import Homework
from scripts import get_lesson_dict
from states import CheckHomework


@dp.callback_query_handler(text='cancel_homework', state=CheckHomework)
async def cancel(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer('Отменено')


@dp.callback_query_handler(text='check_homework')
async def select_subject(call: types.CallbackQuery):
    lesson_dict = await get_lesson_dict(call)
    keys = lesson_dict.keys()
    lessons_ikb = await create_check_lessons_ikb(keys)
    await call.message.edit_text('Выберите предмет', reply_markup=lessons_ikb)
    await CheckHomework.name_lesson.set()


@dp.callback_query_handler(
    lambda call: call.data.startswith('checklesson_'),
    state=CheckHomework.name_lesson,
)
async def select_group(call: types.CallbackQuery, state: FSMContext):
    subject = call.data.split('_')[1]
    await state.update_data(name_lesson=subject)
    lesson_dict = await get_lesson_dict(call)
    groups = lesson_dict[subject]
    groups_ikb = await create_check_groups_ikb(groups)
    await call.message.edit_text('Выберите группу', reply_markup=groups_ikb)
    await CheckHomework.group.set()


@dp.callback_query_handler(
    lambda call: call.data.startswith('checkgroup_'), state=CheckHomework.group
)
async def check_homework(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    subject = data['name_lesson']
    group = call.data.split('_')[1]
    all_date = (
        db.query(Homework)
        .filter(Homework.group == group, Homework.name_lesson == subject)
        .all()
    )
    dates = list(map(lambda x: str(x.made_date), set(all_date)))
    dates_ikb = await create_check_date_ikb(set(dates), subject, group)
    await call.message.edit_text('Выберите дату')
    await call.message.edit_reply_markup(dates_ikb)
    await state.finish()


@dp.callback_query_handler(lambda call: call.data.startswith('d_'))
async def check_homework_student(call: types.CallbackQuery):
    data = call.data.split('_')
    date = data[1]
    subject = data[2]
    group = data[3]
    homework = (
        db.query(Homework)
        .filter(
            Homework.group == group,
            Homework.name_lesson == subject,
            Homework.made_date == date,
        )
        .all()[-1]
    )
    if homework is None:
        await call.message.answer('У группы нет домашних заданий')
    else:
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
                        caption=f'Домашнее задание для группы {group}\n\n\n'
                        f'Текст домашнего задания:\n\n{text}',
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
                        caption=f'Домашнее задание для группы {group}\n\n\n'
                        f'Текст домашнего задания:\n\n{text}',
                    )
                else:
                    album.attach_document(document=files[i])
            await call.message.answer_media_group(media=album)
        else:
            await call.message.answer(
                text=f'Домашнее задание для группы {group}\n\n\n'
                f'Текст домашнего задания:\n\n{text}'
            )
