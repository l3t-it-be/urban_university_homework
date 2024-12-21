import os
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
    FSInputFile,
)
from crud_functions import (
    initiate_db,
    get_all_products,
    add_product,
    add_user,
    is_included,
)

api = ''

bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())

# Создаем обычную клавиатуру
button = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button3 = KeyboardButton(text='Купить')
button4 = KeyboardButton(text='Регистрация')
kb = ReplyKeyboardMarkup(
    keyboard=[[button], [button2], [button3], [button4]], resize_keyboard=True
)

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

# Создаем инлайн-клавиатуру для продуктов
product_buttons = [
    InlineKeyboardButton(
        text='Супрадин 30 шт.',
        callback_data='product_buying',
    ),
    InlineKeyboardButton(
        text='Супрадин 10 шт. шипучие',
        callback_data='product_buying',
    ),
    InlineKeyboardButton(
        text='Супрадин 60 шт.',
        callback_data='product_buying',
    ),
    InlineKeyboardButton(
        text='Супрадин 20 шт. шипучие', callback_data='product_buying'
    ),
]
product_kb = InlineKeyboardMarkup(
    inline_keyboard=[[button] for button in product_buttons],
    resize_keyboard=True,
)

# Словарь для сопоставления названий продуктов и имен файлов изображений
product_images = {
    'Супрадин 30 шт.': '30_pills.png',
    'Супрадин 10 шт. шипучие': '10_effervescent.png',
    'Супрадин 60 шт.': '60_pills.png',
    'Супрадин 20 шт. шипучие': '20_effervescent.png',
}


@dp.message(Command(commands=['start']))
async def start_message(message: Message):
    await message.answer(
        'Привет! Я бот, помогающий твоему здоровью.', reply_markup=kb
    )


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


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


@dp.message(F.text == 'Купить')
async def get_buying_list(message: Message):
    products = get_all_products()
    for product in products:
        product_name = product[1]
        image_filename = product_images.get(product_name)
        if image_filename and os.path.exists(f'pictures/{image_filename}'):
            caption = f'Название: {product_name} | Описание: {product[2]} | Цена: {product[3]} руб.'
            img = FSInputFile(f'pictures/{image_filename}')
            await bot.send_photo(
                chat_id=message.chat.id, photo=img, caption=caption
            )
        else:
            await message.answer(
                f'Название: {product_name} | Описание: {product[2]} | Цена: {product[3]} руб. | Изображение не найдено.'
            )

    await message.answer(
        'Выберите продукт для покупки:', reply_markup=product_kb
    )


@dp.callback_query(F.data == 'product_buying')
async def send_confirm_message(call: CallbackQuery):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.message(F.text == 'Регистрация')
async def sign_up(message: Message, state: FSMContext):
    await message.answer(
        'Введите имя пользователя (только латинский алфавит):'
    )
    await state.set_state(RegistrationState.username)


@dp.message(RegistrationState.username)
async def set_username(message: Message, state: FSMContext):
    username = message.text
    if is_included(username):
        await message.answer('Пользователь существует, введите другое имя:')
        await state.set_state(RegistrationState.username)
    else:
        await state.update_data(username=username)
        await message.answer('Введите свой email:')
        await state.set_state(RegistrationState.email)


@dp.message(RegistrationState.email)
async def set_email(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await state.set_state(RegistrationState.age)


@dp.message(RegistrationState.age)
async def set_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    await message.answer('Регистрация прошла успешно')
    await state.clear()


@dp.message(F.text.in_({'Рассчитать', 'Информация', 'Купить', 'Регистрация'}))
async def all_messages(message: Message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    initiate_db()
    add_product('Супрадин 30 шт.', 'таблетки покрытые оболочкой', 1000)
    add_product('Супрадин 10 шт. шипучие', 'таблетки шипучие', 1200)
    add_product('Супрадин 60 шт.', 'таблетки покрытые оболочкой', 1600)
    add_product('Супрадин 20 шт. шипучие', 'таблетки шипучие', 2000)
    asyncio.run(dp.start_polling(bot, skip_updates=True))
