### - module_14_5.py
### - 06.11.24
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import state
from aiogram.types import CallbackQuery
import asyncio
import itertools
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram import executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton, callback_query                                            ### - для работы клавиатуры
from crud_functions_14_4 import *
import sqlite3
import cursor

from crud_functions_14_5 import is_included, add_user

api = ''                              ###  -  токен как у 03

bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    reg_age = State()
    balance = State()

kb = ReplyKeyboardMarkup()                      ### - создание клавиатуры
button = KeyboardButton(text='Рассчитать')      ### - создание и название верхней кнопки ### kb.row kb.insert
button2 = KeyboardButton(text='Информация')     ### - создание и название кнопки
button3 = KeyboardButton(text='Купить')         ### - создание и название кнопки
button8 = KeyboardButton(text='Регистрация')    ### - создание и название кнопки
kb = ReplyKeyboardMarkup(resize_keyboard=True)  ### - придание кнопкам подвижности по ходу изменения размеров приложения
kb.add(button, button2)                   ### - активация кнопок в одном ряду
kb.row(button3, button8)                  ### - активация кнопок в нижнем ряду отдельно метод kb.row

with open('module_13_5.txt', 'r', encoding='utf-8') as file:
    text_about_calories = file.read()

kb_il = InlineKeyboardMarkup()
button4 = InlineKeyboardButton(text = 'EVLL 1', callback_data= 'product_buying_1')
button5 = InlineKeyboardButton(text = 'MY PROTEIN 2', callback_data='product_buying_2')
button6 = InlineKeyboardButton(text = 'BCA + 3', callback_data='product_buying_3')
button7 = InlineKeyboardButton(text = 'TITANIUM 4', callback_data='product_buying_4')
kb_il.row(button4, button5, button6, button7)   ### - метод row размещает кнопки в один ряд

@dp.message_handler(text=['/start'])
async def start_message(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup = kb)

@dp.message_handler(text=['Информация'])
async def inform(message):
    await message.answer(text_about_calories)

@dp.message_handler(text='Регистрация')
async def sing_up(message: types.Message, state: FSMContext):
    await message.answer("Введите имя пользователя (только латинский алфавит): ")
    await RegistrationState.username.set()                                              ###     +++ <<<

@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text                           ### - обновляет username на message.text
    if is_included(username):                   ### - проверка наличия имени через модуль crud_functions_14_5.py
        await message.answer("Пользователь существует, введите другое имя: ")
        return
    await state.update_data(username=username)        ### - данные сохраняются в правильном поле username.
    await message.answer("Введите свой email: ")
    await RegistrationState.email.set()               ### - Переход к следующему состоянию

@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer("Введите свой возраст: ")
    await RegistrationState.reg_age.set()

@dp.message_handler(state=RegistrationState.reg_age)
async def set_age(message: types.Message, state: FSMContext):
    age = int(message.text)
    await state.update_data(reg_age=age)
    data = await state.get_data()
    data['balance'] = 1000
    await message.answer("Ваши данные добавлены в базу данных SQL - database_14_5 : ")
    add_user(data['username'], data['email'], data['reg_age'], data['balance'] )     ### - Используем данные из словаря
    await state.finish()                                                             ### - Завершаем состояние

@dp.message_handler(text='Рассчитать')
async def set_age(message: types.Message, state: FSMContext):
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

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    await message.answer('Выберите продукт для покупки:', reply_markup = kb_il)

###_______________________________________________________________________________________________________________

connection = sqlite3.connect('database_14_4a.db')                ### - создание соеденения с БД
cursor = connection.cursor()

###________________________   Обработка четырех инлайн кнопок   ____________________________________________________

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('product_buying_'))  ### - реагирует на инлайн кнопки
async def send_confirm_message1(Callback_query: types.CallbackQuery, connection=connection, cursor=cursor):
    product_id = Callback_query.data.split('_')[-1]              ### - создание значения (числа) для
                                                                  ## обращения к - id продукта (строке с данными) из
                                                                   # сallback_data по последней цифре product_buying_1

    cursor.execute('SELECT title, description, price FROM Products WHERE id == ?', (product_id,))
    result = cursor.fetchone()                                   ### - Получаем результат запроса
    if result:                                                   ### - Проверяем, что результат не пустой
        title = result[0]                               ### - заново присваеваем переменным индексы из result
        description = result[1]                         ### - заново присваеваем переменным индексы
        price = result[2]                               ### - заново присваеваем переменным индексы
        await Callback_query.message.answer(F"Вы успешно приобрели {title},  для улучшения тренировок !")
        with open(f'picther.14_3/{product_id}.jpg', 'rb') as img:
            await Callback_query.message.answer_photo(img,
                                        f" Название: {title} | Описание: {description} | Цена: {price} р. ")
    await Callback_query.answer()
    # connection.close()                                           ### - <<< НУЖНО ЛИ ЗАКРЫВАТЬ СОЕДЕНЕНИЕ   ???

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

###################################################################################################################