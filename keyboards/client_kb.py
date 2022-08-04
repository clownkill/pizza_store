from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
)


btn_regime = KeyboardButton("/Режим_работы")
btn_place = KeyboardButton("/Расположение")
btn_menu = KeyboardButton("/Меню")

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(btn_regime).add(btn_place).add(btn_menu).add(btn_contacts).add(btn_geoposition)
