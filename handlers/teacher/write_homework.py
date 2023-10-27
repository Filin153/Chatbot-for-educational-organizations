from typing import List

from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inlines import (
    cancel_homework_ikb,
    create_groups_ikb,
    create_lessons_ikb,
)
from loader import dp
from scripts import get_lesson_dict, update_homework
from states import WriteHomework


@dp.callback_query_handler(text='cancel_homework', state=WriteHomework)
async def cancel(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer('Отменено')


@dp.callback_query_handler(text='write_homework')
async def select_subject(call: types.CallbackQuery):
    lesson_dict = await get_lesson_dict(call)
    keys = lesson_dict.keys()
    lessons_ikb = await create_lessons_ikb(keys)
    await call.message.edit_text('Выберите предмет', reply_markup=lessons_ikb)
    await WriteHomework.name_lesson.set()


@dp.callback_query_handler(
    lambda call: call.data.startswith('lesson_'),
    state=WriteHomework.name_lesson,
)
async def select_group(call: types.CallbackQuery, state: FSMContext):
    subject = call.data.split('_')[1]
    await state.update_data(name_lesson=subject)
    lesson_dict = await get_lesson_dict(call)
    groups = lesson_dict[subject]
    groups_ikb = await create_groups_ikb(groups)
    await call.message.edit_text('Выберите группу', reply_markup=groups_ikb)
    await WriteHomework.group.set()


@dp.callback_query_handler(
    lambda call: call.data.startswith('group_'), state=WriteHomework.group
)
async def write_homework(call: types.CallbackQuery, state: FSMContext):
    group = call.data.split('_')[1]
    await state.update_data(group=group)
    await call.message.edit_text(
        'Пришлите домашнее задание:', reply_markup=cancel_homework_ikb
    )
    await WriteHomework.write.set()


@dp.message_handler(content_types=['text'], state=WriteHomework.write)
async def write_text(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await update_homework(message, data, message.text, 'Нет файлов')
    await state.finish()


@dp.message_handler(content_types=['photo'], state=WriteHomework.write)
async def write_photo(
    message: types.Message, state: FSMContext, album: List[types.Message]
):
    data = await state.get_data()
    files_name = ' '.join(list(map(lambda x: x.photo[-1].file_id, album)))
    await update_homework(message, data, message.caption, files_name)
    await state.finish()


@dp.message_handler(content_types=['document'], state=WriteHomework.write)
async def write_document(
    message: types.Message, state: FSMContext, album: List[types.Message]
):
    data = await state.get_data()
    files_name = ' '.join(list(map(lambda x: x.document.file_id, album)))
    await update_homework(message, data, message.caption, files_name)
    await state.finish()
