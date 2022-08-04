import os

from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from dotenv import load_dotenv


storage = MemoryStorage()

load_dotenv()
tg_token = os.getenv("TG_TOKEN")
bot = Bot(token=tg_token)
dp = Dispatcher(bot, storage=storage)
