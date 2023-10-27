from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards import admin_kb
from keyboards.inlines import start_ikb, accept_ikb
from loader import db, dp
from models import Admin
from models import Student, Teacher
from scripts import true_teacher, true_stud
from states import Register


@dp.message_handler(text='/start')
async def start(message: types.Message):
    admin = (
        db.query(Admin)
        .filter(Admin.tg_user_id == message.from_user.id)
        .first()
    )
    if admin:
        await message.answer(
            f'Здравствуйте {admin.full_name} вам '
            f'доступен полный функционал бота',
            reply_markup=admin_kb,
        )
    elif not true_teacher(message.from_user.id) and not true_stud(
            message.from_user.id
    ):
        await message.answer_document(
            caption='Чтобы продолжить необходимо'
                    ' подтвердить согласие на '
                    'обработку персональных данных',
            document=types.InputFile('start_file/FV_BIT_CONF.docx'),
            reply_markup=accept_ikb,
        )
        await Register.accept.set()
    else:
        await message.answer(
            'Привет я бот-помощник для студентов и преподавателей РКСИ '
            'для продолжения необходимо пройти авторизацию',
            reply_markup=start_ikb,
        )


@dp.callback_query_handler(text='accept', state=Register.accept)
async def accept(call: types.CallbackQuery, state: FSMContext):
    admin = (
        db.query(Admin).filter(Admin.tg_user_id == call.from_user.id).first()
    )
    if admin is None:
        await state.finish()
        await call.message.answer(
            'Привет я бот-помощник для студентов и преподавателей РКСИ '
            'для продолжения необходимо пройти авторизацию',
            reply_markup=start_ikb,
        )
    else:
        await state.finish()
        await call.message.answer(
            f'Здравствуйте {admin.full_name} вам '
            f'доступен полный функционал бота',
            reply_markup=admin_kb,
        )


@dp.callback_query_handler(text='no_accept', state=Register.accept)
async def reg_accept(call: types.CallbackQuery):
    await call.message.answer_document(
        caption='Чтобы продолжить необходимо'
                ' подтвердить согласие на '
                'обработку персональных данных',
        document=types.InputFile('start_file/FV_BIT_CONF.docx'),
        reply_markup=accept_ikb,
    )


# @dp.message_handler(text='/after_start')
# async def after_start(message: types.Message):
#     admin = (
#         db.query(Admin)
#         .filter(Admin.tg_user_id == message.from_user.id)
#         .first()
#     )
#     if admin is None:
#         await message.answer(
#             'Привет я бот-помощник для студентов и преподавателей РКСИ '
#             'для продолжения необходимо пройти авторизацию',
#             reply_markup=start_ikb,
#         )
#     else:
#         await message.answer(
#             f'Здравствуйте {admin.full_name} вам '
#             f'доступен полный функционал бота',
#             reply_markup=admin_kb,
#         )


@dp.callback_query_handler(text='cancel', state=Register)
async def cancel(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer(
        'Привет я бот-помощник для студентов и преподавателей РКСИ '
        'для продолжения необходимо пройти авторизацию',
        reply_markup=start_ikb,
    )


@dp.message_handler(text='/exit')
async def exit_account(message: types.Message):
    account = (
        db.query(Student)
        .filter(Student.tg_user_id == message.from_user.id)
        .first()
    )
    if account is None:
        account = (
            db.query(Teacher)
            .filter(Teacher.tg_user_id == message.from_user.id)
            .first()
        )
    if account is None:
        await message.answer('У вас не было аккаунта')
    else:
        db.delete(account)
        db.commit()
        await message.answer(
            'Вы успешно вышли из аккаунта',
            reply_markup=types.ReplyKeyboardRemove(),
        )
        await message.answer(
            'Привет я бот-помощник для студентов и преподавателей РКСИ '
            'для продолжения необходимо пройти авторизацию',
            reply_markup=start_ikb,
        )
