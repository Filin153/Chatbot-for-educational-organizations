import asyncio

import requests
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from buttons.bt_menu import red_menu, menu
from buttons.dt_send_schedule import schedule_buttons, prepod_schedule_buttons
from db.create_user import send_user_group
from db.redactor import send_redactor
# from load_schedule.make_massage import My_schedule
from config import IP, PORT
import requests
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz, process

from сomponents.make_schedule import PrepodSchedule, MakeSchedule


class prepod_name(StatesGroup):
    last_name = State()
    day = State()

async def name_prepod(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('Отправьте фамилию преподавателя')
    await prepod_name.last_name.set()


async def take_all_prepod(name):
    all_prepod = []
    similarity = []

    r = requests.get("https://rksi.ru/mobile_schedule")
    soup = BeautifulSoup(r.text, "lxml")
    pr_tb_soup = soup.find("select", {"name": "teacher"})
    all_prepod_soup = pr_tb_soup.find_all("option", )

    for i in all_prepod_soup:
        all_prepod.append(str(i.text))

    if all_prepod.count(name) == 0:
        matching_strings = process.extract(name, all_prepod, scorer=fuzz.partial_token_sort_ratio, limit=3)

        for string, score in matching_strings:
            similarity.append(f"<code>{string}</code>\n")

        return similarity

async def name_p(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text


        _, red_id = send_redactor()
        if data['name'] == '/start':
            await state.finish()
            if red_id.count(str(message.from_user.id)):
                await message.answer('Меню:', reply_markup=red_menu)
            else:
                await message.answer('Меню:', reply_markup=menu)
        else:
            res = await take_all_prepod(data['name'])
            if not res:
                prepod_chedule = PrepodSchedule(prepod_name=data['name'])
                schedule_info = await prepod_chedule.run()
                msg_schedule = schedule_info.schedule
                try:
                    await message.answer(str(msg_schedule), reply_markup=schedule_buttons, parse_mode="HTML")
                    await state.finish()
                except:
                    msg = MakeSchedule().share_msg(msg_schedule)
                    firstText = await message.edit_text(next(msg), parse_mode="HTML")
                    await message.answer(next(msg), reply_markup=schedule_buttons, parse_mode="HTML")
                    try:
                        delMsg = await firstText.reply('Удалится через 2 мин')
                        await asyncio.sleep(120)
                        await delMsg.delete()
                        await firstText.delete()
                    except:
                        pass

                    await state.finish()
                # await message.answer('Какой день:', reply_markup=prepod_schedule_buttons)
                # await prepod_name.next()
            else:
                await message.answer(f'Похожие варианты:\n{"".join(res)}', parse_mode='HTML')
                await message.answer(f'Отправьте фамилию преподавателя:')

# async def day_p(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['day'] = message.text
#
#         _, red_id = send_redactor()
#     if data['day'] == '/start' or data['day'] == '/menu':
#         await state.finish()
#         if red_id.count(str(message.from_user.id)):
#             await message.answer('Меню:', reply_markup=red_menu)
#         else:
#             await message.answer('Меню:', reply_markup=menu)
#     else:
#         if data['day'] == 'На сегодня':
#             await state.finish()
#             r = requests.get(f'http://load_schedule_api:{PORT}/getprepodschedule/{data["name"]}/today')
#             if r.status_code == 200:
#                 if str(r.text) == "0":
#                     await message.answer(await send_schedule_prepod(data['name']), reply_markup=schedule_buttons, parse_mode="HTML")
#                     await state.finish()
#                 else:
#                     await message.answer(r.text.replace(r'\n', '\n')[1:-1], reply_markup=schedule_buttons)
#             else:
#                 await message.answer('🥲Расписания нету', reply_markup=schedule_buttons)
#         elif data['day'] == 'На завтра':
#             await state.finish()
#             r = requests.get(f'http://load_schedule_api:{PORT}/getprepodschedule/{data["name"]}/tomorrow')
#             if r.status_code == 200:
#                 if str(r.text) == "0":
#                     await message.answer(await send_schedule_prepod(data['name']), reply_markup=schedule_buttons, parse_mode="HTML")
#                     await state.finish()
#                 else:
#                     await message.answer(r.text.replace(r'\n', '\n')[1:-1], reply_markup=schedule_buttons)
#             else:
#                 await message.answer('🥲Расписания нету', reply_markup=schedule_buttons)
#         elif data['day'] == 'На неделю':
#             await message.answer(await send_schedule_prepod(data['name']), reply_markup=schedule_buttons, parse_mode="HTML")
#             await state.finish()
#         else:
#             await state.finish()
#             await message.reply('Неверный день', reply_markup=schedule_buttons)





def reg_hand_prepod_send_schedule(dp: Dispatcher):
    dp.register_callback_query_handler(name_prepod, text='prepod')
    dp.register_message_handler(name_p, state=prepod_name.last_name)
    # dp.register_message_handler(day_p, state=prepod_name.day)