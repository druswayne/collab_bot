from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from loader import router

@router.message(Command('start'))
async def fun_start(message: Message):
    await message.answer(text="Добро пожаловать!")