from loader import dp, Bot
from aiogram import F
from aiogram.types import Message, FSInputFile, URLInputFile, BufferedInputFile
from aiogram.filters import Command


@dp.message(F.text == 'Привет')
async def func_name_1(message: Message):
    """
    обработчик, который реагирует на текст "Привет"
    """
    await message.answer(message.text)


@dp.message(F.text == 'Сделай комплимент')
async def func_name_1(message: Message):
    """
    обработчик, который реагирует на текст "Сделай комплимент"
    """
    await message.answer(text='Ты хороший программист!')


@dp.message(F.text == 'Мне скучно. Что бы поделать?')
async def func_name_1(message: Message):
    """
    обработчик, который реагирует на текст "Мне скучно. Что бы поделать?"
    """
    await message.answer(text='Ты можешь поиграть в METRO ROYALE в PUBG MOBILE или пойди учи PYTHON')


@dp.message(Command('metro'))
async def func_name_2(message: Message):
    """
    обработчик, который реагирует на команду /metro
    """
    await message.answer(text='Ты нажал команду /metro и иди играй в METRO ROYALE в PUBG MOBILE')


@dp.message(F.text == 'Что приготовить?')
async def func_name_1(message: Message):
    """
    обработчик, который реагирует на текст "Что приготовить?"
    """
    await message.answer(text='Выбирай что хочешь на https://www.russianfood.com/')