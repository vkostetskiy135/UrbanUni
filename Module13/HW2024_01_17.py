from aiogram import executor, Dispatcher, types, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from bot_api_key import token
bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_message(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)