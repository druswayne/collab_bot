from loader import dp, Bot
from aiogram import F
from aiogram.types import Message, FSInputFile, URLInputFile, BufferedInputFile
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keyboard import *

@dp.message(Command('calc'))
async def Calculator(message: Message):
    await message.answer(text='Калькулятор')
    builder = ReplyKeyboardBuilder()
    for button in kb_menu:
        builder.add(button)
    builder.adjust(1)
    await message.answer(reply_markup=builder.as_markup(resize_keyboard=True),text='')