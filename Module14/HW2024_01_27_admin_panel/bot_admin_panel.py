from aiogram import executor, Dispatcher, types, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from bot_api_key import token
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import crud_functions

bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())


kb = ReplyKeyboardMarkup(resize_keyboard=True)
info_button = KeyboardButton(text='Информация')
calculate_button = KeyboardButton(text='Рассчитать')
purchase_button = KeyboardButton(text='Купить')
kb.row(info_button, calculate_button)
kb.row(purchase_button)

ikb = InlineKeyboardMarkup()
calories_button = InlineKeyboardButton(text= 'Рассчитать норму калорий', callback_data='calories')
formulas_button = InlineKeyboardButton(text= 'Формулы расчёта', callback_data='formulas')
ikb.add(calories_button, formulas_button)

products_ikb = InlineKeyboardMarkup()
product1 = InlineKeyboardButton(text='Product 1', callback_data='buy_product1')
product2 = InlineKeyboardButton(text='Product 2', callback_data='buy_product2')
product3 = InlineKeyboardButton(text='Product 3', callback_data='buy_product3')
product4 = InlineKeyboardButton(text='Product 4', callback_data='buy_product4')
products_ikb.add(product1, product2, product3, product4)
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

@dp.message_handler(text=['Купить'])
async def get_buying_list(message: types.Message):
    products = crud_functions.get_all_products()
    for product in products:
        product_id, title, description, price, image_path = product
        with open(image_path, 'rb') as image:
            await message.answer_photo(image, caption=f'Название: {title} | Описание: {description} | Цена: {price} руб.')
    await message.answer('Выберите продкут для покупки:', reply_markup=products_ikb)

#Реагириуте не на product_buying, потому что я хотел добавить распознавание какой именно продукт приобрели
@dp.callback_query_handler(Text(startswith='buy_'))
async def send_confirm_message(call: types.CallbackQuery):
    product_title = call.data[len('buy_'):]
    product_data = crud_functions.get_product_by_title(product_title)
    product_id, title, description, price, image_path = product_data
    with open(image_path, 'rb') as image:
        await call.message.answer_photo(image,
        caption=f'Поздравляем, вы приобрели {title} за {price}', reply_markup=kb)

@dp.message_handler()
async def initial_message(message: types.Message):
    await message.answer(f'Введите команду /start, что бы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)