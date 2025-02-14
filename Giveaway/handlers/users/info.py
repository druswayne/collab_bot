from aiogram.types import Message
from loader import router
from aiogram import F

@router.message(F.text == "Информация")
async def fun_start(message: Message):
    with open('data/info.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    await message.answer(content)