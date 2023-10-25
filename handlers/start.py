from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inlines import start_ikb
from loader import dp, db
from states import Register

from models import Teacher, Student


@dp.message_handler(text='/start')
async def start(message: types.Message):
    await message.answer('Стартовое сообщение', reply_markup=start_ikb)


@dp.callback_query_handler(text='cancel', state=Register)
async def cancel(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer('Стартовое сообщение', reply_markup=start_ikb)


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
            'Вы успешно вышли из аккаунта\n\n' 'Стартовое сообщение',
            reply_markup=start_ikb,
        )
