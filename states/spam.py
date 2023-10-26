from aiogram.dispatcher.filters.state import State, StatesGroup


class Spam(StatesGroup):
    group = State()
    message = State()
