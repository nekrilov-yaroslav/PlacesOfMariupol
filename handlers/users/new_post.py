import logging
import time

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import ContentType, CallbackQuery

from filters import IsAdmin
from keyboards.inline import confirm
from loader import dp, bot, db
from states import Publication


@dp.message_handler(IsAdmin(), Command("new_post"))
async def new_post(message: types.Message):
    await message.answer(f"Ожидаю текст к новой публикации...")
    await Publication.send_text.set()


@dp.message_handler(IsAdmin(), state=Publication.send_text)
async def get_text(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data(text=text)
    await message.answer("Ваш текст принят. \nОжидаю фото для публикации...")
    await Publication.send_photo.set()


@dp.message_handler(IsAdmin(), state=Publication.send_photo, content_types=ContentType.PHOTO)
async def get_photo(message: types.Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    await state.update_data(photo_id=photo_id)
    await message.answer("Ваше фото принято. \nОжидаю подтверждение публикации...")
    await Publication.final.set()
    data = await state.get_data()
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photo_id,
                         caption=data.get('text'),
                         reply_markup=confirm)


@dp.callback_query_handler(text="yes", state=Publication.final)
async def show_categories(call: CallbackQuery, state: FSMContext):
    await call.answer(text="Рассылка производится...")
    data = await state.get_data()
    users = await db.select_users()
    for i in range(len(users)):
        try:
            await bot.send_photo(chat_id=users[i].get('telegram_id'),
                                 photo=data.get('photo_id'),
                                 caption=data.get('text'))
            time.sleep(2)
        except Exception as err:
            logging.exception(err)
    await state.finish()


@dp.callback_query_handler(text="no", state=Publication.final)
async def show_categories(call: CallbackQuery, state: FSMContext):
    await call.answer(text="Рассылка отменина...")
    await state.finish()
