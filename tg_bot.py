import logging

from aiogram.utils import executor

from create_bot import dp
from handlers import admin, client, other

logging.basicConfig(level=logging.INFO)


async def on_startup(_):
    print('Bot is online')


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
