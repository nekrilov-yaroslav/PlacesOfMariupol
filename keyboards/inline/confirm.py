from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


confirm = InlineKeyboardMarkup(row_width=2,
                               inline_keyboard=[[
                                    InlineKeyboardButton(text="✔️ Yes", callback_data="yes"),
                                    InlineKeyboardButton(text="✖️ No", callback_data="no")]])
