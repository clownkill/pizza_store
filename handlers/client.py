from aiogram import Dispatcher, types

from create_bot import bot, dp


async def start_command(message: types.Message):
    try:
        await bot.send_message(
            message.from_user.id,
            "Приятного аппетита!",
        )
        await message.delete()
    except Exception as e:
        logging.error(e)
        message_text = """
        Общение с ботом через ЛС, напишите ему:
        https://t.me/ai_pizzastore_bot
        """
        await message.reply(text=message_text)


async def work_regime_command(message: types.Message):
    user_id = message.from_user.id
    message_text = """
    Вс-Чт с 9:00 до 20:00 Пт-Сб с 10:00 до 23:00
    """
    await bot.send_message(user_id, text=message_text)


async def place_command(message: types.Message):
    user_id = message.from_user.id
    message_text = """
    ул. Колбасная, 15
    """
    await bot.send_message(user_id, text=message_text)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=["start", "help"])
    dp.register_message_handler(work_regime_command, commands=['Режим_работы'])
    dp.register_message_handler(place_command, commands=['Расположение'])
