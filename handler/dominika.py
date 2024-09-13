from loader import dp, Bot
from aiogram import F,types
from aiogram.types import Message, FSInputFile, URLInputFile, BufferedInputFile
from aiogram.filters import Command
@dp.message(Command("weather"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Гродно"),
            types.KeyboardButton(text="Брест"),
            types.KeyboardButton(text="Витебск"),
            types.KeyboardButton(text="Гомель"),
            types.KeyboardButton(text="Минск"),
            types.KeyboardButton(text="Могилев")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите город"
    )
    await message.answer("В каком городе?", reply_markup=keyboard)

@dp.message(F.text == "Гродно")
async def func_name_1(message: types.Message):
    await message.answer("+22")
@dp.message(F.text == "Брест")
async def func_name_2(message: types.Message):
    await message.answer("+24")
@dp.message(F.text == "Витебск")
async def func_name_3(message: types.Message):
    await message.answer("+18")
@dp.message(F.text == "Гомель")
async def func_name_4(message: types.Message):
    await message.answer("+21")
@dp.message(F.text == "Минск")
async def func_name_5(message: types.Message):
    await message.answer("+23")
@dp.message(F.text == "Могилев")
async def func_name_6(message: types.Message):
    await message.answer("+20")
@dp.message(F.text == "Спасибо")
async def func_name_7(message: Message):
    """
    обработчик, который реагирует на команду /photo
    """
    image = FSInputFile('data/image/3.jpg')

    await message.answer_photo(image)