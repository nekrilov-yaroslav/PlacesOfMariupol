from aiogram.types import CallbackQuery

from keyboards.inline import districts, back_del
from loader import dp, db


@dp.callback_query_handler(text="find_nearby")
async def find_nearby(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=districts)


@dp.callback_query_handler(text="1")
async def show_central(call: CallbackQuery):
    x = await db.select_d_central()
    result = ''
    for i in range(len(x)):
        name = x[i].get('name')
        phone = x[i].get('phone')
        address = x[i].get('address')
        district = x[i].get('district')
        website = x[i].get('website')
        y = f"<b>{name}</b>\n☎️ {phone}\n📍Адреса: {address}\n🗺Район: {district}\n<a href='{website}'>🌐Website</a>\n\n"
        result += y
    await call.message.answer(text=result, disable_web_page_preview=True, reply_markup=back_del)


@dp.callback_query_handler(text="2")
async def show_seaside(call: CallbackQuery):
    x = await db.select_d_seaside()
    result = ''
    for i in range(len(x)):
        name = x[i].get('name')
        phone = x[i].get('phone')
        address = x[i].get('address')
        district = x[i].get('district')
        website = x[i].get('website')
        y = f"<b>{name}</b>\n☎️ {phone}\n📍Адреса: {address}\n🗺Район: {district}\n<a href='{website}'>🌐Website</a>\n\n"
        result += y
    await call.message.answer(text=result, disable_web_page_preview=True, reply_markup=back_del)


@dp.callback_query_handler(text="3")
async def show_left_coast(call: CallbackQuery):
    x = await db.select_d_left_coast()
    result = ''
    for i in range(len(x)):
        name = x[i].get('name')
        phone = x[i].get('phone')
        address = x[i].get('address')
        district = x[i].get('district')
        website = x[i].get('website')
        y = f"<b>{name}</b>\n☎️ {phone}\n📍Адреса: {address}\n🗺Район: {district}\n<a href='{website}'>🌐Website</a>\n\n"
        result += y
    await call.message.answer(text=result, disable_web_page_preview=True, reply_markup=back_del)
