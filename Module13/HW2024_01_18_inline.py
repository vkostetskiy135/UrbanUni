from aiogram import executor, Dispatcher, types, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import state

from bot_api_key import token
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())


kb = ReplyKeyboardMarkup(resize_keyboard=True)
info_button = KeyboardButton(text='Информация')
calculate_button = KeyboardButton(text='Рассчитать')
kb.row(info_button, calculate_button)

ikb = InlineKeyboardMarkup()
calories_button = InlineKeyboardButton(text= 'Рассчитать норму калорий', callback_data='calories')
formulas_button = InlineKeyboardButton(text= 'Формулы расчёта', callback_data='formulas')
ikb.add(calories_button, formulas_button)


class UserStates(StatesGroup):
    age = State()
    height = State()
    weight = State()
    calories = State()


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(f'Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text=["Рассчитать"])
async def main_menu(message: types.Message):
    await message.answer('Выберите опцию', reply_markup=ikb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer(f'10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (г) + 5')


@dp.callback_query_handler(text='calories')
async def set_age(call: types.CallbackQuery):
    await call.message.answer('Введите свой возраст:')
    await UserStates.age.set()


@dp.message_handler(state=UserStates.age)
async def set_height(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserStates.height.set()


@dp.message_handler(state=UserStates.height)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(height=message.text)
    await message.answer('Введите свой вес:')
    await UserStates.weight.set()


@dp.message_handler(state=UserStates.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    print(data)
    age = int(data['age'])
    height = int(data['height'])
    weight = int(data['weight'])

    # Упрощенная формула Миффлина - Сан Жеора для подсчета нормы калорий
    calories = 10 * weight + 6.25 * height - 5 * age + 5  # Для мужчин

    await state.update_data(calories=calories)

    await message.answer(f'Ваша норма калорий: {calories} ккал', reply_markup=kb)
    await state.finish()

#Пытался сделать функцию информации по прошлым запросам, но что бы это корректно работало, нужна бд
# @dp.message_handler(text= 'Информация')
# async def information(message: types.Message, state: FSMContext):
#     data = await state.get_data()
#     await message.answer(f'''
#     Вот информация по вашему прошлому запросу:
#
#     Возраст - {data['age']}
#     Рост - {data['height']}
#     Вес - {data['weight']}
#
#     Калории - {data['calories']}
#     ''', reply_markup=kb)


@dp.message_handler()
async def initial_message(message: types.Message):
    await message.answer(f'Введите команду /start, что бы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)