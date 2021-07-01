from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

tg_link = InlineKeyboardMarkup(row_width=1, inline_keyboard=[[InlineKeyboardButton(text="Напиши нам 📩",
                                                                                   url="https://t.me/ranel_12")],
                                                             [InlineKeyboardButton(text="↩️ Назад️️",
                                                                                   callback_data="back")]])
