import os
import logging
import json
import string

from dotenv import load_dotenv
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

logging.basicConfig(level=logging.INFO)

load_dotenv()
tg_token = os.getenv("TG_TOKEN")
bot = Bot(token=tg_token)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Bot is online')


'''***************************Клиентская часть******************************'''
@dp.message_handler(commands=['start', 'help'])
async def start_command(message: types.Message):
    try:
        await bot.send_message(
            message.from_user.id,
            'Приятного аппетита!',
        )
        await message.delete()
    except Exception as e:
        logging.error(e)
        message_text = '''
        Общение с ботом через ЛС, напишите ему:
        https://t.me/ai_pizzastore_bot
        '''
        await message.reply(
            text=message_text
        )


@dp.message_handler(commands=['Режим_работы',])
async def work_regime_command(message: types.Message):
    user_id=message.from_user.id
    message_text = '''
    Вс-Чт с 9:00 до 20:00 Пт-Сб с 10:00 до 23:00
    '''
    await bot.send_message(
        user_id,
        text=message_text
    )


@dp.message_handler(commands=['Расположение',])
async def place_command(message: types.Message):
    user_id = message.from_user.id
    message_text = '''
    ул. Колбасная, 15
    '''
    await bot.send_message(
        user_id,
        text=message_text
    )
'''*************************Администраторская часть*************************'''


'''*************************Общая часть*************************************'''


@dp.message_handler()
async def cenz_filter(message: types.Message):
    filtered_words = {
        word.lower().translate(str.maketrans('', '', string.punctuation)) for word in message.text.split(' ')
    }
    with open('cenz.json', 'r') as f:
        cenz_words = set(json.load(f))
    if filtered_words.intersection(cenz_words) != set():
        await message.reply('Маты запрещены')
        await message.delete()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
