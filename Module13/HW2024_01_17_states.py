from aiogram import executor, Dispatcher, types, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from bot_api_key import token
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
import asyncio

bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserStates(StatesGroup):
    age = State()
    height = State()
    weight = State()


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(f'Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler(text='Calories')
async def set_age(message: types.Message):
    await message.answer('Введите свой возраст:')
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

    await message.answer(f'Ваша норма калорий: {calories} ккал')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
