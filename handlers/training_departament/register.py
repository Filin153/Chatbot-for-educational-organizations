from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inlines import cancel_ikb
from keyboards import departament_kb
from loader import db, dp
from models import Student, Teacher, TrainingDepartament, TrainingDepartamentData
from states import Register


@dp.callback_query_handler(text='training_departament')
async def training_departament(call: types.CallbackQuery):
    students_id = list(map(lambda x: x.tg_user_id, db.query(Student).all()))
    teachers_id = list(map(lambda x: x.tg_user_id, db.query(Teacher).all()))
    all_id = students_id + teachers_id
    if call.from_user.id not in all_id:
        await call.answer('Для входа в учебный отдел нужно сначала авторизоваться как '
                          'студент или преподаватель')
    else:
        await call.message.answer(
            'Введите пароль выданный администрацией', reply_markup=cancel_ikb
        )
        await Register.password_departament.set()


@dp.message_handler(content_types=['text'], state=Register.password_departament)
async def get_fio(message: types.Message, state: FSMContext):
    password = message.text
    departament_data = (
        db.query(TrainingDepartamentData).filter(TrainingDepartamentData.password == password).first()
    )
    if departament_data:
        account = db.query(Student).filter(Student.tg_user_id == message.from_user.id).first()
        if account is None:
            account = db.query(Teacher).filter(Teacher.tg_user_id == message.from_user.id).first()
        account.is_departament = 1
        db.commit()
        await message.answer('Вам доступен новый функционал', reply_markup=departament_kb)
        await state.finish()
    else:
        await message.answer(
            'Неверный пароль, попробуйте снова', reply_markup=cancel_ikb
        )
