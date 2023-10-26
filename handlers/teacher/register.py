from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inlines import cancel_ikb
from keyboards import start_kb
from loader import db, dp
from models import Student, Teacher, TeacherData
from states import Register


@dp.callback_query_handler(text='teacher')
async def teacher_call(call: types.CallbackQuery):
    students_id = list(map(lambda x: x.tg_user_id, db.query(Student).all()))
    teachers_id = list(map(lambda x: x.tg_user_id, db.query(Teacher).all()))
    all_id = students_id + teachers_id
    if call.from_user.id in all_id:
        await call.answer('Вы уже вошли в аккаунт')
    else:
        await call.message.answer(
            'Введите пароль выданный администрацией', reply_markup=cancel_ikb
        )
        await Register.fio.set()


@dp.message_handler(content_types=['text'], state=Register.fio)
async def get_fio(message: types.Message, state: FSMContext):
    password = message.text
    teacher_data = (
        db.query(TeacherData).filter(TeacherData.password == password).first()
    )
    if teacher_data:
        teacher = Teacher()
        teacher.tg_user_id = message.from_user.id
        teacher.user_name = message.from_user.full_name
        teacher.full_name = teacher_data.full_name
        db.add(teacher)
        db.commit()
        await message.answer(
            f'Здравствуйте {teacher.full_name},'
            f' Вы успешно вошли, теперь вы можете смотреть расписание,'
            f' записывать домашнее задание для группы,'
            f' получить интересующую вас информацию о колледже.\n(Теперь вы '
            f'можете войти в учебный отдел)', reply_markup=start_kb
        )
        await state.finish()
    else:
        await message.answer(
            'Неверный пароль, попробуйте снова', reply_markup=cancel_ikb
        )
