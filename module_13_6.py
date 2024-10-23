from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton                ### - для работы клавиатуры
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton         ### - для работы инлайн клавиатуры


api = ''                       ###  -  токен как у 03

bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

### - домашнее задание 13_6 _________________________________________________________________

@dp.message_handler(text=['/start'])
async def start_message(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

kb = InlineKeyboardMarkup()
button = InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data='calories')
button2 = InlineKeyboardButton(text = 'Формулы расчёта', callback_data='formulas')
kb.add(button, button2)

with open('module_13_6.txt', 'r', encoding='utf-8') as file:
    text_about_calories = file.read()

@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup = kb)           ### - кнопка прилипушка
    await message.answer()

@dp.callback_query_handler(text = 'formulas')                            ### - на какую кнопку хендлер будет отрабатывать
async def get_formulas(call):
    await call.message.answer(text_about_calories)
    await call.answer()

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer("Введите свой возраст: ")
    await UserState.age.set()
#______________________________________________________________________________________________

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
