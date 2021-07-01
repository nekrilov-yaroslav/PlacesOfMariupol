from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

categories = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                    [InlineKeyboardButton(text="🛵Самовивіз", callback_data="самовивіз"),
                                     InlineKeyboardButton(text="💨Кальян", callback_data="кальян")],
                                    [InlineKeyboardButton(text="🍸Алкоголь", callback_data="алкоголь"),
                                     InlineKeyboardButton(text="🍲Бізнес ланч", callback_data="бізнес_ланч")],
                                    [InlineKeyboardButton(text="☕Кава️", callback_data="кава"),
                                     InlineKeyboardButton(text="↩️Назад️️️", callback_data="back")],
                                        ])
