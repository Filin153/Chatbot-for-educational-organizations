from loader import db, dp
from aiogram import types

from models import Homework, Student
from keyboards.inlines import create_subjects_ikb, write_homework_ikb


@dp.message_handler(text='Домашнее задание')
async def homework_start(message: types.Message):
    account = (
        db.query(Student)
        .filter(Student.tg_user_id == message.from_user.id)
        .first()
    )
    if account is None:
        await message.answer(
            'Выберите действие', reply_markup=write_homework_ikb
        )
    else:
        group = account.group
        all_homeworks = (
            db.query(Homework).filter(Homework.group == group).all()
        )
        subjects = list(map(lambda x: x.name_lesson, all_homeworks))
        subjects_ikb = await create_subjects_ikb(set(subjects))
        await message.answer(
            'Выберите предмет\n'
            '(Для студентов - если нет inline кнопок нет дз)',
            reply_markup=subjects_ikb,
        )
