from aiogram import Dispatcher
from data.config import admins_id


async def on_startup_notify(dp: Dispatcher):
    for admin_id in admins_id:
        try:
            await dp.bot.send_message(chat_id=admin_id, text='Bot Started')
        except Exception:
            pass
