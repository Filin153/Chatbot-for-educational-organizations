from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inlines import (
    cancel_teacher_ikb,
    create_for_delete_teachers,
    do_teacher_ikb,
)
from loader import bot, db, dp
from models import Admin, TeacherData, Teacher
from scripts import take_all_prepod
from states import AddTeacher


@dp.message_handler(text='Преподаватели')
async def teachers(message: types.Message):
    admin = (
        db.query(Admin)
        .filter(Admin.tg_user_id == message.from_user.id)
        .first()
    )
    if admin is not None:
        await message.answer('Выберите действие', reply_markup=do_teacher_ikb)


@dp.callback_query_handler(text='cancel_teacher', state=AddTeacher)
async def cancel_teacher(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer('Отменено')


@dp.callback_query_handler(text='add_teacher')
async def add_teacher(call: types.CallbackQuery):
    await call.message.answer(
        'Введите ФИО преподавателя', reply_markup=cancel_teacher_ikb
    )
    await AddTeacher.full_name.set()


@dp.message_handler(content_types=['text'], state=AddTeacher.full_name)
async def teacher_full_name(message: types.Message, state: FSMContext):
    teacher = message.text
    check = await take_all_prepod(teacher)
    if not check:
        await message.answer(
            'Введите пароль для аккаунта препода:',
            reply_markup=cancel_teacher_ikb,
        )
        await state.update_data(full_name=teacher)
        await AddTeacher.password.set()
    else:
        check = ''.join(check)
        await message.answer(
            f'Преподаватель не найден вот совпадения\n'
            f'{check}\nПопробуйте снова',
            reply_markup=cancel_teacher_ikb,
        )


@dp.message_handler(content_types=['text'], state=AddTeacher.password)
async def teacher_password(message: types.Message, state: FSMContext):
    data = await state.get_data()
    password = message.text
    teacher = data['full_name']
    check_data = (
        db.query(TeacherData).filter(TeacherData.full_name == teacher).first()
    )
    if check_data is not None:
        db.delete(check_data)
        db.commit()
    teacher_data = TeacherData()
    teacher_data.full_name = teacher
    teacher_data.password = password
    db.add(teacher_data)
    db.commit()
    password = f'<span class="tg-spoiler">{password}</span>'
    await state.finish()
    await message.answer(
        f'Преподаватель успешно добавлен\n'
        f'ФИО: {teacher}\n'
        f'Пароль: {password}',
        parse_mode='html',
    )


@dp.callback_query_handler(text='delete_teacher')
async def delete_teacher(call: types.CallbackQuery):
    teachers = db.query(TeacherData).all()
    teachers = list(map(lambda x: x.full_name, teachers))
    delete_teacher_ikb = await create_for_delete_teachers(teachers)
    await call.message.answer(
        'Выберите преподавателя которого хотите удалить',
        reply_markup=delete_teacher_ikb,
    )


@dp.callback_query_handler(lambda call: call.data.startswith('dt_'))
async def dt_teacher(call: types.CallbackQuery):
    teacher_name = call.data.split('_')[1]
    teacher_data = (
        db.query(TeacherData)
        .filter(TeacherData.full_name == teacher_name)
        .first()
    )
    teacher = db.query(Teacher).filter(Teacher.full_name == teacher_name).all()
    for i in teacher:
        try:
            await bot.send_message(
                chat_id=i.tg_user_id,
                text='Преподавателя удалили из '
                'базы данных пожалуйста '
                'авторизируйтесь снова',
                reply_markup=types.ReplyKeyboardRemove(),
            )
        except Exception:
            pass
        db.delete(i)
    db.delete(teacher_data)
    db.commit()
    await call.message.answer('Преподаватель успешно удалён из базы данных')
