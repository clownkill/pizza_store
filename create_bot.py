import os

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from dotenv import load_dotenv


load_dotenv()
tg_token = os.getenv("TG_TOKEN")
bot = Bot(token=tg_token)
dp = Dispatcher(bot)
