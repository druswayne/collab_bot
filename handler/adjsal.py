import random

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


@dp.message(F.text == 'как дела')
async def func_name_1(message: Message):
    """
    обработчик, который реагирует на текст "Привет"
    """
    a = random.randint(1,3)
    if a == 1:
       await message.answer('нормис')
    if a == 2:
       await message.answer('круто')
    if a == 3:
       await message.answer('плоха')

@dp.message(F.text == 'любое слово')
async def func_name_1(message: Message):
    """
    обработчик, который реагирует на текст "Привет"
    """
    a = random.randint(1,52)
    if a == 1:
       await message.answer('холодильник')
    if a == 2:
       await message.answer('айфон')
    if a == 3:
       await message.answer('бумага')
    if a == 4:
       await message.answer('ручка')
    if a == 5:
       await message.answer('яблоко')
    if a == 6:
       await message.answer('арбуз')
    if a == 7:
       await message.answer('машина')
    if a == 8:
       await message.answer('компьеютер')
    if a == 9:
       await message.answer('сыр')
    if a == 10:
       await message.answer('автобус')
    if a == 11:
       await message.answer('бес')
    if a == 12:
       await message.answer('демон')
    if a == 13:
       await message.answer('учеба')
    if a == 14:
       await message.answer('кросворд')
    if a == 15:
       await message.answer('магазин')
    if a == 16:
       await message.answer('корова')
    if a == 17:
       await message.answer('трактор')
    if a == 18:
       await message.answer('самосвал')
    if a == 19:
       await message.answer('мусор')
    if a == 20:
       await message.answer('муха')
    if a == 21:
       await message.answer('клещ')
    if a == 22:
       await message.answer('гитара')
    if a == 23:
       await message.answer('кларнет')
    if a == 24:
       await message.answer('скрипка')
    if a == 25:
       await message.answer('барабан')
    if a == 26:
       await message.answer('колокольчик')
    if a == 27:
       await message.answer('треугольник')
    if a == 28:
       await message.answer('квадрат')
    if a == 29:
       await message.answer('прямоугольник')
    if a == 30:
       await message.answer('параллелепипед')
    if a == 31:
       await message.answer('ромб')
    if a == 32:
       await message.answer('пятиугольник')
    if a == 33:
       await message.answer('квас')
    if a == 34:
       await message.answer('кола')
    if a == 35:
       await message.answer('фанта')
    if a == 36:
       await message.answer('хомяк')
    if a == 37:
       await message.answer('собака')
    if a == 38:
       await message.answer('кот')
    if a == 39:
       await message.answer('страус')
    if a == 40:
       await message.answer('жираф')
    if a == 41:
       await message.answer('индюк')
    if a == 42:
       await message.answer('комар')
    if a == 43:
       await message.answer('тумба')
    if a == 44:
       await message.answer('шкаф')
    if a == 45:
       await message.answer('стол')
    if a == 46:
       await message.answer('стул')
    if a == 47:
       await message.answer('кресло')
    if a == 48:
       await message.answer('батарея')
    if a == 49:
       await message.answer('двигатель')
    if a == 52:
       await message.answer('электричество')
    if a == 50:
       await message.answer('уголь')
    if a == 51:
       await message.answer('сом')