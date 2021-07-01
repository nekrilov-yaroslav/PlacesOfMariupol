from aiogram.dispatcher.filters.state import StatesGroup, State


class Publication(StatesGroup):
    send_text = State()
    send_photo = State()
    final = State()
