from typing import List

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import MediaGroup

from keyboards.inlines import cancel_spam_ikb
from loader import dp, db, bot
from models import Student, Teacher
from scripts import take_all_group
from states import Spam


@dp.callback_query_handler(text='spam_teacher')
async def spam(call: types.CallbackQuery):
    await call.message.answer(
        'Пришлите сообщение:', reply_markup=cancel_spam_ikb
    )
    await Spam.message.set()


@dp.callback_query_handler(text='spam_group')
async def spam_group(call: types.CallbackQuery):
    await call.message.answer('Напишите группу:', reply_markup=cancel_spam_ikb)
    await Spam.group.set()


@dp.message_handler(content_types=['text'], state=Spam.group)
async def get_group(message: types.Message, state: FSMContext):
    msg = message.text.upper()
    user_msg = msg[:-1] + msg[-1].lower()
    check = await take_all_group(user_msg)
    if not check:
        await state.update_data(group=user_msg)
        await message.answer(
            'Введите сообщение для рассылки', reply_markup=cancel_spam_ikb
        )
        await Spam.message.set()
    else:
        check = '\n'.join(check)
        await message.answer(
            f'Такой группы нет\nВот список похожих групп\n' f'{check}',
            reply_markup=cancel_spam_ikb,
        )


@dp.message_handler(content_types=['text'], state=Spam.message)
async def spam_text(message: types.Message, state: FSMContext):
    try:
        data = await state.get_data('group')
        group = data['group']
        users = db.query(Student).filter(Student.group == group).all()
        user_ids = list(map(lambda x: x.tg_user_id, users))
    except Exception:
        teachers = db.query(Teacher).all()
        user_ids = list(map(lambda x: x.tg_user_id, teachers))
    for user_id in user_ids:
        await bot.send_message(
            chat_id=user_id, text=f'Рассылка\n\nСообщение\n{message.text}'
        )
    await message.answer('Рассылка отправлена')
    await state.finish()


@dp.message_handler(content_types=['photo'], state=Spam.message)
async def spam_photo(
    message: types.Message, state: FSMContext, album: List[types.Message]
):
    try:
        data = await state.get_data('group')
        group = data['group']
        users = db.query(Student).filter(Student.group == group).all()
        user_ids = list(map(lambda x: x.tg_user_id, users))
    except Exception:
        teachers = db.query(Teacher).all()
        user_ids = list(map(lambda x: x.tg_user_id, teachers))

    album_photo = MediaGroup()
    text = f'Рассылка\n\nСообщение\n{message.caption}'
    for i in range(len(album)):
        if i == 0:
            album_photo.attach_photo(album[i].photo[-1].file_id, caption=text)
        else:
            album_photo.attach_photo(album[i].photo[-1].file_id)
    for user_id in user_ids:
        await bot.send_media_group(chat_id=user_id, media=album_photo)
    await message.answer('Рассылка отправлена')
    await state.finish()


@dp.message_handler(content_types=['document'], state=Spam.message)
async def spam_document(
    message: types.Message, state: FSMContext, album: List[types.Message]
):
    try:
        data = await state.get_data('group')
        group = data['group']
        users = db.query(Student).filter(Student.group == group).all()
        user_ids = list(map(lambda x: x.tg_user_id, users))
    except Exception:
        teachers = db.query(Teacher).all()
        user_ids = list(map(lambda x: x.tg_user_id, teachers))
    text = f'Рассылка\n\nСообщение\n{message.caption}'
    album_document = MediaGroup()
    for i in range(len(album)):
        if i == 0:
            album_document.attach_document(
                album[i].document.file_id, caption=text
            )
        else:
            album_document.attach_document(album[i].document.file_id)
    for user_id in user_ids:
        await bot.send_media_group(chat_id=user_id, media=album_document)
    await message.answer('Рассылка отправлена')
    await state.finish()
