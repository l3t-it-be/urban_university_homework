import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message

api = ''

bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())


@dp.message(Command(commands=['start']))
async def start_message(message: Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.')


@dp.message(F.text.in_(['Urban', 'ff']))
async def urban_message(message: Message):
    print('Urban message')
    await message.answer('Urban message')


@dp.message()
async def all_messages(message: Message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    asyncio.run(dp.start_polling(bot, skip_updates=True))
