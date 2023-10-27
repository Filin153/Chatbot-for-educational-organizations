from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand('start', 'Политика бота'),
            types.BotCommand('after_start', 'Авторизация'),
            types.BotCommand('exit', 'Выйти с аккаунта'),
        ]
    )
