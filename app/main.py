import os
from aiogram import Bot, Dispatcher, exceptions, types

parent_dir = os.path.dirname(os.path.dirname(__file__))
TOKEN = os.environ["API_TOKEN"]
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply("Hello! \nI am a test bot)) \n Send me any message")
