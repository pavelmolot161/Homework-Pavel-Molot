from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ''

bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())

### - домашнее задание 13_3 _________________________________________________________________

@dp.message_handler(text = ['/start'])
async def start_message(message):
    # print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer("Привет! Я бот помогающий твоему здоровью.")
@dp.message_handler()
async def all_message(message):
    # print('Введите команду /start, чтобы начать общение.')
    await message.answer("Введите команду /start, чтобы начать общение.")
#________________________________________________________________________________________________
@dp.message_handler(text = ['Urban'])
async def urban_message(message):
    print("Urban message")
    await message.answer ("Urban сообщение из await !")

@dp.message_handler(text = ['start'])
async def start_message(message):
    print("Start message")
    await message.answer("Рады вас видеть в нашем боте (из await) !")

@dp.message_handler()
async def all_message(message):
    print('Мы получили сообщение')
    await message.answer(message.text.upper()) ### - то что отправил, то и ответит (эхо бот)

if __name__ == "__main__":

    executor.start_polling(dp, skip_updates=True)