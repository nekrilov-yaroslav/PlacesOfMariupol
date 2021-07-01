from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(row_width=1,
                            inline_keyboard=[
                                    [InlineKeyboardButton(text="🌆 Категорія закладів", callback_data="categories")],
                                    [InlineKeyboardButton(text="🗺 Знайти поруч", callback_data="find_nearby")],
                                    [InlineKeyboardButton(text="📨 Зв`язок", callback_data="communication")],
                                        ])
