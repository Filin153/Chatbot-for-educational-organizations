from aiogram.dispatcher.filters.state import State, StatesGroup


class AddTeacher(StatesGroup):
    full_name = State()
    password = State()


class ResetDepartament(StatesGroup):
    password = State()
