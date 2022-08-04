import json, string

from aiogram import types, Dispatcher
from create_bot import dp


async def cenz_filter(message: types.Message):
    filtered_words = {
        word.lower().translate(str.maketrans("", "", string.punctuation))
        for word in message.text.split(" ")
    }

    with open("cenz.json", "r") as f:
        cenz_words = set(json.load(f))

    if filtered_words.intersection(cenz_words) != set():
        await message.reply("Маты запрещены")
        await message.delete()


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(cenz_filter)
