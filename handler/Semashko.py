from loader import dp, Bot
from aiogram import F
from aiogram.types import Message, FSInputFile, URLInputFile, BufferedInputFile
from aiogram.filters import Command



@dp.message(F.text == 'таблица')
async def func_name_1(message: Message):
    await message.answer(text = 'химия или математика или алфавит')

@dp.message(F.text =='химия')
async def func_name_2(message: Message):
    image = FSInputFile('data/image/3.png')
    await message.answer_photo(image, caption='ну бывает(я её ненавижу)')


@dp.message(F.text =='математика')
async def func_name_3(message: Message):
    image = FSInputFile('data/image/2.png')
    await message.answer_photo(image, caption='ну может забыл ,надеюсь не всю')

@dp.message(F.text =='алфавит')
async def func_name_3(message: Message):
    image = FSInputFile('data/image/4.png')
    await message.answer_photo(image, caption='эмм ладно...')

@dp.message(F.text ==('формулы'))
async def func_name_4(message: Message):
    await message.answer(text='Пифогора , Дисркеминанта , дальше лень')

@dp.message(F.text ==('Пифогора'))
async def func_name_5(message: Message):
    image = FSInputFile('data/image/5.png')
    await message.answer_photo(image, caption='')

@dp.message(F.text ==('Дисркеминанта'))
async def func_name_6(message: Message):
    image = FSInputFile('data/image/6.png')
    await message.answer_photo(image, caption='')