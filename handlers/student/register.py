from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards import start_kb
from keyboards.inlines import cancel_ikb
from loader import db, dp
from models import Student, Teacher
from scripts import take_group
from states import Register


@dp.callback_query_handler(text='study')
async def study_call(call: types.CallbackQuery):
    students_id = list(map(lambda x: x.tg_user_id, db.query(Student).all()))
    teachers_id = list(map(lambda x: x.tg_user_id, db.query(Teacher).all()))
    all_id = students_id + teachers_id
    if call.from_user.id in all_id:
        await call.answer('Вы уже вошли в аккаунт')
    else:
        await call.message.answer(
            'Введите свою группу\n\nНапример: БД-21', reply_markup=cancel_ikb
        )
        await Register.group.set()


@dp.message_handler(content_types=['text'], state=Register.group)
async def get_group(message: types.Message, state: FSMContext):
    group = message.text
    groups = await take_group()
    if group in groups:
        student = Student()
        student.tg_user_id = message.from_user.id
        student.user_name = message.from_user.full_name
        student.group = group
        db.add(student)
        db.commit()
        await message.answer(
            f'Привет {student.user_name}', reply_markup=start_kb
        )
        await state.finish()
    else:
        await message.answer(
            'Такой группы не существует, повторите попытку'
            '\n\nНапример: БД-21',
            reply_markup=cancel_ikb,
        )
