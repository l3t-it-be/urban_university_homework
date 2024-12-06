import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.fsm.storage.memory import MemoryStorage

api = ''

bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())

logging.basicConfig(level=logging.INFO)


@dp.message(F.text.in_(['/start']))
async def start_message(message):
    print('Привет! Я бот помогающий твоему здоровью.')


@dp.message(F.text.in_(['Urban', 'ff']))
async def urban_message(message):
    print('Urban message')


@dp.message()
async def all_messages(message):
    print('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    asyncio.run(dp.start_polling(bot, skip_updates=True))
