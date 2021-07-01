from aiogram.types import CallbackQuery

from keyboards.inline import tg_link
from loader import dp


@dp.callback_query_handler(text="communication")
async def communication(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=tg_link)
