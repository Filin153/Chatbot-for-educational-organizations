from aiogram.dispatcher.filters.state import State, StatesGroup


class Register(StatesGroup):
    accept = State()
    group = State()
    fio = State()
    password_departament = State()
