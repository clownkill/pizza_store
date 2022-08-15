from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
)


btn_load = KeyboardButton("/Загрузить")
btn_delete = KeyboardButton("/Удалить")

btn_case_admin = ReplyKeyboardMarkup(resize_keyboard=True)
btn_case_admin.add(btn_load).add(btn_delete)
