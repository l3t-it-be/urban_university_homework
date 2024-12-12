import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup

api = ''

bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())

button = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')

# Создаем клавиатуру и добавляем кнопки
kb = ReplyKeyboardMarkup(keyboard=[[button], [button2]], resize_keyboard=True)


@dp.message(Command(commands=['start']))
async def start_message(message: Message):
    await message.answer(
        'Привет! Я бот, помогающий твоему здоровью.', reply_markup=kb
    )


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message(F.text == 'Рассчитать')
async def set_age(message: Message, state: FSMContext):
    await message.answer('Введите свой возраст: ')
    await state.set_state(UserState.age)


@dp.message(UserState.age)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост (в см): ')
    await state.set_state(UserState.growth)


@dp.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес (в кг): ')
    await state.set_state(UserState.weight)


@dp.message(UserState.weight)
async def send_calories(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    # Упрощённая формула Миффлина - Сан Жеора для женщин
    bmr = 10 * weight + 6.25 * growth - 5 * age - 161

    await message.answer(f'Ваша норма калорий: {bmr} ккал')
    await state.clear()


@dp.message()
async def all_messages(message: Message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    asyncio.run(dp.start_polling(bot, skip_updates=True))
