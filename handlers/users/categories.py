from aiogram.types import CallbackQuery

from keyboards.inline import categories, menu, back_del
from loader import dp, db, bot


@dp.callback_query_handler(text="categories")
async def show_categories(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=categories)


@dp.callback_query_handler(text="back")
async def show_categories(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=menu)


@dp.callback_query_handler(text="back_del")
async def show_categories(call: CallbackQuery):
    await bot.delete_message(call.message.chat.id, call.message.message_id)


@dp.callback_query_handler(text="самовивіз")
async def show_pickup(call: CallbackQuery):
    x = await db.select_pickup()
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


@dp.callback_query_handler(text="кальян")
async def show_hookah(call: CallbackQuery):
    x = await db.select_hookah()
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


@dp.callback_query_handler(text="алкоголь")
async def show_alcohol(call: CallbackQuery):
    x = await db.select_alcohol()
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


@dp.callback_query_handler(text="бізнес_ланч")
async def show_business_lunch(call: CallbackQuery):
    x = await db.select_business_lunch()
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


@dp.callback_query_handler(text="кава")
async def show_coffee(call: CallbackQuery):
    x = await db.select_coffee()
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
