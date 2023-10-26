import math

from aiogram import types, filters
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from keyboards import spam_butt
from loader import bot, dp
from scripts import take_all_stud
from scripts.help_to_handler import edit_or_answer, valid_data, take_g_or_p, take
from scripts import check_prepod, take_all_prepod, true_teacher, take_all_group
class SendMsg(StatesGroup):
    name = State()
    msg_for_user = State()

@dp.message_handler(filters.Text(equals="Рассылка"))
async def spam_start(message: types.Message):
    await message.answer("Выберите:", reply_markup=spam_butt)

@dp.callback_query_handler(text="group_spam")
async def spam_start(call: types.CallbackQuery):
    await call.message.answer("Отправте группу")
    await SendMsg.name.set()

@dp.message_handler(state=SendMsg.name)
async def spam_start(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data[f"name_of_{message.from_user.id}"] = message.text.upper()

        res = await take_all_group(data[f"name_of_{message.from_user.id}"])
        if not res:
            await message.answer("Напишите сообщение:")
            await SendMsg.next()
        else:
            await message.answer(f'Похожие варианты:\n{"".join(res)}', parse_mode='HTML')
            await message.answer('Отправьте группу')

@dp.message_handler(state=SendMsg.msg_for_user)
async def spam_start(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data[f"msg_{message.from_user.id}"] = message.text

        stud = take_all_stud(data[f"name_of_{message.from_user.id}"])
        try:
            no = 0
            for i in stud:
                try:
                    await bot.send_message(chat_id=i.tg_user_id, text=data[f"msg_{message.from_user.id}"])
                except:
                    n += 1
            await message.answer("Рассылка закончена!")
            await message.answer(f"Не получили сорбщение {n} пользователей!")
        except:
            await state.finish()
            await message.answer("Что-то пошло не так :(")




