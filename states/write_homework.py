from aiogram.dispatcher.filters.state import State, StatesGroup


class WriteHomework(StatesGroup):
    name_lesson = State()
    group = State()
    write = State()


class CheckHomework(StatesGroup):
    name_lesson = State()
    group = State()
