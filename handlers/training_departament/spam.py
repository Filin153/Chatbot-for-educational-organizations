from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inlines import spam_ikb
from loader import db, dp
from models import Admin, Student, Teacher
from states import Spam


@dp.message_handler(text='Рассылка')
async def spam(message: types.Message):
    admins = db.query(Admin).all()
    admins_id = list(map(lambda x: x.tg_user_id, admins))
    account = db.query(Student).filter(Student.tg_user_id == message.from_user.id).first()
    if account is None:
        account = db.query(Teacher).filter(Teacher.tg_user_id == message.from_user.id).first()
    if not account.is_departament and message.from_user.id not in admins_id:
        await message.answer('У вас нет прав доступа на рассылку')
    else:
        await message.answer('Кому вы хотите отправить рассылку?', reply_markup=spam_ikb)


@dp.callback_query_handler(text='cancel_spam', state=Spam)
async def cancel_spam(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer('Отменено')
    await state.finish()
