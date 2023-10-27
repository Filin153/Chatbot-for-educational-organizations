from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards import start_kb
from keyboards.inlines import reset_password_ikb, cancel_password_ikb
from loader import dp, db, bot
from models import Admin, Student, Teacher, TrainingDepartamentData
from states import ResetDepartament


@dp.callback_query_handler(text='cancel_password', state=ResetDepartament)
async def cancel_password(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer('Отменено')


@dp.message_handler(text='Учебный отдел')
async def departament(message: types.Message):
    admin = (
        db.query(Admin)
        .filter(Admin.tg_user_id == message.from_user.id)
        .first()
    )
    if admin is not None:
        await message.answer(
            'Выберите действие', reply_markup=reset_password_ikb
        )


@dp.callback_query_handler(text='reset_password')
async def reset_password(call: types.CallbackQuery):
    await call.message.answer(
        'Введите новый пароль для учебного отдела:',
        reply_markup=cancel_password_ikb,
    )
    await ResetDepartament.password.set()


@dp.message_handler(content_types=['text'], state=ResetDepartament.password)
async def res_password(message: types.Message, state: FSMContext):
    students_in_departaments = (
        db.query(Student).filter(Student.is_departament == 1).all()
    )
    teachers_in_departaments = (
        db.query(Teacher).filter(Teacher.is_departament == 1).all()
    )
    for i in students_in_departaments:
        user_id = i.tg_user_id
        i.is_departament = 0
        try:
            await bot.send_message(
                chat_id=user_id,
                text='Пароль от учебного отдела был изменён',
                reply_markup=start_kb,
            )
        except Exception:
            pass
    for i in teachers_in_departaments:
        user_id = i.tg_user_id
        i.is_departament = 0
        try:
            await bot.send_message(
                chat_id=user_id,
                text='Пароль от учебного отдела был изменён',
                reply_markup=start_kb,
            )
        except Exception:
            pass

    departament_data = TrainingDepartamentData()
    departament_data.password = message.text
    db.add(departament_data)
    db.commit()
    await state.finish()
    await message.answer('Пароль изменён')
