from aiogram import Dispatcher


async def on_startup_notify(dp: Dispatcher):
    await dp.bot.send_message(chat_id="2002268318", text="Bot Started")
