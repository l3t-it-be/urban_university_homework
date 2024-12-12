import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (
    Message,
    KeyboardButton,
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
)

api = ''

bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())

# Создаем обычную клавиатуру
button = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
kb = ReplyKeyboardMarkup(keyboard=[[button], [button2]], resize_keyboard=True)

# Создаем инлайн-клавиатуру
inline_button_calories = InlineKeyboardButton(
    text='Рассчитать норму калорий', callback_data='calories'
)
inline_button_formulas = InlineKeyboardButton(
    text='Формулы расчёта', callback_data='formulas'
)
inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[[inline_button_calories], [inline_button_formulas]],
    resize_keyboard=True,
)


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
async def main_menu(message: Message):
    await message.answer('Выберите опцию:', reply_markup=inline_kb)


@dp.callback_query(F.data == 'formulas')
async def get_formulas(call: CallbackQuery):
    await call.message.answer(
        'Формула Миффлина-Сан Жеора для женщин: '
        'BMR = 10 * вес + 6.25 * рост - 5 * возраст - 161'
    )
    await call.answer()


@dp.callback_query(F.data == 'calories')
async def set_age(call: CallbackQuery, state: FSMContext):
    await call.message.answer('Введите свой возраст:')
    await state.set_state(UserState.age)


@dp.message(UserState.age)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост (в см):')
    await state.set_state(UserState.growth)


@dp.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес (в кг):')
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
