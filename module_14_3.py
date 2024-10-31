from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton                                                ### - для работы клавиатуры


api = ''                  ###  -  токен как у 03

bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

### - домашнее задание 14_3 _________________________________________________________________

kb = ReplyKeyboardMarkup()                      ### - создание клавиатуры
button = KeyboardButton(text='Рассчитать')      ### - создание и название верхней кнопки ### kb.row kb.insert
button2 = KeyboardButton(text='Информация')     ### - создание и название кнопки
button3 = KeyboardButton(text='Купить')         ### - создание и название кнопки
kb = ReplyKeyboardMarkup(resize_keyboard=True)  ### - придание кнопкам подвижности по ходу изменения размеров приложения
kb.add(button, button2)                   ### - активация кнопок в одном ряду
kb.row(button3)                                 ### - активация кнопок в нижнем ряду отдельно метод kb.row

with open('module_13_5.txt', 'r', encoding='utf-8') as file:
    text_about_calories = file.read()

kb_il = InlineKeyboardMarkup()
button4 = InlineKeyboardButton(text = 'EVLL 1', callback_data='product_buying_1')
button5 = InlineKeyboardButton(text = 'MY PROTEIN 2', callback_data='product_buying_2')
button6 = InlineKeyboardButton(text = 'BCA + 3', callback_data='product_buying_3')
button7 = InlineKeyboardButton(text = 'TITANIUM 4', callback_data='product_buying_4')
kb_il.row(button4, button5, button6, button7)   ### - метод row размещает кнопки в один ряд    ### - (+)

@dp.message_handler(text=['/start'])
async def start_message(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup = kb)

@dp.message_handler(text=['Информация'])
async def inform(message):
    await message.answer(text_about_calories)

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

#______________________________________________________________________________________________

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    await message.answer('Выберите продукт для покупки:', reply_markup = kb_il)

### - 1 _______________________________________________________________________________________

@dp.callback_query_handler(text = 'product_buying_1')            ### - реагирует на инлайн кнопки
async def send_confirm_message1(call):
    await call.message.answer("Вы успешно приобрели EVLL 1, для увеличения взрывной силы !")
                                                                 ### - ответ на нажатие инлайн кнопки
    with open('picther.14_3/1.jpg', 'rb') as img:                ### - открываем картинку из файла files

        await call.message.answer_photo(img, "Название: EVLL 1 | Описание: описание - Добавка | Цена: 1500 р. ",)
        # await call.message.answer_photo(img, "Название: EVLL 1 | Описание: описание - Добавка | Цена: 1500 р. ",). ",
        #                            reply_markup = kb_il)
    await call.answer()

### - 2 _______________________________________________________________________________________

@dp.callback_query_handler(text = 'product_buying_2')
async def send_confirm_message2(call):
    await call.message.answer("Вы успешно приобрели MY PROTEIN 2, для роста мышечной массы!")
    with open('picther.14_3/2.jpg', 'rb') as img:
        await call.message.answer_photo(img, "Название: MY PROTEIN 2 | Описание: описание - Протеин | Цена: 3700 р. ",)
    await call.answer()

### - 3 _______________________________________________________________________________________

@dp.callback_query_handler(text = 'product_buying_3')
async def send_confirm_message3(call):
    await call.message.answer("Вы успешно приобрели BCA + 3, для скорости и ловкости !")
    with open('picther.14_3/3.jpg', 'rb') as img:
        await call.message.answer_photo(img, "Название: BCA + 3 | Описание: описание - BCA Кислота | Цена: 4200 р. ",)
    await call.answer()

### - 4 _______________________________________________________________________________________

@dp.callback_query_handler(text = 'product_buying_4')
async def send_confirm_message4(call):
    await call.message.answer("Вы успешно приобрели TITANIUM 4, для МЕГА МОЩИ !")
    with open('picther.14_3/4.png', 'rb') as img:
        await call.message.answer_photo(img, "Название: TITANIUM 4 | Описание: описание - МЕГА протеин | Цена: 6900 р. ",)
    await call.answer()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

##################################################################################


