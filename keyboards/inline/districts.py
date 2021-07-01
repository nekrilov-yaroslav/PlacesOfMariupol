from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


districts = InlineKeyboardMarkup(row_width=1,
                                 inline_keyboard=[
                                    [InlineKeyboardButton(text="🏛 Центральний", callback_data="1")],
                                    [InlineKeyboardButton(text="🏗 Приморський", callback_data="2")],
                                    [InlineKeyboardButton(text="🏙 Лівий берег", callback_data="3")],
                                    [InlineKeyboardButton(text="↩️ Назад️️", callback_data="back")]
                                        ])
