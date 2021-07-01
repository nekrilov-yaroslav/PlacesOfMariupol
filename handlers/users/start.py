import logging

import asyncpg.exceptions
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from keyboards.inline import menu
from loader import dp, db


@dp.message_handler(Command("start"))
async def bot_start(message: types.Message):
    await message.answer(f"\nПривіт, {message.from_user.full_name} 👋. Я – бот <b>Mariupol Places</b>. "
                         f"\nЯ допожу тобі обрати, куди краще сходити та повідомлю про нові заклади "
                         f"або цікаві події у місті Маріуполь🏙 ")
    try:
        await db.add_user(fullname=message.from_user.full_name,
                          username=message.from_user.username,
                          telegram_id=message.from_user.id)
    except asyncpg.exceptions.UniqueViolationError as err:
        logging.info("add user error:\n" + str(err))

    await message.answer(f"Оберіть та натисніть необхідну кнопку:", reply_markup=menu)
