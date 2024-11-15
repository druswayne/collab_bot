from loader import dp, Bot
from aiogram import F
from aiogram.types import Message, FSInputFile, URLInputFile, BufferedInputFile
from aiogram.filters import Command
import random
import os


@dp.message(F.text == 'Что послушать')
async def func_name_1(message: Message):
    """
    обработчик, который реагирует на текст ""
    """
    await message.answer(text= "Советую тебе послушать группу Metallica, red hot chilly peppers и pink floyd")

@dp.message(F.text == ('Посоветуй фильм'))
async def func_name_2(message: Message):
    """
    обработчик, который реагирует
    """
    await message.answer(text='Советую тебе фильмы "Forest Gump", "Kill Bill" и серию кинофильмов "Star Wars"')

@dp.message(Command('RandomGame'))
async def func_name_3(message: Message):
    list_image = os.listdir('data/games')
    url = f'data/games/{random.choice(list_image)}'
    photo = FSInputFile(url)
    await message.answer_photo(photo, caption='держи игру')

