
### - домашнее задание 13_4 _________________________________________________________________

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

api = ''

bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text=['/start'])
async def start_message(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

@dp.message_handler(text='Calories')
async def set_age(message: types.Message):
    await message.answer("Введите свой возраст: ")
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост: ")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес: ")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data['age'])
    growth = float(data['growth'])
    weight = float(data['weight'])
    calories = 10 * weight + 6.25 * growth - 5 * age

    await message.answer(f"Ваш приблизительный суточный расход калорий: {calories}")
    await state.finish()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)




















