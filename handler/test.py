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


@dp.message(Command('start'))
async def func_name_2(message: Message):
    """
    обработчик, который реагирует на команду /start
    """
    await message.answer(text='Ты нажал команду /start')


@dp.message(F.photo)
async def func_name_3(message: Message, bot: Bot):
    """
    обработчик, который реагирует на команду отправленные изображения
    """
    await bot.download(message.photo[-1],
                       f'data/image/{message.photo[-1].file_id}.jpg')
    await message.answer(text='Я сохранил твоё изображение')


@dp.message(Command('photo'))
async def func_name_4(message: Message):
    """
    обработчик, который реагирует на команду /photo
    """
    image = FSInputFile('data/image/1.jpg')

    await message.answer_photo(image, caption='держи фотку')
